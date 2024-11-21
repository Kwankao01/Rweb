from sqlmodel import SQLModel, create_engine, Session

# Define the absolute path to your database file
DATABASE_URL = "sqlite:///C:/Users/kullanit/Rproject/Rweb/data.db"

# Create the database engine
engine = create_engine(DATABASE_URL, echo=True)

def init_db(engine_param=None):
    """
    Initialize the database by creating all tables.
    If an engine is provided, use it; otherwise, use the global engine.
    """
    if engine_param is None:
        engine_param = engine
    SQLModel.metadata.create_all(engine_param)

def get_session():
    """
    Provide a database session for dependency injection.
    This uses the global engine defined above.
    """
    with Session(engine) as session:
        yield session
