from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_url = "postgresql://postgres:Rahul%40vanna@localhost:5432/Fastapi_db"
engine = create_engine(db_url)
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)