from datetime import datetime, timedelta
from db.models import UserModel
from decouple import config
from fastapi import status
from fastapi.exceptions import HTTPException
from jose import JWSError, jwt, ExpiredSignatureError
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from schemas import User

crypt_context = CryptContext(schemes=['sha256_crypt'])
SECRET_KEY = config('SECRET_KEY')
ALGORITHM = config('ALGORITHM')

class UserUseCases:

    def __init__(self, db_session: Session) -> None:
        self.db_session = db_session

    def user_register(self, user: User):
        user_model = UserModel(
            username=user.username,
            password= crypt_context.hash(user.password)
        )
        try:
            self.db_session.add(user_model)
            self.db_session.commit()
        except IntegrityError:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='User already exists'
            )

    def user_login(self, user: User, expires_in:int = 30):

        user_on_db = self.db_session.query(UserModel).filter_by(username=user.username).first()

        if user_on_db is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="User or Password invalid")

        if not crypt_context.verify(user.password, user_on_db.password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="User or Password invalid")

        # sempre msm timezone, now() pega o timezone local
        exp = datetime.utcnow() + timedelta(minutes=expires_in)

        payload = {
            'sub': user.username,
            'exp': exp
        }

        access_token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
        # quando passamos um datetime no objeto precisamos transfomá-lo em string
        return {
            'access_token': access_token,
            'exp': exp.isoformat()
        }

    def verify_token(self, access_token):

        try:
            # decodifica o token, retornando meu payload gerado na funcao de login
            data = jwt.decode(access_token, SECRET_KEY, algorithms=[ALGORITHM])
        except JWSError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token")
        except ExpiredSignatureError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token Expired!")

        user_on_db = self.db_session.query(UserModel).filter_by(username=data['sub']).first()

        if user_on_db is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token")
