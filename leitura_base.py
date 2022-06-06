
import pandas as pd
import datetime

def read_base():
    df = pd.read_csv("base/base_fixa.csv", sep = ";")
    base = df['DOCUMENTO'].unique()
    return base

def save_result(cnpj, contact, produtos):

    data_smart = {

            "CLIENTE" : cnpj,
            "NOME" : contact[0],
            "TELEFONE_CELULAR" : contact[1],
            "TELEFONE_COMERCIAL": contact[2],
            "EMAIL": contact[3],
            "ACEITA_SMS": contact[4],
            "CONTATO": contact[5],
            "TELEFONE_RESIDENCIAL": contact[6],
            "ACEITA_SMS" : contact[7],
            "PRODUTOS" : produtos,
            "CRIADO EM" : datetime.datetime.now(),

        }
    df = pd.DataFrame(data_smart, index = [0])
    df.to_csv("base/resultado_base.csv", mode = "a", index = False, header = False)