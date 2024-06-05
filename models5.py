from sqlalchemy import Column, Integer, String, ForeignKey, Enum as SQLEnum
from sqlalchemy.orm import relationship
from db5 import Base, engine
from services.choices5 import Genre


class Book(Base):
    __tablename__ = 'book'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    genre = Column(SQLEnum(Genre))
    publisher = relationship("Publisher", back_populates="book")


class Publisher(Base):
    __tablename__ = 'publisher'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    release_date = Column(String, index=True)
    book_id = Column(Integer, ForeignKey("book.id"))
    book = relationship("Book", back_populates="publisher")


Base.metadata.create_all(bind=engine)

