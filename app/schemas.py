from pydantic import BaseModel, validator
import re

class User(BaseModel):
    username: str
    password: str

    @validator('username')
    def validate_username(cls, value):
        if re.match('ˆ([a-z]|[0-9]|@)+$', value):
            raise ValueError('Username format invalid')
        return value
