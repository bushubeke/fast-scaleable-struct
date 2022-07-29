import jwt
from fastapi import FastAPI,Depends,HTTPException
from fastapi.middleware.cors import CORSMiddleware
from useradmin.approutes import apirouter as userrouter,get_current_active_user
from simplecms.models.dbmodels import TestingDataTypes,TestingTableModel,TestingTablePostModel
from simplecms.approutes import apirouter as cmsrouter
from json import  dumps as jsondumps,JSONDecoder
from fastapi.security import OAuth2PasswordBearer
from curd.sqlcurd import SQLAlchemyCURD
from simplecms.models.dbconnect import asyncengine as cmsasync
from config import settings

sqlcurd= SQLAlchemyCURD()


def create_dev_app():
    app=FastAPI(title="Development User Admin App")
    origins = [ "*"]
    app.add_middleware(
            CORSMiddleware,
            allow_origins=origins,
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
            )
        
    sqlcurd.init_app(app,cmsasync)
    sqlcurd.set_current_user(get_current_active_user)


    app.include_router(userrouter,prefix="/admin")
    app.include_router(cmsrouter,prefix="/cms")
    modlist=[[TestingDataTypes,TestingTableModel,TestingTablePostModel]]  
    sqlcurd.add_curd(modlist)
    sqlcurd.include_apirouter(prefix="/cmscurd")
    @app.get("/")
    def index():
        return {"Message":"You should make your own index page"}
    return app

def create_testing_app():
    app=FastAPI()   
    origins = [ "*"]
    app.add_middleware(
            CORSMiddleware,
            allow_origins=origins,
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
            )
    app.include_router(userrouter,prefix="/admin")
    app.include_router(cmsrouter,prefix="/cms")
    
    @app.get("/")
    def index():
        return {"Message":"You should make your own index page"}
    return app
