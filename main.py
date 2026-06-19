from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from schema import CustomerInput, PredictionResponse
from model import predict_churn

app = FastAPI(title="Customer Churn Prediction API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {"message": "Customer Churn Prediction API Running"}


@app.post("/predict", response_model=PredictionResponse)
def predict(data: CustomerInput):
    prediction, message = predict_churn(
        data.age,
        data.monthly_charge
    )

    return PredictionResponse(
        prediction=prediction,
        message=message
    )