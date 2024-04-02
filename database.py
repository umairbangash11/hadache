from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL="postgresql://umairbangash272:tnMO4LxeI9Cv@ep-soft-butterfly-a59l1ip0.us-east-2.aws.neon.tech/int?sslmode=require"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
def get_session():
    with Session(engine) as session:
        yield session