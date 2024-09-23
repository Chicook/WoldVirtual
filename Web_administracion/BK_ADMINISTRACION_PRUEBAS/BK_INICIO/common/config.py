# BK_INICIO/common/config.py

class Config:
    DEBUG = True
    SECRET_KEY = 'supersecretkey'
    DATABASE_URI = 'sqlite:///site.db'

def get_config():
    return Config
  
