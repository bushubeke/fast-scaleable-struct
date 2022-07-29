import os
from pydantic import BaseSettings 

class Settings(BaseSettings):
    DATABASE_CMS_URI: str=os.getenv('DATABASE_CMS_URI') #bushumongoose
    DATABASE_CMSASYNC_URI: str=os.getenv("DATABASE_CMSASYNC_URI")
    DATABASE_MIGRATION_URI : str=os.getenv('DATABASE_MIGRATION_URI') #bushuuseradmin
    DATABASE_ASYNC_URI : str=os.getenv("DATABASE_ASYNC_URI")
    SECRET_KEY : str = os.getenv("SECRET_KEY")
    class Config:
        env_file = ".env"

settings = Settings()