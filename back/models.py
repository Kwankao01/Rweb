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
    

class Availability(BaseModel):
    user_id: int 
    group_id : int
    date : list[date]  

class AvailableOut(Availability):
    id: int

class AvailableDB(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="userdb.id")  # Reference to the UserDB table
    group_id: int = Field(foreign_key="groupdb.id")  # Reference to the GroupDB table
    date: date

class Favorite(BaseModel):
    user_id: int
    landmark_id: Optional[int] = None
    hospitality_id: Optional[int] = None
    restaurant_id: Optional[int] = None
    transportation_id: Optional[int] = None

# Output model that includes an ID
class FavoriteOut(Favorite):
    id: int

# SQLModel for database representation
class FavoriteDB(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="userdb.id")
    landmark_id: Optional[int] = Field(default=None, foreign_key="landmarkdb.id")
    hospitality_id: Optional[int] = Field(default=None, foreign_key="hospitalitydb.id")
    restaurant_id: Optional[int] = Field(default=None, foreign_key="restaurantdb.id")
    transportation_id: Optional[int] = Field(default=None, foreign_key="transdb.id")

    user: Optional[UserDB] = Relationship(back_populates="favorites")
    landmark: Optional["LandmarkDB"] = Relationship(back_populates="favorites")
    hospitality: Optional["HospitalityDB"] = Relationship(back_populates="favorites")
    restaurant: Optional["RestaurantDB"] = Relationship(back_populates="favorites")
    transportation: Optional["TransDB"] = Relationship(back_populates="favorites") 
