from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import joblib
from pathlib import Path

# Create FastAPI app
app = FastAPI()

# HTML templates folder
templates = Jinja2Templates(directory="templates")

# Load trained model
MODEL_FILE = Path("models/knn_model.joblib")

artifact = joblib.load(MODEL_FILE)
model = artifact["model"]
feature_names = artifact["feature_names"]


# Input structure
class IrisInput(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float


# Home route → loads HTML page
@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )


# Prediction route
@app.post("/flower")
def predict(data: IrisInput):

    X = [[
        data.sepal_length,
        data.sepal_width,
        data.petal_length,
        data.petal_width
    ]]

    prediction = model.predict(X)[0]

    return {
        "prediction": prediction
    }