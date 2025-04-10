from sqlalchemy.orm import Session
import models
import schemas
from security import encrypt_secret


def create_secret(db: Session, secret: schemas.SecretCreate, ip_address: str):
    encrypted_secret = encrypt_secret(secret.secret)
    db_secret = models.Secret(
        secret_key=encrypted_secret['key'],
        secret=encrypted_secret['value'],
        ttl_seconds=secret.ttl_seconds,
        ip_address=ip_address
    )
    db.add(db_secret)
    db.commit()
    db.refresh(db_secret)
    return db_secret


def get_secret(db: Session, secret_key: str):
    return db.query(models.Secret).filter(models.Secret.secret_key == secret_key).first()

def delete_secret(db: Session, secret_key: str):
    secret = db.query(models.Secret).filter(models.Secret.secret_key == secret_key).first()
    if secret:
        db.delete(secret)
        db.commit()
