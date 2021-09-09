from pydantic import BaseModel, ValidationError, validator

from datetime import date, datetime, time, timedelta


class User(BaseModel):
    id: int
    name: str
    UHID: str
    

class AsicsForm(BaseModel):
    q1: int
    q2: int
    q3: int
    q4: int
    q5: int
    q6: int
    q7: int
    q8: int
    q9: int
    q10: int
    q11: int
    q12: int
    q13: int
    q14: int
    q15: int
    q16: int
    q17: int
    q18: int
    q19: int
    q20: int
    q21: int
    q22: int
    q23: int
    q24: int
    q25: int
    q26: int
    q27: int
    q28: int
    q29: int
    q30: int
    username: str
    time_submit: datetime

    @validator('username')
    def username_alphanumeric(cls, v):
        assert v.isalnum(), 'must be alphanumeric'
        return v