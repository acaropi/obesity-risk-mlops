from fastapi import FastAPI
from pydantic import BaseModel, Field
import joblib
import pandas as pd

# Inicialización de FastAPI
app = FastAPI(
    title="API de Predicción de Riesgo de Obesidad",
    description="Microservicio MLOps para estimar el riesgo de obesidad basado en hábitos y condición física.",
    version="1.0.0"
)

# Esquema de entrada
class UserFeatures(BaseModel):
    Gender: str = Field(..., example="Female")
    Age: float = Field(..., example=21.0)
    Height: float = Field(..., example=1.62)
    Weight: float = Field(..., example=64.0)
    Family_history_overweight: str = Field(..., example="yes")
    Frequent_high_caloric_food: str = Field(..., example="no")
    Frequent_consumption_vegetables: float = Field(..., example=2.0)
    Number_of_main_meals: float = Field(..., example=3.0)
    Food_between_meals: str = Field(..., example="Sometimes")
    Smoke: str = Field(..., example="no")
    Daily_Water_Intake: float = Field(..., example=2.0)
    Calorie_Monitoring: str = Field(..., example="no")
    Physical_Activity_Frequency: float = Field(..., example=0.0)
    Technology_Use_Time: float = Field(..., example=1.0)
    Alcohol_Consumption: str = Field(..., example="no")
    Transportation_type: str = Field(..., example="Public_Transportation")


# Endpoint de estado
@app.get("/")
def health_check():
    return {
        "status": "ok",
        "message": "API de Riesgo de Obesidad activa y lista para recibir solicitudes."
    }


# Endpoint de predicción
@app.post("/predict")
def predict_risk(data: UserFeatures):

    model_pipeline = joblib.load("model_pipeline.pkl")

    input_data = pd.DataFrame([data.dict()])

    prediction = model_pipeline.predict(input_data)[0]

    probability = model_pipeline.predict_proba(input_data)[0][1]

    return {
        "riesgo_obesidad_predicho": int(prediction),
        "probabilidad_riesgo": float(round(probability, 4)),
        "interpretacion":
            "Presenta Riesgo de Obesidad"
            if prediction == 1
            else "No presenta Riesgo de Obesidad"
    }
