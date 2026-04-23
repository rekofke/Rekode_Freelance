import os
from dotenv import load_dotenv


load_dotenv()

class Config:
    SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'dev-secret')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///Rekode_Freelance.db')
    SQLALCHEMY_TRACK_MODIFICATIOND = False
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'dev-jwt secret')