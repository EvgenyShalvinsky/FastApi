#Импорт библиотек
from fastapi import FastAPI, HTTPException, Depends, Request
from sqlalchemy.orm import Session
import models
import schemas
import crud
from database import SessionLocal, engine
#Запуск
app = FastAPI()
#Создание таблиц
models.Base.metadata.create_all(bind=engine)
#Создание сессии
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/secret", response_model=schemas.SecretResponse)
def create_secret(secret: schemas.SecretCreate, request: Request, db: Session = Depends(get_db)):
    ip_address = request.client.host
    db_secret = crud.create_secret(db, secret, ip_address)
    return {"secret_key": db_secret.secret_key}

@app.get("/secret/{secret_key}", response_model=schemas.SecretRead)
def read_secret(secret_key: str, db: Session = Depends(get_db)):
    db_secret = crud.get_secret(db, secret_key)
    if db_secret is None:
        raise HTTPException(status_code=404, detail="Secret not found")
    # Логика для удаления или недоступности секрета после первого получения
    return {"secret": db_secret.secret}

@app.delete("/secret/{secret_key}")
def delete_secret(secret_key: str, db: Session = Depends(get_db)):
    crud.delete_secret(db, secret_key)
    return {"status": "secret_deleted"}
