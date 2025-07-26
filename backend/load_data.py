from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASS')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)

SessionLocal = sessionmaker(bind=engine)
db = SessionLocal()

# Example load logic (replace with your CSV logic)
def load_users():
    df = pd.read_csv("users.csv")
    for _, row in df.iterrows():
        user = User(username=row["username"])
        db.add(user)
    db.commit()

if __name__ == "__main__":
    load_users()
