from fastapi import APIRouter, HTTPException, status

from constants import UserExistsException, CredentialsException
from services import UserServiceDep, AuthServiceDep
from dependencies import PasswordRequestFormDep
from dto import RegisterInfo, User, Token

router = APIRouter()


@router.post("/login")
async def login(form_data: PasswordRequestFormDep, authentication_service: AuthServiceDep) -> Token:
    try:
        access, refresh = authentication_service.authenticate_user(form_data.username, form_data.password)
        return Token(access_token=access, refresh_token=refresh, token_type="bearer")
    except CredentialsException:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"})


@router.post("/register")
async def register(register_data: RegisterInfo, user_service: UserServiceDep) -> User:
    try:
        user = user_service.create_new_user(register_data.username, register_data.password, register_data.email)
        return user
    except UserExistsException as e:
        raise HTTPException(status_code=400, detail="User already exists")
