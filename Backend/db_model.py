from sqlalchemy import Column,Integer,FLOAT,String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Product(Base):

    __tablename__ = "products"

    id = Column(Integer, primary_key=True ,index=True)
    name = Column(String(50))
    price = Column(FLOAT)
    description = Column(String(250))
    quantity = Column(Integer())