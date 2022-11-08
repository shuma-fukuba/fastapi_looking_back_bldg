from pydantic import BaseModel


class CreateTokenSchema(BaseModel):
    username: str
    password: str
