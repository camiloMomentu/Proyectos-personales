from fastapi import HTTPException, status, Security
from fastapi.security import HTTPBearer
from config import SECRET_KEY

def authBearer(api_key:str = Security(HTTPBearer())):
    if api_key.credentials != SECRET_KEY:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Forbidden / Unauthorized"
        )