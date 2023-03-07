from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Company(BaseModel):
    id:Optional[str]
    name:str
    is_active:bool
    created_at:datetime