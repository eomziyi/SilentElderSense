from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password_hash = Column(String(128), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    def set_password(self, password):
        """密码加密"""
        import hashlib
        self.password_hash = hashlib.sha256(password.encode()).hexdigest()

    def check_password(self, password):
        """验证密码"""
        import hashlib
        return self.password_hash == hashlib.sha256(password.encode()).hexdigest()


# 数据库引擎和会话
engine = None
SessionLocal = None


def init_db(app):
    global engine, SessionLocal
    database_url = app.config['SQLALCHEMY_DATABASE_URI']
    engine = create_engine(database_url, echo=True)
    SessionLocal = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()