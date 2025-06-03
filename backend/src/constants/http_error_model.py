from pydantic import BaseModel


class HttpErrorModel(BaseModel):
    detail: str

    model_config = {
            "example": {"detail": "HTTPException raised."},
        }
