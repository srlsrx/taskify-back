from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from models import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False)
    password = Column(String(100), nullable=False)
    is_admin = Column(Boolean, default=False)
    tasks = relationship("Task", back_populates="user")

    def __repr__(self):
        return f"<User(id={self.id}, username='{self.username}', email='{self.email}', is_admin={self.is_admin})>"
