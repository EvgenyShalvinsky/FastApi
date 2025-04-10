from pydantic import BaseModel

class SecretCreate(BaseModel):
    secret: str
    passphrase: str = None
    ttl_seconds: int = 300

class SecretResponse(BaseModel):
    secret_key: str

class SecretRead(BaseModel):
    secret: str
