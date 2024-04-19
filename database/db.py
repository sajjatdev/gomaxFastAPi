import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Development and production Settings
env_file = ".env.prod" if os.getenv("MODE_ENV") == "production" else ".env.dev"
load_dotenv(env_file)
# END

DB_NAME=os.getenv("POSTGRES_DB")
DB_USERNAME=os.getenv("POSTGRES_USER")
DB_PASSWORD=os.getenv("POSTGRES_PASSWORD")
DB_SERVER=os.getenv("POSTGRES_SERVER")

SQLALCHEMY_DATABASE_URL = f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_SERVER}/{DB_NAME}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()