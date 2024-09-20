from sqlalchemy import Column, Integer, String,Boolean,Date,ForeignKey
from sqlalchemy.orm import relationship
from models.db import *
from datetime import date


class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String,nullable=False)
    priority = Column(Integer,default=1)
    date=Column(Date)
    is_complete= Column(Boolean,default=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    # Устанавливаем отношение с родительскими записями
    target = relationship("User", backref="tasks")

def set_date(self, value):

        self.date = date.fromisoformat(value)
def __repr__(self):
        return {
            "name":self.name,
            "priority":self.priority,
            "is_complete":self.is_complete,
            "date":self.date
        }

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    first_name=Column(String)
    last_name=Column(String)
    phone=Column(String,nullable=True)

    def __repr__(self):
        return {
            "id": self.id,
            "username": self.username,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "phone": self.phone
        }

Base.metadata.create_all(bind=engine)