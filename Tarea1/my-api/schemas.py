from typing import List, Optional
from datetime import datetime, date

from pydantic import BaseModel

class News(BaseModel):
    id:int
    title:str
    url:str
    date: date
    media_outlet:str
    category:str

    class Config:
        orm_mode = True


