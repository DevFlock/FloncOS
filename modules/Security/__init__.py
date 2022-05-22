from fastapi import HTTPException, Security
from fastapi.security.api_key import APIKeyHeader

api_key_header = APIKeyHeader(name="X-API-KEY")

class Secure:
    def __init__(self, accepted_keys: list = []):
        self.accepted_keys = accepted_keys
        self.api_key_header = APIKeyHeader(name="X-API-KEY")

    def __call__(self, key: str = Security(api_key_header)):
        if key in self.accepted_keys:
            return key
        else:
            raise HTTPException(status_code=401, detail="Invalid API key")