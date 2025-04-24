from pydantic import BaseModel
from typing import Optional

class LabResult(BaseModel):
    test_name: str
    value: float
    unit: Optional[str]
    normal_min: float
    normal_max: float
    status: str
    explanation: Optional[str] = None
