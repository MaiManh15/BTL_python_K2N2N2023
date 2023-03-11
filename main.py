from fastapi import FastAPI
import numpy as np
import pandas as pd

app = FastAPI()

@app.get('/')
def home():
    return "welcome home"