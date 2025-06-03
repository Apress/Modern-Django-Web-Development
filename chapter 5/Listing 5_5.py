#Listing 5_5: alembic migration
from sqlalchemy import Column, Integer, String


class Base(DeclarativeBase):
    pass

class Book(Base):
    __tablename__ = 'Books'
    
    id = mapped_column(Integer, primary_key=True, index=True)
    title = Column(String)
    author = mapped_column(String(256))
    price = mapped_column(Integer)
    publisher = mapped_column(String(256))
    year_of_pub = mapped_column(Integer)
