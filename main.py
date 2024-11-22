from sqlmodel import SQLModel, create_engine, Session, select, delete
from fastapi import FastAPI, HTTPException, Depends
from app.database.model import Login
from dotenv import load_dotenv
from pydantic import BaseModel
import os

load_dotenv()
mysqlLink = os.getenv("DB_URL")
engine = create_engine(mysqlLink, echo=True)
SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

class logincred(BaseModel):
    username: str
    password: str

app = FastAPI()

@app.post("/login")
def send_usename_and_password(login: logincred, session: Session = Depends(get_session)):
    statement = select(Login).where(Login.username == login.username)  # Query the database
    result = session.exec(statement).first()  # Fetch the first result

    if result:  # Check if a record is found
        result_dict = dict(result)
        if result_dict["username"] == login.username and result_dict["password"] == login.password:
            return {"message": "Ya welcome bel bash"}
        else:
            return {"message": "2tla3 bra ya 3bn el kaleb"}
    else:
        return {"message": "User not found, ya 2bny."}
