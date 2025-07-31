import os
from datetime import timedelta

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'clave_super_segura_para_flask'  
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY') or 'clave_super_segura_para_jwt'  
    
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)
    #JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=1)
    
    
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost/api_messages_seti'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    
   
