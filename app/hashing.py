from passlib.context import CryptContext

password_ctx = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Hash():
    def bcrypt(password:str)->str:
        return password_ctx.hash(password)

    def verify(password, hashed_password)->bool:
        return password_ctx.verify(password, hashed_password)