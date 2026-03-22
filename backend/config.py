import os

class Config:
    SECRET_KEY = 'your-secret-key-here'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///backend/users.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
