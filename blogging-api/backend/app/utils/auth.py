from datetime import datetime, timedelta 
from jose import jwt

SECRET_KEY = "supersecretkey123"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_TIME = 60

def create_access_token(data: dict, expires_minutes: int = ACCESS_TOKEN_EXPIRE_TIME):
    #Creates an access token with defined number of minutes
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=expires_minutes)
    to_encode.update({"exp": expire}) #Expiration time of the token 
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt