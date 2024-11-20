from fastapi import FastAPI, HTTPException, Depends,Request
from fastapi.security import OAuth2PasswordBearer
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



@app.post("/groups", response_model=GroupOut)
def create_group(group: GroupCreate, session: Session = Depends(get_session), user=Depends(get_current_user)):
    # Create the group
    db_group = GroupDB(name=group.name)
    session.add(db_group)
    session.commit()
    session.refresh(db_group)

    # Link users to the group
    for user_id in group.user_ids:
        db_user_group = UserGroupLink(user_id=user_id, group_id=db_group.id)
        session.add(db_user_group)

    session.commit()
    return db_group


@app.get("/groups/{group_id}", response_model=GroupOut)
def get_group(group_id: int, session: Session = Depends(get_session), user=Depends(get_current_user)):
    db_group = session.exec(select(GroupDB).where(GroupDB.id == group_id)).first()
    if not db_group:
        raise HTTPException(status_code=404, detail="Group not found")
    return db_group

@app.get("/users/{user_id}", response_model=UserOut)
def get_user(user_id: int, session: Session = Depends(get_session), user=Depends(get_current_user)):
    db_user = session.exec(select(UserDB).where(UserDB.id == user_id)).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


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


