from typing import List
from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from .. import crud, schemas
from ..dependencies import get_db

router = APIRouter(
    prefix="/posts",
    tags=['Posts']
    )


@router.get("/posts", response_model=List[schemas.Post])
def read_posts(db: Session = Depends(get_db)):
    print('here we are')
    posts = crud.get_posts(db)
    return posts