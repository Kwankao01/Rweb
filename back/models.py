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
    
#------------------ Restaurants ---------------------

# Class สำหรับเก็บข้อมูลร้านอาหาร
class Restaurant(BaseModel):
    title: str  # ชื่อร้าน
    slug: str  # slug หรือ URL-friendly identifier
    image: str  # รูปภาพของร้าน
    rating: float  # คะแนนรีวิว
    reviews: int  # จำนวนรีวิว
    price: int  # ราคาโดยประมาณ
    cancellation: Optional[str] = None  # ข้อความการยกเลิก
    city: str  # เมืองที่ตั้งร้าน
    content: str  # รายละเอียดเกี่ยวกับร้าน
    type: str  # ประเภทของร้าน (Restaurant)

# Output ที่ใช้ในการแสดงผล
class RestaurantOut(Restaurant):
    id: int  # id ของร้านในฐานข้อมูล

# Model สำหรับบันทึกข้อมูลในฐานข้อมูล
class RestaurantDB(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)  # ID สำหรับบันทึกในฐานข้อมูล
    title: str  # ชื่อร้าน
    slug: str  # slug หรือ URL-friendly identifier
    image: str  # รูปภาพของร้าน
    rating: float  # คะแนนรีวิว
    reviews: int  # จำนวนรีวิว
    price: int  # ราคาโดยประมาณ
    cancellation: Optional[str] = None  # ข้อความการยกเลิก
    city: str  # เมืองที่ตั้งร้าน
    content: str  # รายละเอียดเกี่ยวกับร้าน
    type: str  # ประเภทของร้าน (Restaurant)

    # สามารถเพิ่มฟิลด์อื่นๆ เช่น favorites หากจำเป็น
    favorites: List["FavoriteDB"] = Relationship(back_populates="restaurant")

# Response สำหรับการอัพเดต
class UpdateResponse(BaseModel):
    message: str
    restaurant: Optional[Restaurant] = None


#------------------- Hotel -----------------------

# Class สำหรับเก็บข้อมูลโรงแรม
class Hotel(BaseModel):
    title: str  # ชื่อโรงแรม
    slug: str  # slug หรือ URL-friendly identifier
    image: str  # รูปภาพของโรงแรม
    rating: float  # คะแนนรีวิว
    reviews: int  # จำนวนรีวิว
    price: int  # ราคาโดยประมาณต่อคืน
    cancellation: Optional[str] = None  # ข้อความการยกเลิก
    city: str  # เมืองที่ตั้งโรงแรม
    content: str  # รายละเอียดเกี่ยวกับโรงแรม
    type: str = "Hotel"  # ประเภทของสถานที่ (Hotel)

# Output ที่ใช้ในการแสดงผล
class HotelOut(Hotel):
    id: int  # id ของโรงแรมในฐานข้อมูล

# Model สำหรับบันทึกข้อมูลในฐานข้อมูล
class HotelDB(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)  # ID สำหรับบันทึกในฐานข้อมูล
    title: str  # ชื่อโรงแรม
    slug: str  # slug หรือ URL-friendly identifier
    image: str  # รูปภาพของโรงแรม
    rating: float  # คะแนนรีวิว
    reviews: int  # จำนวนรีวิว
    price: int  # ราคาโดยประมาณต่อคืน
    cancellation: Optional[str] = None  # ข้อความการยกเลิก
    city: str  # เมืองที่ตั้งโรงแรม
    content: str  # รายละเอียดเกี่ยวกับโรงแรม
    type: str = "Hotel"  # ประเภทของสถานที่ (Hotel)

    # สามารถเพิ่มฟิลด์อื่นๆ เช่น favorites หากจำเป็น
    favorites: List["FavoriteDB"] = Relationship(back_populates="hotel")

# Response สำหรับการอัพเดต
class UpdateResponse(BaseModel):
    message: str
    hotel: Optional[Hotel] = None

#---------------------- Landmarks ------------------------

# Class สำหรับเก็บข้อมูล Landmark
class Landmark(BaseModel):
    title: str  # ชื่อของ Landmark
    slug: str  # slug หรือ URL-friendly identifier
    image: str  # รูปภาพของ Landmark
    rating: float  # คะแนนรีวิว
    reviews: int  # จำนวนรีวิว
    price: int  # ราคาโดยประมาณ
    cancellation: Optional[str] = None  # ข้อความการยกเลิก
    city: str  # เมืองที่ตั้ง Landmark
    content: str  # รายละเอียดเกี่ยวกับ Landmark
    type: str  # ประเภท (Landmark)

# Output ที่ใช้ในการแสดงผล
class LandmarkOut(Landmark):
    id: int  # id ของ Landmark ในฐานข้อมูล

# Model สำหรับบันทึกข้อมูลในฐานข้อมูล
class LandmarkDB(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)  # ID สำหรับบันทึกในฐานข้อมูล
    title: str  # ชื่อของ Landmark
    slug: str  # slug หรือ URL-friendly identifier
    image: str  # รูปภาพของ Landmark
    rating: float  # คะแนนรีวิว
    reviews: int  # จำนวนรีวิว
    price: int  # ราคาโดยประมาณ
    cancellation: Optional[str] = None  # ข้อความการยกเลิก
    city: str  # เมืองที่ตั้ง Landmark
    content: str  # รายละเอียดเกี่ยวกับ Landmark
    type: str  # ประเภทของ Landmark (เช่น Landmark)

    # สามารถเพิ่มฟิลด์อื่นๆ เช่น favorites หากจำเป็น
    favorites: List["FavoriteDB"] = Relationship(back_populates="landmark")

# Response สำหรับการอัพเดต
class UpdateResponse(BaseModel):
    message: str
    landmark: Optional[Landmark] = None

# ---------------Trip ---------------------

# Association Table for Trip Details
class TripDetailDB(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    trip_id: int = Field(foreign_key="tripdb.id")
    hotel_id: Optional[int] = Field(default=None, foreign_key="hoteldb.id")
    restaurant_id: Optional[int] = Field(default=None, foreign_key="restaurantdb.id")
    landmark_id: Optional[int] = Field(default=None, foreign_key="landmarkdb.id")

    # Relationships to each entity
    trip: "TripDB" = Relationship(back_populates="trip_details")
    hotel: Optional["HotelDB"] = Relationship()
    restaurant: Optional["RestaurantDB"] = Relationship()
    landmark: Optional["LandmarkDB"] = Relationship()

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
    trip_details: List[TripDetailDB] = Relationship(back_populates="trip")
 
    def duration(self) -> int:
        return (self.end - self.start).days + 1
 
    def countdown(self) -> int:
        today = date.today()
        return max(0, (self.start - today).days)
 
class TripOut(Trip):
    id: int
    duration: int
    countdown: int

# Input Model for Adding Trip Details
class TripDetail(BaseModel):
    trip_id: int
    hotel_ids: Optional[List[int]] = None
    restaurant_ids: Optional[List[int]] = None
    landmark_ids: Optional[List[int]] = None

# Output Model for Trip Details
class TripDetailOut(BaseModel):
    id: int
    trip_id: int
    hotels: Optional[List[HotelOut]] = None
    restaurants: Optional[List[RestaurantOut]] = None
    landmarks: Optional[List[LandmarkOut]] = None


    
#------------- Avalible -------------

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
    hotel_id: Optional[int] = Field(default=None, foreign_key="hoteldb.id")
    restaurant_id: Optional[int] = Field(default=None, foreign_key="restaurantdb.id")

    user: UserDB = Relationship(back_populates="favorites")
    landmark: Optional["LandmarkDB"] = Relationship(back_populates="favorites")
    hotel: Optional["HotelDB"] = Relationship(back_populates="favorites")
    restaurant: Optional["RestaurantDB"] = Relationship(back_populates="favorites") 

