from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from cliente import Clientes
import time
import leitura_base

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
wait = WebDriverWait(driver,5)
wait_quickly = WebDriverWait(driver,5)

def open_smart():
    driver.get("https://vivovendas.vivo.com.br/sales_ext/start.swe")

def login_smart(user = '', password = ''):

    user = '80836247'
    password = 'Grog@34av'

    user_login = wait.until(EC.presence_of_element_located((By.ID, 'username')))
    user_password = wait.until(EC.presence_of_element_located((By.ID, 'password')))

    user_login.send_keys(user)
    user_password.send_keys(password)

    input("Aperte ENTER após o login e tela de carregamento concluído \n")

def enter_venda():
    try:
        venda = wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(@title, 'Venda')]")))
        venda.click()
    except Exception as e:
        print(e)

def client_venda(doc):
    try:
        documento = wait.until(EC.presence_of_element_located((By.NAME,"s_1_1_11_0")))
        documento.send_keys(str(doc) + Keys.ENTER)
    except Exception as e:
        print(e)

def get_products():

    tr = True
    i = 1
    produtos = []
    
    while tr:
    
        try:
            product_name_path = f'//*[@id="{i}_s_4_l_Product_Name"]/span'
            install_date_path = f'//*[@id="{i}_s_4_l_Install_Date"]'
            product_name = wait_quickly.until(EC.presence_of_element_located((By.XPATH, product_name_path)))
            install_date = wait_quickly.until(EC.presence_of_element_located((By.XPATH,  install_date_path)))
            i += 1
            produtos.append(product_name.text)
            produtos.append(install_date.text)
            print(f'produtos {produtos}')
            
        except Exception as e:
            print(e)
            tr = False
            print('saiu do get_products')

    return produtos     
    
    

    
    

def extract_contact():


    telefone_celular_path = wait.until(EC.presence_of_element_located((By.NAME, "s_1_1_63_0")))
    nome_path = wait.until(EC.presence_of_element_located((By.NAME,"s_1_1_47_0")))
    telefone_comercial_path = wait.until(EC.presence_of_element_located((By.NAME, "s_1_1_62_0")))
    email_path = wait.until(EC.presence_of_element_located((By.NAME, "s_1_1_70_0")))
    sms_path = wait.until(EC.presence_of_element_located((By.NAME,"s_1_1_71_0")))
    contato_path = wait.until(EC.presence_of_element_located((By.NAME,"s_1_1_61_0")))
    telefone_residencial_path =wait.until(EC.presence_of_element_located((By.NAME, "s_1_1_65_0")))
    aceita_email_path = wait.until(EC.presence_of_element_located((By.NAME, "s_1_1_6_0")))

    nome = nome_path.get_attribute("value")
    telefone_celular = telefone_celular_path.get_attribute("value")
    telefone_comercial = telefone_comercial_path.get_attribute("value")
    email = email_path.get_attribute("value")
    sms = sms_path.get_attribute("value")
    contato = contato_path.get_attribute("value")
    telefone_residencial= telefone_residencial_path.get_attribute("value")
    aceita_email = aceita_email_path.get_attribute("value")

    contacts = [nome, telefone_celular, telefone_comercial, email]

    return contacts


def rentabilizar():
    try:
        rentabilizar = wait.until(EC.presence_of_element_located((By.ID, "s_1_1_10_0_Ctrl")))
        rentabilizar.click()
    except Exception as e:
        print(e)

def justificativa():

    try:
        justificativa = wait.until(EC.presence_of_element_located((By.NAME, "s_3_1_2_0")))
        justificativa.send_keys("Endereço FWT" + Keys.ENTER)   
        
        justificativa.send_keys(Keys.ENTER)
        
        botao_salvar = wait.until(EC.presence_of_element_located((By.NAME, "s_3_1_3_0")))
        botao_salvar.click()
    except Exception as e:
        print(e)

def get_data(doc):

    try:
        enter_venda() 
        client_venda(str(doc).zfill(14))
        produtos = get_products()
        rentabilizar()
        contact = extract_contact()
        justificativa()
        print(contact, produtos)
        """leitura_base.save_result(str(doc).zfill(14), contact, produtos)"""
        print('terminou aqui')
        cliente = Clientes(doc,contact[0],contact[1],contact[2],contact[3], produtos[0],produtos[1])
        cliente.add_produto()
        cliente.recomendacao()
        print(cliente)
        cliente.append_csv()

    except Exception as e:
        print(e)
        print("exceção")

    finally:
        print('finally')
        enter_venda()
        
        






