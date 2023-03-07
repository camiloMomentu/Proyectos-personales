from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class User(BaseModel):
    id:Optional[int]
    first_name:str
    last_name:str
    email:str
    password:str
    is_admin:Optional[bool] = True
    is_active:Optional[bool] = True
    created_at:Optional[datetime] = datetime.now()
    company_id:int