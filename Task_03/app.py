from fastapi import FastAPI
import joblib
import uvicorn  # 1. Add this import

app = FastAPI()

# This is where the error happened - make sure model.pkl exists first!
model = joblib.load('model.pkl')

@app.get("/")
def home():
    return {"Status": "API is Running"}

@app.get("/predict")
def predict(sqft: int, beds: int):
    # Using float() ensures the web app can read the number
    prediction = model.predict([[sqft, beds]])
    return {"Estimated Price": float(prediction[0])}

# 2. Add this "Protection Block" at the very bottom
if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
