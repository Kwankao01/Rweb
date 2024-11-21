from typing import Optional, List
from pydantic import BaseModel
from sqlmodel import Field, SQLModel, Relationship
from datetime import date
import random,string

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
    favorites: List["FavoriteDB"] = Relationship(back_populates="user")

# Base model for group input
class GroupBase(BaseModel):
    name: str

# Model for creating a group (includes user IDs to add to the group)
class GroupCreate(GroupBase):
    user_ids: List[int]

class GroupCreateOut(BaseModel):
    id: int
    name: str 
    invite_code: str

# Model for group output (includes group ID and size)
class GroupOut(GroupBase):
    id: int
    size: int  # Number of users in the group

def generate_invite_code():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))

# Model for GroupDB table in the database
class GroupDB(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    invite_code: str = Field(default_factory=generate_invite_code, unique=True)

    # Relationship with users
    users: List[UserDB] = Relationship(back_populates="groups", link_model=UserGroupLink)
    trips: List["TripDB"] = Relationship(back_populates="group")

    @property
    def size(self) -> int:
        return len(self.users)  # Calculate group size based on linked users
    
class JoinGroupRequest(BaseModel):
    invite_code: str
    
# Restaurants

class Restaurant(BaseModel):
    name: str
    address: str
    type: str
    rate: float = Field(default=5.0)
 
class RestaurantOut(Restaurant):
    id: int
 
class RestaurantDB(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    address: str
    type: str
    rate: float
    favorites: list["FavoriteDB"] = Relationship(back_populates="restaurant")

class UpdateResponse(BaseModel):
    message: str
    restaurant: Optional[Restaurant] = None

# Hospitalities

class Hospitality(BaseModel):
    name: str
    type: str
    address : str
    price: int
    rate: float = Field(default=5.0)

class HospitalityOut(Hospitality):
    id: int

class HospitalityDB(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    type: str
    address : str
    price: int
    rate : float
    favorites: list["FavoriteDB"] = Relationship(back_populates="hospitality")

# Landmarks

class Landmark(BaseModel):
    name: str
    address: str
    fee: float
    type: str
    rate: float = Field(default=5.0)  

class LandmarkOut(Landmark):
    id: int

class LandmarkDB(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    address: str
    fee: float
    type: str
    rate: float
    favorites: list["FavoriteDB"] = Relationship(back_populates="landmark")

# Trip
class Trip(BaseModel):
    name: str
    destination: str
    start: date
    end: date
    group_id: int  
 
class TripDB(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    destination: str
    start: date
    end: date
    group_id: int = Field(foreign_key="groupdb.id")  
    group: Optional["GroupDB"] = Relationship(back_populates="trips")  
 
    def duration(self) -> int:
        return (self.end - self.start).days + 1
 
    def countdown(self) -> int:
        today = date.today()
        return max(0, (self.start - today).days)
 
class TripOut(Trip):
    id: int
    duration: int
    countdown: int
    
#Avalible

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

    user: UserDB = Relationship(back_populates="favorites")
    landmark: Optional["LandmarkDB"] = Relationship(back_populates="favorites")
    hospitality: Optional["HospitalityDB"] = Relationship(back_populates="favorites")
    restaurant: Optional["RestaurantDB"] = Relationship(back_populates="favorites") 

