from fastapi import FastAPI, HTTPException, Depends,Request
from sqlmodel import Session, create_engine, select
from pydantic import BaseModel
from database import get_session, init_db, engine
from models import UserDB, GroupDB, UserGroupLink, User, UserOut, GroupCreate, GroupOut
import jwt

# Initialize the database and app
init_db(engine)
get_session()
app = FastAPI()


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


SECRET_KEY = "your-secret-key"  # Change this to a secure secret key!

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
def add_favorite(slug: str, token: str = Depends(oauth2_scheme)):
    user_id = get_current_user(token)
    # Logic to add the favorite to the database
    return {"message": "Added to favorites"}

@app.delete("/api/favorites/{slug}")
def remove_favorite(slug: str, token: str = Depends(oauth2_scheme)):
    user_id = get_current_user(token)
    # Logic to remove the favorite from the database
    return {"message": "Removed from favorites"}


