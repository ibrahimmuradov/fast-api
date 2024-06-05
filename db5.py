from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


DATABASE_URL = "sqlite:///db.sqlite"

engine = create_engine(DATABASE_URL)  # create_engine - creates a new SQLAlchemy engine instance

SessionLocal = sessionmaker(bind=engine)  # sessionmaker - creates a custom Session class.

Base = declarative_base()  # Creates a base class for defining ORM models


