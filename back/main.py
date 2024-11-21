from fastapi import FastAPI, HTTPException, Depends,Request
from fastapi.security import OAuth2PasswordBearer
from typing import Union
from sqlalchemy import func, delete
from sqlmodel import Session, create_engine, select
from pydantic import BaseModel
from database import get_session, init_db, engine
from models import *
import jwt


# Initialize the database and app
init_db(engine)
get_session()
app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

# Login request and response models
class LoginRequest(BaseModel):
    email: str
    password: str

class LoginResponse(BaseModel):
    message: str
    user: UserOut = None

@app.post("/users", response_model=UserOut)
def create_user(user: User, session: Session = Depends(get_session)):
    # Directly store the plaintext password
    db_user = UserDB(
        name=user.name,
        display_name=user.display_name,
        email=user.email,
        password=user.password,  # Store password as is
        phone_number=user.phone_number,
        address=user.address,
        
    )
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user


SECRET_KEY = "boomboom"  

# Login Endpoint with Token Generation
@app.post("/login")
def login(user: LoginRequest, session: Session = Depends(get_session)):
    # Fetch the user from the database
    db_user = session.exec(select(UserDB).where(UserDB.email == user.email)).first()
    if not db_user or db_user.password != user.password:
        raise HTTPException(status_code=400, detail="Invalid email or password")

    # Generate a JWT token
    token = jwt.encode({"user_id": db_user.id}, SECRET_KEY, algorithm="HS256")

    # Return token and user ID
    return {"token": token, "user_id": db_user.id, "message": "Login successful"}



#Create a function to check the token from the database for protected endpoints:
def get_current_user(request: Request, session: Session = Depends(get_session)):
    # Extract Authorization header
    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        raise HTTPException(status_code=403, detail="Authorization token is missing or invalid")

    token = auth_header.split(" ")[1]
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
    except jwt.PyJWTError:
        raise HTTPException(status_code=403, detail="Invalid or expired token")

    # Fetch user from token payload
    user_id = payload.get("user_id")
    db_user = session.exec(select(UserDB).where(UserDB.id == user_id)).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    
    return db_user


@app.post("/groups", response_model=GroupCreateOut)
def create_group(group: GroupCreate, session: Session = Depends(get_session), user=Depends(get_current_user)):
    db_group = GroupDB(name=group.name)
    session.add(db_group)
    session.commit()
    session.refresh(db_group)
    
    # Add current user to the group
    user_group = UserGroupLink(user_id=user.id, group_id=db_group.id)
    session.add(user_group)

    # Add other users to the group
    for user_id in group.user_ids:
        if user_id != user.id:  # Skip current user, already added
            user_group = UserGroupLink(user_id=user_id, group_id=db_group.id)
            session.add(user_group)

    session.commit()
    
    return {"id": db_group.id, "name": db_group.name, "invite_code": db_group.invite_code}

@app.post("/groups/join")
def join_group(request: JoinGroupRequest, session: Session = Depends(get_session), user=Depends(get_current_user)):
    # Find the group with the provided invite code
    db_group = session.exec(select(GroupDB).where(GroupDB.invite_code == request.invite_code)).first()
    
    if not db_group:
        raise HTTPException(status_code=404, detail="Invalid invite code")
    
    # Check if user is already in the group
    existing_link = session.exec(
        select(UserGroupLink)
        .where(UserGroupLink.user_id == user.id)
        .where(UserGroupLink.group_id == db_group.id)
    ).first()
    
    if existing_link:
        raise HTTPException(status_code=400, detail="User already in group")
    
    # Add user to the group
    user_group = UserGroupLink(user_id=user.id, group_id=db_group.id)
    session.add(user_group)
    session.commit()
    
    return {"message": "Joined group successfully"}

@app.post("/users/find")
def find_users_by_email(
    emails: dict,
    session: Session = Depends(get_session),
    current_user: UserDB = Depends(get_current_user)
):
    users = session.exec(
        select(UserDB)
        .where(UserDB.email.in_(emails['emails']))
    ).all()
    
    return users

@app.get("/groups")
def get_groups(session: Session = Depends(get_session), user=Depends(get_current_user)):
    user_groups = session.exec(
        select(GroupDB)
        .join(UserGroupLink)
        .where(UserGroupLink.user_id == user.id)
    ).all()
    return user_groups

@app.get("/users/{user_id}", response_model=UserOut)
def get_user(user_id: int, session: Session = Depends(get_session), user=Depends(get_current_user)):
    db_user = session.exec(select(UserDB).where(UserDB.id == user_id)).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

# Trip

@app.post("/trips/", response_model=TripOut)
def create_trip(trip: Trip, session: Session = Depends(get_session)):
    if not session.get(GroupDB, trip.group_id):
        raise HTTPException(status_code=404, detail="Group not found")

    trip_db = TripDB(**trip.model_dump())
    session.add(trip_db)
    session.commit()
    session.refresh(trip_db)

    return TripOut(**trip_db.model_dump(), duration=trip_db.duration(), countdown=trip_db.countdown())

@app.get("/trips/", response_model=list[TripOut])
def get_all_trips(session: Session = Depends(get_session), user=Depends(get_current_user)):
    user_groups = select(GroupDB.id).join(UserGroupLink).where(UserGroupLink.user_id == user.id)
    trips = session.exec(select(TripDB).where(TripDB.group_id.in_(user_groups))).all()
    return [TripOut(**trip.model_dump(), duration=trip.duration(), countdown=trip.countdown()) for trip in trips]

@app.put("/trips/{trip_id}", response_model=TripOut)
def update_trip(trip_id: int, trip: Trip, session: Session = Depends(get_session)):
    existing_trip = session.get(TripDB, trip_id)
    if not existing_trip:
        raise HTTPException(status_code=404, detail="Trip not found")

    # Update the trip details
    for key, value in trip.model_dump().items():
        setattr(existing_trip, key, value)

    session.add(existing_trip)
    session.commit()
    session.refresh(existing_trip)

    return TripOut(**existing_trip.model_dump(), duration=existing_trip.duration(), countdown=existing_trip.countdown())

@app.delete("/trips/{trip_id}", response_model=dict)
def delete_trip(trip_id: int, session: Session = Depends(get_session)):
    trip = session.get(TripDB, trip_id)
    if not trip:
        raise HTTPException(status_code=404, detail="Trip not found")

    session.delete(trip)
    session.commit()

    return {"message": f"Trip {trip_id} deleted successfully"}

# availability

@app.post("/availability", response_model=dict)
def add_availability(availability: Availability, session: Session = Depends(get_session)):
    try:
        # Check if group exists
        group = session.get(GroupDB, availability.group_id)
        if not group:
            raise HTTPException(status_code=404, detail="Group not found")

        # Check if user is a member of the group
        membership = session.exec(select(UserGroupLink).where(
            UserGroupLink.group_id == availability.group_id,
            UserGroupLink.user_id == availability.user_id
        )).first()

        if not membership:
            raise HTTPException(status_code=403, detail="User is not a member of the group")
        
        # Check if availability already exists for each date
        existing_availabilities = session.exec(select(AvailableDB).where(
            AvailableDB.user_id == availability.user_id,
            AvailableDB.group_id == availability.group_id,
            AvailableDB.date.in_(availability.date)
        )).all()

        existing_dates = {av.date for av in existing_availabilities}
        new_dates = set(availability.date) - existing_dates

        if not new_dates:
            raise HTTPException(status_code=400, detail="Availability already exists for the provided dates")

        # Add availability for each new date
        for date in new_dates:
            db_availability = AvailableDB(user_id=availability.user_id, group_id=availability.group_id, date=date)
            session.add(db_availability)

        session.commit()

        return {"message": "Availability added successfully"}

    except Exception as e:
        print(f"Error: {e}")  # Log the error
        raise HTTPException(status_code=500, detail=str(e))

    
@app.get("/groups/{group_id}/available-dates/", response_model=Union[list[date], str])
def find_perfect_dates(group_id: int, session: Session = Depends(get_session)):
    # Check if the group exists
    group = session.get(GroupDB, group_id)
    if not group:
        raise HTTPException(status_code=404, detail="Group not found")
    
    # Get user_ids of members in the group
    user_ids = session.exec(
        select(UserGroupLink.user_id).where(UserGroupLink.group_id == group_id)
    ).all()
    
    if not user_ids:
        raise HTTPException(status_code=404, detail="No members in the group")
    
    # Find the perfect available dates common to all users
    available_dates = session.exec(
        select(AvailableDB.date)
        .where(AvailableDB.user_id.in_(user_ids))  # Select dates for the users in the group
        .group_by(AvailableDB.date)  # Group by the date
        .having(func.count(AvailableDB.user_id) == len(user_ids))  # Ensure all members are available on that date
    ).all()

    # Return available dates or a message if none found
    return available_dates if available_dates else "No matching dates found"

@app.put("/availability/group/{group_id}/user/{user_id}", response_model=dict)
def update_availability(group_id: int, user_id: int, availability_data: Availability, session: Session = Depends(get_session)):
    # Validate group and membership
    if not session.get(GroupDB, group_id):
        raise HTTPException(status_code=404, detail="Group not found")
    if not session.exec(select(UserGroupLink).where(UserGroupLink.group_id == group_id, UserGroupLink.user_id == user_id)).first():
        raise HTTPException(status_code=403, detail="User is not a member of the group")
    
    # Delete old availability using delete statement
    session.exec(
        delete(AvailableDB).where(AvailableDB.group_id == group_id, AvailableDB.user_id == user_id)
    )
    
    # Insert new availability dates
    session.bulk_save_objects([AvailableDB(user_id=user_id, group_id=group_id, date=date) for date in availability_data.date])
    
    session.commit()
    return {"message": "Availability updated successfully"}


#fav

@app.post("/api/favorites/{slug}")
async def add_favorite(
    slug: str, 
    current_user: UserDB = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    # Create new favorite
    favorite = FavoriteDB(user_id=current_user.id, slug=slug)
    session.add(favorite)
    try:
        session.commit()
        return {"message": "Added to favorites", "slug": slug}
    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=400, detail=str(e))

@app.delete("/api/favorites/{slug}")
async def remove_favorite(
    slug: str,
    current_user: UserDB = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    # Find and remove favorite
    favorite = session.exec(
        select(FavoriteDB)
        .where(FavoriteDB.user_id == current_user.id)
        .where(FavoriteDB.slug == slug)
    ).first()
    
    if not favorite:
        raise HTTPException(status_code=404, detail="Favorite not found")
        
    session.delete(favorite)
    try:
        session.commit()
        return {"message": "Removed from favorites", "slug": slug}
    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=400, detail=str(e))


