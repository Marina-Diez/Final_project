import pandas as pd
from src.config import collection

def carga_data():
    data = pd.read_csv("output/data_modelo_def.csv")
    return data




 