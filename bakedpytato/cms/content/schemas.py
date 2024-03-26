import pydantic
from typing import List, Dict, Union


class DOMTagV1(pydantic.BaseModel):
    version: int = 1
    id: str
    cls: List[str]
    content: str = None
