import pandas as pd
import datetime

def read_base():
    df = pd.read_csv("base/base_fixa.csv", sep = ";")
    base = df['DOCUMENTO'].unique()
    return df, base

def save_result(df, nome, telefone_celular, telefone_comercial, email, sms, contato, telefone_residencial, aceita_email):

    data_smart = {

            "CLIENTE" : df["DOCUMENTO"],
            "NOME" : nome,
            "TELEFONE_CELULAR" : telefone_celular,
            "TELEFONE_COMERCIAL": telefone_comercial,
            "EMAIL": email,
            "ACEITA_SMS": sms,
            "CONTATO": contato,
            "TELEFONE_RESIDENCIAL": telefone_residencial,
            "ACEITA_SMS" : aceita_email,
            "CRIADO EM" : datetime.datetime.now(),

        }
        
    df = pd.DataFrame(data_smart)
    df.to_csv("base/resultado_base.csv", mode = "a", index=False)