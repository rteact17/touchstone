from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import psycopg2
import os

app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class User(BaseModel):
    firstname: str
    lastname: str
    email: str
    phone: str

conn = psycopg2.connect(
    host="dpg-cvscdluuk2gs739rvjq0-a.oregon-postgres.render.com",
    database="touchstone",
    user="touchstone_user",
    password="jjbn8046mBOfhroURnSmpcXxI0A4rcrg"
    # host=os.getenv("DB_HOST"),
    # database=os.getenv("DB_NAME"),
    # user=os.getenv("DB_USER"),
    # password=os.getenv("DB_PASS")
)
cursor = conn.cursor()

# Create table if not exists
# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS users (
#         id SERIAL PRIMARY KEY,
#         firstname TEXT,
#         lastname TEXT,
#         email TEXT,
#         phone TEXT
#     )
# ''')
# conn.commit()

@app.post("/users")
def create_user(user: User):
    cursor.execute("INSERT INTO users (firstname, lastname, email, phone) VALUES (%s, %s, %s, %s)",
                   (user.firstname, user.lastname, user.email, user.phone))
    conn.commit()
    return {"status": "success"}

@app.get("/users")
def get_users():
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    return [
        {"id": row[0], "firstname": row[1], "lastname": row[2], "email": row[3], "phone": row[4]}
        for row in rows
    ]
