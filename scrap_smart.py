from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import login_smart
import leitura_base

def  wait_time():
    time.sleep(3)

driver = login_smart.driver
base = leitura_base.read_base()

def extract_client_data():   

    for doc in range(len(base)):

        try:    
            time.sleep(2)
            
            venda = driver.find_element(by=By.XPATH, value="//span[contains(@title, 'Venda')]")
            venda.click()
            
            wait_time()  
            
            documento = driver.find_element(by=By.NAME, value="s_1_1_11_0")
            documento.send_keys(str(base.loc[doc, 'DOCUMENTO']) + Keys.ENTER)
            
            wait_time()
            rentabilizar = driver.find_element(by=By.ID, value="s_1_1_10_0_Ctrl")
            rentabilizar.click()
            
            wait_time()        
           
            extract_contact()
            
            wait_time()        
            
            justificativa()
            
            wait_time()

        except Exception as e:
            login_smart.open_smart()
            print("Rentabilizar não disponível")
            wait_time()

def extract_contact():

        telefone_celular_path = driver.find_element(by=By.NAME, value="s_1_1_63_0")
        nome_path = driver.find_element(by=By.NAME, value="s_1_1_47_0")
        telefone_comercial_path = driver.find_element(by=By.NAME, value = "s_1_1_62_0")
        email_path = driver.find_element(by=By.NAME, value = "s_1_1_70_0")
        sms_path = driver.find_element(by=By.NAME, value = "s_1_1_71_0")
        contato_path = driver.find_element(by=By.NAME, value = "s_1_1_61_0")
        telefone_residencial_path = driver.find_element(by=By.NAME, value = "s_1_1_65_0")
        aceita_email_path = driver.find_element(by=By.NAME, value = "s_1_1_6_0")

        nome = nome_path.get_attribute("value")
        telefone_celular = telefone_celular_path.get_attribute("value")
        telefone_comercial = telefone_comercial_path.get_attribute("value")
        email = email_path.get_attribute("value")
        sms = sms_path.get_attribute("value")
        contato = contato_path.get_attribute("value")
        telefone_residencial= telefone_residencial_path.get_attribute("value")
        aceita_email = aceita_email_path.get_attribute("value")  

        leitura_base.save_result(base, nome, telefone_celular, telefone_comercial, email, sms, contato, telefone_residencial, aceita_email)

def justificativa():

        justificativa = driver.find_element(by=By.NAME, value="s_3_1_2_0")
        justificativa.send_keys("Endereço FWT" + Keys.ENTER)
        
        wait_time()        

        justificativa.send_keys(Keys.ENTER)
        
        wait_time()        

        botao_salvar = driver.find_element(by=By.NAME, value="s_3_1_3_0")
        botao_salvar.click()