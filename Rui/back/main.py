from fastapi import FastAPI, HTTPException, Depends
from sqlmodel import Session, create_engine, select
from database import engine, get_session, init_db
from models import UserDB, GroupDB, UserGroupLink, GroupCreate, UserOut, GroupOut, User

init_db()
app = FastAPI()

# คำสั่ง POST สำหรับสร้าง User
@app.post("/users", response_model=UserOut)
def create_user(user: User, session: Session = Depends(get_session)):
    # สร้างผู้ใช้ใหม่
    db_user = UserDB(name=user.name, display_name=user.display_name, email=user.email,
                     password=user.password, phone_number=user.phone_number, address=user.address)
    session.add(db_user)
    session.commit()
    session.refresh(db_user)  # รีเฟรชเพื่อให้ได้ id ของผู้ใช้
    return db_user

# คำสั่ง POST สำหรับสร้าง Group
@app.post("/groups", response_model=GroupOut)
def create_group(group: GroupCreate, session: Session = Depends(get_session)):
    # สร้างกลุ่มใหม่
    db_group = GroupDB(name=group.name)
    session.add(db_group)
    session.commit()
    session.refresh(db_group)  # รีเฟรชเพื่อให้ได้ id ของกลุ่ม

    # เชื่อมโยงผู้ใช้กับกลุ่ม
    for user_id in group.user_ids:
        db_user_group = UserGroupLink(user_id=user_id, group_id=db_group.id)
        session.add(db_user_group)

    session.commit()  # บันทึกการเชื่อมโยง
    return db_group

# คำสั่ง GET สำหรับดึงข้อมูลกลุ่ม
@app.get("/groups/{group_id}", response_model=GroupOut)
def get_group(group_id: int, session: Session = Depends(get_session)):
    # ดึงข้อมูลกลุ่ม
    db_group = session.exec(select(GroupDB).where(GroupDB.id == group_id)).first()
    if db_group is None:
        raise HTTPException(status_code=404, detail="Group not found")
    return db_group

# คำสั่ง GET สำหรับดึงข้อมูลผู้ใช้
@app.get("/users/{user_id}", response_model=UserOut)
def get_user(user_id: int, session: Session = Depends(get_session)):
    # ดึงข้อมูลผู้ใช้
    db_user = session.exec(select(UserDB).where(UserDB.id == user_id)).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
