from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class User(BaseModel):
    _id:Optional[int]
    first_name:str
    last_name:str
    email:str
    password:str
    is_active:Optional[bool] = True
    created_at:Optional[datetime] = datetime.now()
    company:str