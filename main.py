from sqlmodel import SQLModel, create_engine, Session
from dotenv import load_dotenv
import os

load_dotenv()

mysqlLink = os.getenv("DB_URL")

engine = create_engine(mysqlLink, echo=True)

def get_session():
    with Session(engine) as session:
        yield session