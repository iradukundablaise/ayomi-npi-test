from sqlmodel import SQLModel, Field

class Result(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    express: str
    results: int