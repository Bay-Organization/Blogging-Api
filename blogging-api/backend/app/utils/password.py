from passlib.context import CryptContext

#Create a context for password hashing using bcrypt algorithm
pwd_context = CryptContext(schemes=["bcrypt"],deprecated="auto")

def hash_password(password: str):
    #Hashes password using bcrypt algorithm
    return pwd_context.hash([password])

def verify_password(plain_password: str, hashed_password: str):
    #Verifies whether plain and hashed password matches
    return pwd_context.verify(plain_password,hashed_password)

