from sqlmodel import SQLModel, create_engine, Session, select, delete
from fastapi import FastAPI, HTTPException, Depends
from app.database.model import Login
from dotenv import load_dotenv
import os

load_dotenv()
mysqlLink = os.getenv("DB_URL")
engine = create_engine(mysqlLink, echo=True)
SQLModel.metadata.create_all(engine)

