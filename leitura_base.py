
import pandas as pd
import datetime

def read_base():
    df = pd.read_csv("base/MAILING_FIXA_GABRIELA.csv", sep = ";", on_bad_lines='skip')
    base = df['DOCUMENTO'].unique()
    return base
