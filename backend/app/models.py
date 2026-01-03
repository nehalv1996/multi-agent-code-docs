from sqlalchemy import Column, String
from uuid import uuid4
from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, default=lambda: str(uuid4()))
    email = Column(String, unique=True, index=True)
    password = Column(String)
    role = Column(String, default="USER")

class Project(Base):
    __tablename__ = "projects"

    id = Column(String, primary_key=True, default=lambda: str(uuid4()))
    owner_email = Column(String)
    name = Column(String)
    personas = Column(String)
    status = Column(String, default="CREATED")