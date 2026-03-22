import os

class Config:
    SECRET_KEY = 'your-secret-key-here'
    # 使用 SQLAlchemy 的标准格式
    SQLALCHEMY_DATABASE_URI = 'sqlite:///users.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False