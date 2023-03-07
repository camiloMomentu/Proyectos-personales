from fastapi import APIRouter, Depends
from utils.auth import authBearer
from schemas.companies import Company

companies = APIRouter()

@companies.get('/company', dependencies=[Depends(authBearer)], response_model=Company)
async def getUser():
    return 'get Company'

@companies.post('/company', dependencies=[Depends(authBearer)])
async def postUser(company:Company):
    return company