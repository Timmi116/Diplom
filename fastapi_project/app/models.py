from sqlalchemy import Column, Integer, String, Date, Text, LargeBinary
from .database import Base

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    username = Column(String)
    age = Column(Integer)
    gender = Column(String)
    email = Column(String)
    password = Column(String)
    date_of_birth = Column(Date)
    place_of_birth = Column(String)
    address = Column(Text)
    biography = Column(Text)
    profile_picture = Column(LargeBinary)