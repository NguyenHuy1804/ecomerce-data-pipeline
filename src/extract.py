import pandas as pd

def extract():
    df = pd.read_csv("data/raw/online_retail.csv", encoding="ISO-8859-1")
    return df
