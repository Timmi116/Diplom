from fastapi import APIRouter, Depends, Form, File, UploadFile, HTTPException
from starlette.requests import Request
from starlette.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from .models import User
from .database import get_db
from datetime import datetime

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/register/")
async def register_get(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})

@router.post("/register/")
async def register_post(
    request: Request,
    username: str = Form(None, label="Имя пользователя"),
    age: int = Form(None, label="Возраст"),
    gender: str = Form(None, label="Пол"),
    email: str = Form(None, label="Электронная почта"),
    password: str = Form(None, label="Пароль"),
    db = Depends(get_db)
):
    user = User(username=username, age=age, gender=gender, email=email, password=password)
    db.add(user)
    db.commit()

    response = RedirectResponse(url="/profile/", status_code=303)
    response.set_cookie(key="email", value=email)  # Устанавливаем куки с электронной почтой пользователя
    return response

@router.get("/profile/")
async def profile_get(request: Request):
    return templates.TemplateResponse("profile.html", {"request": request})

@router.post("/profile/")
async def profile_post(
    request: Request,
    date_of_birth: str = Form(None, label="Дата рождения"),
    place_of_birth: str = Form(None, label="Место рождения"),
    address: str = Form(None, label="Адрес проживания"),
    biography: str = Form(None, label="Биография"),
    db = Depends(get_db)
):
    user = db.query(User).filter_by(email=request.cookies["email"]).first()
    
    user.date_of_birth = datetime.strptime(date_of_birth, "%Y-%m-%d").date()
    user.place_of_birth = place_of_birth
    user.address = address
    user.biography = biography
    db.commit()

    response = RedirectResponse(url="/upload_photo/", status_code=303)
    response.set_cookie(key="email", value=request.cookies["email"])  # Устанавливаем куки с электронной почтой пользователя
    return response

@router.get("/upload_photo/")
async def upload_photo_get(request: Request):
    return templates.TemplateResponse("upload_photo.html", {"request": request})

@router.post("/upload_photo/")
async def upload_photo_post(
    request: Request,
    file: UploadFile = File(None, label="Фотография"),
    db = Depends(get_db)
):
    contents = await file.read()
    user = db.query(User).filter_by(email=request.cookies["email"]).first()
    user.profile_picture = contents
    db.commit()
    return RedirectResponse(url="/congratulations/", status_code=303)

@router.get("/congratulations/")
async def congratulations_get(request: Request):
    return templates.TemplateResponse("congratulations.html", {"request": request})
