from sqlmodel import SQLModel, create_engine, Session

DATABASE_URL = "sqlite:///data.db"
engine = create_engine(DATABASE_URL)

def init_db(engine):
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session