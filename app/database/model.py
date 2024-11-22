from sqlmodel import SQLModel, create_engine, Session, Field

class Login(SQLModel, table=True):
    __tablename__ = "login"
    id: int | None = Field(primary_key=True)
    username: str
    password: str