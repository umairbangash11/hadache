# from sqlalchemy import Boolean, Column, Integer, ForeignKey, String
# from sqlalchemy.orm import relationship
# from database import Base





# class UserToRole(Base):
#     __tablename__ = "User_to_roles"

#     user_id = Column(ForeignKey("users.id"), primary_key=True)
#     role_id = Column(ForeignKey("roles.id"), primary_key=True)
#     user = relationship("User", back_populates="roles")
#     role = relationship("Role", back_populates="users")

# class User(Base):
#     __tablename__= "users"

#     id = Column(Integer, primary_key=True, index=True)
#     username = Column(String)
#     email = Column(String)
#     password = Column(String)
#     roles = relationship("UserToRole", back_populates="user")

# class Role(Base):
#     __tablename__ = "roles"

#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String)
#     users = relationship("UserToRole", back_populates="role")
    

from typing import List, Optional
from sqlmodel import Field, SQLModel, Relationship, ForeignKey, Session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

DATABASE_URL = "postgresql://umairbangash272:tnMO4LxeI9Cv@ep-soft-butterfly-a59l1ip0.us-east-2.aws.neon.tech/new?sslmode=require"

# SQLAlchemy Engine
engine = create_engine(DATABASE_URL)

# SessionMaker for SQLAlchemy
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str
    email: str
    password: str
    roles: List["UserToRole"] = Relationship(back_populates="user")


class Role(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    users: List["UserToRole"] = Relationship(back_populates="role")


class UserToRole(SQLModel, table=True):
    user_id: int = Field(primary_key=True)
    role_id: int = Field(primary_key=True)
    user: Optional[User] = Relationship(back_populates="roles")
    role: Optional[Role] = Relationship(back_populates="users")

    user_fkey: int = ForeignKey("users.id")
    role_fkey: int = ForeignKey("roles.id")


def get_session():
    with SessionLocal() as session:
        yield session

def create_tables():
    SQLModel.metadata.create_all(engine)

create_tables()
  










    

    

