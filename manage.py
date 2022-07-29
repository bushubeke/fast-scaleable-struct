from ast import Try
from typing import Callable
import typer
import asyncio
import subprocess
from main.main import create_dev_app
from useradmin.models import async_main as userData,droptables as userDrop
from simplecms.models.dbconnect import async_main as cmsData,droptables as cmsDrop
    
    
capp = typer.Typer()
app=create_dev_app()

@capp.command()
def rung():
    """starts gunicorn server of the app with uvicorn works bound  to 0.0.0.0:9000 with one worker
    """
    subprocess.run(["gunicorn", "manage:app", "-k" ,"uvicorn.workers.UvicornWorker","-b" ,"0.0.0.0:9000","--reload","-w","1"]) 

@capp.command()
def upgrade():
    """creates  base models based on their methadata"""
    asyncio.run(userData())
    asyncio.run(cmsData())

@capp.command()
def drop():
    """drops all tables created from provided database"""
    asyncio.run(userDrop())
    asyncio.run(cmsDrop())

@capp.command()
def test(location):
    """
      Takes location of test locations as arguments. this argument is required    
    """
    subprocess.run(["pytest", location,"--asyncio-mode=strict"])
    

if __name__ == "__main__":
    capp()  