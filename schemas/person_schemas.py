from pydantic import BaseModel,Field

from pydantic import BaseModel
from schemas.compani_schemas import Company

class Person(BaseModel):
    name: str =Field(default="Undefined",min_length=3,max_lendth=20)

    company:Company