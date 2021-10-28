
from typing import List
from fastapi import FastAPI
from fastapi.params import Depends
from starlette.responses import RedirectResponse
from . import models,schemas,crud
from .database import SessionLocal,engine
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.get("/")
def main():
    return RedirectResponse(url="/docs/")


@app.get("/v1/",response_model=List[schemas.News])
def showNews(from_:str , to_: str ,category: str,db:Session=Depends(get_db)):
    noticias = crud.get_news(db, from_=from_,to_=to_, category=category)
    return noticias

