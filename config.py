import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql' + os.getenv('DATABASE_URL')[7]
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = False