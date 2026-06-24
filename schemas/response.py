from pydantic import BaseModel
from typing import Optional, Generic, TypeVar
from datetime import datetime

T = TypeVar("T")

class APIResponse(BaseModel, Generic[T]):
    status: bool
    timestamp: str
    message: str
    data: Optional[T] = None

    @classmethod
    def success(cls, data: T = None, message: str = "Success"):
        return cls(
            status=True,
            timestamp=str(datetime.now()),
            message=message,
            data=data
        )

    @classmethod
    def error(cls, message: str = "Something went wrong"):
        return cls(
            status=False,
            timestamp=str(datetime.now()),
            message=message,
            data=None
        )