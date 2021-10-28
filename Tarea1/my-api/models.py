# timedatectl set-local-rtc true 
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String,Date
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import false

from .database import Base #Se importa el objeto Base desde el archivo database.py

class News(Base): 

    __tablename__ = "news"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50), index=True)
    url = Column(String(300), index=True)
    media_outlet = Column(String(50))
    date = Column(Date(), unique=False, index=True)
    category = Column(String(50), index=False, unique=False)
    #has_category = relationship("Category", back_populates="owner")
'''
class Category(Base):

    __tablename__ = "has_category"

    id = Column(Integer, primary_key=True, index=True)
    value = Column(String(50), index=True)

    owner = relationship("News", back_populates="has_category")
'''