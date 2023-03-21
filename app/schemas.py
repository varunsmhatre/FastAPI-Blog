from typing import List, Union
from pydantic import BaseModel


class PostBase(BaseModel):
    title: str
    content: Union[str, None] = None


class PostCreate(PostBase):
    pass


class Post(PostBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    username: str
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    items: List[Post] = []

    class Config:
        orm_mode = True