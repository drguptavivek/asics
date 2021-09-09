from pydantic import BaseModel, ValidationError, validator, Field
from pydantic import NegativeInt, conint, conlist, constr, StrictInt, PositiveInt

from enum import Enum, IntEnum
from datetime import date, datetime, time, timedelta


class User(BaseModel):
    id: int
    name: str
    UHID: str
    

class AsicsOptions(IntEnum):
    Never = 1
    Sometimes = 2 
    Often = 3
    Always = 4  

class AsicsForm(BaseModel):
    q1:  AsicsOptions
    q2:  conint(gt=0, lt=5)
    q3:  conint(gt=0, lt=5)
    q4:  conint(gt=0, lt=5)
    q5:  conint(gt=0, lt=5)
    q6:  conint(gt=0, lt=5)
    q7:  conint(gt=0, lt=5)
    q8:  conint(gt=0, lt=5)
    q9:  conint(gt=0, lt=5)
    q10: conint(gt=0, lt=5)
    q11: conint(gt=0, lt=5)
    q12: conint(gt=0, lt=5)
    q13: conint(gt=0, lt=5)
    q14: conint(gt=0, lt=5)
    q15: conint(gt=0, lt=5)
    q16: conint(gt=0, lt=5)
    q17: conint(gt=0, lt=5)
    q18: conint(gt=0, lt=5)
    q19: conint(gt=0, lt=5)
    q20: conint(gt=0, lt=5)
    q21: conint(gt=0, lt=5)
    q22: conint(gt=0, lt=5)
    q23: conint(gt=0, lt=5)
    q24: conint(gt=0, lt=5)
    q25: conint(gt=0, lt=5)
    q26: conint(gt=0, lt=5)
    q27: conint(gt=0, lt=5)
    q28: conint(gt=0, lt=5)
    q29: conint(gt=0, lt=5)
    q30: constr(regex=r'^[1-4]$')
    username: str
    time_submit: datetime

    @validator('username')
    def username_alphanumeric(cls, v):
        assert v.isalnum(), 'must be alphanumeric'
        return v
