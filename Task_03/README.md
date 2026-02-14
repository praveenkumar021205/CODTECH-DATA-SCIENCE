# Task 3: House Price Prediction API

*Domain:* Data Science / Web Development  
*Technique:* Linear Regression & API Deployment  
*Tools:* FastAPI, Scikit-Learn, Pandas  

## Description
This project implements a machine learning model to predict house prices based on square footage and the number of bedrooms. The model is deployed as a REST API using *FastAPI*, allowing users to get real-time price estimates.

## The Problem
Real estate pricing can be complex. This project aims to build a simple tool that provides instant price estimations based on key features (Size and Bedroom count) using historical data.

## Workflow
1.  *Data:* A dataset (data.csv) containing housing features.
2.  *Training:* A Linear Regression model is trained using train_model.py and saved as model.pkl.
3.  *Deployment:* A FastAPI application (main.py) loads the model and serves predictions via a /predict endpoint.

## How to Run
1.  Install dependencies: pip install -r requirements.txt
2.  Train the model: python train_model.py
3.  Start the API: uvicorn main:app --reload
4.  Test via browser: http://127.0.0.1:8000/predict?sqft=2000&beds=3
