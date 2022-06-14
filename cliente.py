import datetime
from csv import writer

class Clientes:
    
    
    def __init__(self, cnpj, name , celular, telefone_comercial , email , produto, data_de_ativacao ) :

        self.cnpj = cnpj
        self.name = name
        self.celular = celular
        self .telefone_comercial = telefone_comercial
        self.email = email
        self.produto = produto
        self.data_de_ativacao = data_de_ativacao
        self.produtos = {
            "produto" : [],
            "data_de_ativacao" : [],
            "ultima oferta":[],
            "recomendacao":[]
        }
    
    def __str__(self):
        return f'{self.cnpj}, {self.name}, {self.celular}, {self.telefone_comercial}, {self.email}, {self.produtos}, {self.produtos["recomendacao"]}'
    
    def add_produto(self):
        self.produtos["produto"].append(self.produto)
        self.produtos["data_de_ativacao"].append(self.data_de_ativacao)

    def recomendacao(self):
        
        hoje = datetime.datetime.now()

        for data in self.produtos['data_de_ativacao']:
            ativacao = datetime.datetime.strptime(data, "%d/%m/%Y %H:%M:%S")
            
            print(ativacao)

            num_months = (hoje.year - ativacao.year) * 12 + (hoje.month - ativacao.month)

            if num_months >16:
                self.produtos["recomendacao"].append("sim")
            else:
                self.produtos["recomendacao"].append("não")

    def append_csv(self): 
        try:
            list_data=[f'{self.cnpj}', f'{self.name}', f'{self.celular}', f'{self.telefone_comercial}', f'{self.email}', f'{self.produtos["produto"]}', f'{self.produtos["recomendacao"]}']

            with open('resultado/mailing_fixa_gabriela_smart.csv', 'a+', newline='',) as f_object:  
                writer_object = writer(f_object)
                writer_object.writerow(list_data)  
                f_object.close()
        
        except Exception as e:
            print(e)




        
        

    

    

