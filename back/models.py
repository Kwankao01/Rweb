from typing import Optional, List
from pydantic import BaseModel
from sqlmodel import Field, SQLModel, Relationship

# โมเดลที่ใช้ในการเชื่อมโยง UserDB และ GroupDB
class UserGroupLink(SQLModel, table=True):
    user_id: int = Field(foreign_key="userdb.id", primary_key=True)
    group_id: int = Field(foreign_key="groupdb.id", primary_key=True)

# โมเดลสำหรับข้อมูลผู้ใช้
class User(BaseModel):
    name: str
    display_name: str
    email: str
    password: str
    phone_number: str
    address: str

# โมเดลสำหรับการแสดงผลข้อมูลผู้ใช้พร้อม id
class UserOut(User):
    id: int

# โมเดลที่ใช้สำหรับฐานข้อมูลในตาราง User
class UserDB(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    display_name: str
    email: str
    password: str
    phone_number: str
    address: str

    # ความสัมพันธ์ Many-to-Many กับ GroupDB โดยใช้ UserGroupLink
    groups: List["GroupDB"] = Relationship(back_populates="users", link_model=UserGroupLink)

# โมเดลสำหรับข้อมูลกลุ่ม
class GroupBase(BaseModel):
    name: str

# โมเดลสำหรับการสร้างกลุ่ม โดยกำหนด user_ids ที่จะเพิ่มในกลุ่ม
class GroupCreate(GroupBase):
    user_ids: List[int]

# โมเดลสำหรับการแสดงผลข้อมูลกลุ่มพร้อม id และขนาดกลุ่ม
class GroupOut(GroupBase):
    id: int
    size: int  # จำนวนผู้ใช้ในกลุ่ม

# โมเดลที่ใช้สำหรับฐานข้อมูลในตาราง Group
class GroupDB(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str

    # ความสัมพันธ์ Many-to-Many กับ UserDB โดยใช้ UserGroupLink
    users: List[UserDB] = Relationship(back_populates="groups", link_model=UserGroupLink)

    @property
    def size(self) -> int:
        return len(self.users)  # คำนวณขนาดกลุ่มจากจำนวนผู้ใช้ที่เชื่อมโยง
