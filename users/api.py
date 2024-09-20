from models.models_for_db import *
from fastapi import Depends,Body,APIRouter
from fastapi.responses import JSONResponse

router_u=APIRouter()

@router_u.get("/{id}")
def get_user(id, db: Session = Depends(get_db)):
    print('dfgsdfgsdf')
    # получаем пользователя по id
    user = db.query(User).filter(User.id == id).first()
    # если не найден, отправляем статусный код и сообщение об ошибке
    if user == None:
        return JSONResponse(status_code=404, content={"message": "User is not found"})
    # если пользователь найден, отправляем его
    return user

@router_u.post("/")
def create_user(data=Body(), db: Session = Depends(get_db)):
    user = User(name=data["name"], phone=data["phone"])
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@router_u.put("/")
def edit_user(data=Body(), db: Session = Depends(get_db)):
    # получаем пользователя по id
    user = db.query(User).filter(User.id == data["id"]).first()
    # если не найден, отправляем статусный код и сообщение об ошибке
    if user == None:
        return JSONResponse(status_code=404, content={"message": "User is not found"})
    # если пользователь найден, изменяем его данные и отправляем обратно клиенту
    user.phone = data["phone"]
    user.name = data["name"]
    db.commit()  # сохраняем изменения
    db.refresh(user)
    return user


@router_u.delete("/{id}")
def delete_user(id, db: Session = Depends(get_db)):
    # получаем пользователя по id
    user = db.query(User).filter(User.id == id).first()
    # если не найден, отправляем статусный код и сообщение об ошибке
    if user == None:
        return JSONResponse(status_code=404, content={"message":  "User is not found"})
    # если пользователь найден, удаляем его
    db.delete(user)  # удаляем объект
    db.commit()  # сохраняем изменения
    return user