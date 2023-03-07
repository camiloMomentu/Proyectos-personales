from fastapi import APIRouter, Depends
from utils.auth import authBearer
from config import Mongo
from schemas.users import User
from utils.encrypt import encode, verify

users = APIRouter()

@users.get('/user', dependencies=[Depends(authBearer)], response_model_exclude_defaults=User)
async def getUser(email:str, password:str):
    data = Mongo.getOne('users',{'email':email})
    if data != None:
        verifycation = verify(data['password'],password)
        data['correct_password'] = verifycation

        if verifycation:
            return data
        else:
            return {'correct_password':False}
    else:
        return {'error':'No data'}

@users.post('/user', dependencies=[Depends(authBearer)])
async def postUser(user:User):
    print(user)
    user_info = {i[0]:i[1] for i in user}
    user_info['password'] = encode(user_info['password'])
    set = Mongo.setOne('users', user_info)

    response = {
        "status":200 if type(set) == str else 404,
        "id":set
    }

    return response