import datetime
date = '6/2/2022 19:43:11'
hoje = datetime.datetime.now()

produto = {
    "produtos" : ['Vivo Internet Solo Empresas', 'Banda Larga Avulsa L Empresas Oferta',  'Ilimitado Brasil Empresas Especial Oferta - Duplo Acesso A'],
    "data_de_ativacao" : ['29/7/2021 06:31:58', '12/12/2019 11:46:55','23/3/2019 00:00:00'  ]
}
for data in produto['data_de_ativacao']:
    ativacao = datetime.datetime.strptime(data, "%d/%m/%Y %H:%M:%S")
    
    print(ativacao)

    num_months = (hoje.year - ativacao.year) * 12 + (hoje.month - ativacao.month)

    if num_months >16:
        print("tem recomendação")
    else:
        print("não tem recomendação")
