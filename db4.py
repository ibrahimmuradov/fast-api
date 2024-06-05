from sqlmodel import create_engine, SQLModel, Session


DATABASE_URL = 'sqlite:///db.sqlite'


engine = create_engine(DATABASE_URL, echo=True)  # create_engine - Creates an engine object to interact with
# the SQLite database, echo=True - enables logging of SQL statements


def init_db():
    SQLModel.metadata.create_all(engine)  # creates all tables in the database defined by the
    # SQLModel metadata


def get_session():  # provides a session context
    with Session(engine) as session:  # ensure the session is properly closed after use
        yield session  # used to provide the session to the caller.





