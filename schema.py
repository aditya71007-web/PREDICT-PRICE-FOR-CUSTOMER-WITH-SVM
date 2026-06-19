from pydantic import BaseModel


class CustomerInput(BaseModel):
    age: int
    monthly_charge: float


class PredictionResponse(BaseModel):
    prediction: int
    message: str