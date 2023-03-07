from fastapi import APIRouter, Depends
from utils.auth import authBearer
from utils.encrypt import encode, verify
from schemas.users import User
from conections.sqlConnection import SQLDB
import json

users = APIRouter()

@users.get('/user', dependencies=[Depends(authBearer)], response_model=User)
async def getUser(email:str):
    consult = SQLDB().getOne('users','email',email)

    config = json.loads(User.schema_json())['properties']
    keys = list(config.keys())

    response = {}
    for n,i in enumerate(keys):
        response[i] = consult[n]

    return response

@users.post('/user', dependencies=[Depends(authBearer)])
async def postUser(user:User):
    data = (user.first_name, user.last_name, user.email, encode(user.password), user.is_admin, user.is_active, user.created_at, user.company_id)
    response = SQLDB().putOne('users', data)
    return response

@users.get('/user/verify', dependencies=[Depends(authBearer)])
async def getUser(email:str, password:str):
    consult = SQLDB().getOne('users','email',email)

    if consult != None:
        config = json.loads(User.schema_json())['properties']
        keys = list(config.keys())

        response = {}
        for n,i in enumerate(keys):
            response[i] = consult[n]

        response['correct_password'] = verify(response['password'],password)
    else:
        response = {
            'correct_password':False
        }
    
    print(response)
    return response