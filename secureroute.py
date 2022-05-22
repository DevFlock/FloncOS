from fastapi import APIRouter, Security
import secure

router = APIRouter(
    prefix="/secure",
    tags=["secure"]
)

@router.get("/", summary="Secure endpoint")
def read_secure(api_key: str = Security(secure.get_api_key)):
    response = api_key + " is a valid API key."
    return response