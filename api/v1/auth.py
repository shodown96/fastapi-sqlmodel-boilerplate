from datetime import timedelta
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from models.user import Token, User, UserCreate
from boilerplate.core.config import settings
from starlette.exceptions import HTTPException
from utils.auth import authenticate_user, create_access_token, get_password_hash

from core.db import SessionDep

router = APIRouter()


@router.post("/sign-in", response_model=Token)
async def login_for_access_token(
    session: SessionDep,
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
) -> Token:
    user = authenticate_user(session, form_data.email, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.id}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")


@router.post("/sign-up", response_model=User)
def create_hero(user: UserCreate, session: SessionDep):
    db_user = User.model_validate(
        {
            **user.model_dump(exclude="password"),
            "password": get_password_hash(user.password),
        }
    )
    print("db_user", db_user)
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user
    # return None
