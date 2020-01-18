import os
from dotenv import load_dotenv
load_dotenv

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    
class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class DevConfig(Config):
    # pass
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://faith:456789@localhost/phones'
    
    DEBUG = True
    
config_options = {
    'development':DevConfig,
    'production':ProdConfig
}
    