from typing import Optional, List
from pydantic import BaseModel
from sqlmodel import Field, SQLModel, Relationship

# Many-to-Many relationship table linking Users and Groups
class UserGroupLink(SQLModel, table=True):
    user_id: int = Field(foreign_key="userdb.id", primary_key=True)
    group_id: int = Field(foreign_key="groupdb.id", primary_key=True)

# Base model for user input
class User(BaseModel):
    name: str
    display_name: str
    email: str
    password: str
    phone_number: str
    address: str

# Model for user output (includes user ID)
class UserOut(User):
    id: int

# Model for UserDB table in the database
class UserDB(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    display_name: str
    email: str
    password: str
    phone_number: str
    address: str

    # Relationship with groups
    groups: List["GroupDB"] = Relationship(back_populates="users", link_model=UserGroupLink)

# Base model for group input
class GroupBase(BaseModel):
    name: str

# Model for creating a group (includes user IDs to add to the group)
class GroupCreate(GroupBase):
    user_ids: List[int]

# Model for group output (includes group ID and size)
class GroupOut(GroupBase):
    id: int
    size: int  # Number of users in the group

# Model for GroupDB table in the database
class GroupDB(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str

    # Relationship with users
    users: List[UserDB] = Relationship(back_populates="groups", link_model=UserGroupLink)

    @property
    def size(self) -> int:
        return len(self.users)  # Calculate group size based on linked users
