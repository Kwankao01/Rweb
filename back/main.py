from fastapi import FastAPI, HTTPException, Depends
from sqlmodel import Session, create_engine, select
from passlib.context import CryptContext
from pydantic import BaseModel
from database import get_session, init_db
from models import UserDB, GroupDB, UserGroupLink, User, UserOut, GroupCreate, GroupOut

# Initialize the database and app
DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL, echo=True)
init_db(engine)

app = FastAPI()

# Password hashing utility
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

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


@app.post("/login", response_model=LoginResponse)
def login(request: LoginRequest, session: Session = Depends(get_session)):
    # Look for the user by email
    db_user = session.exec(select(UserDB).where(UserDB.email == request.email)).first()
    if not db_user:
        raise HTTPException(status_code=400, detail="Invalid email or password")
    
    # Verify the provided password
    if not pwd_context.verify(request.password, db_user.password):
        raise HTTPException(status_code=400, detail="Invalid email or password")
    
    return {"message": "Login successful", "user": db_user}

@app.post("/groups", response_model=GroupOut)
def create_group(group: GroupCreate, session: Session = Depends(get_session)):
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
def get_group(group_id: int, session: Session = Depends(get_session)):
    db_group = session.exec(select(GroupDB).where(GroupDB.id == group_id)).first()
    if not db_group:
        raise HTTPException(status_code=404, detail="Group not found")
    return db_group

@app.get("/users/{user_id}", response_model=UserOut)
def get_user(user_id: int, session: Session = Depends(get_session)):
    db_user = session.exec(select(UserDB).where(UserDB.id == user_id)).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
