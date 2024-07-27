from fastapi import FastAPI, HTTPException, Header
import pandas as pd

app = FastAPI()

data = pd.read_csv("data_no_outlier.csv")
data = data.to_dict()

@app.get("/")
def root():
    return data

