#Listing 5_2: SQLAlchemy model
from sqlalchemy import Column, Integer, String


class Base(DeclarativeBase):
    pass

class Book(Base):
    __tablename__ = 'Books'
    
    id = mapped_column(Integer, primary_key=True, index=True)
    title = mapped_column(String(256))
    author = mapped_column(String(256))
    price = mapped_column(Integer)
    publisher = mapped_column(String(256))
