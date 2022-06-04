from turtle import done
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

def extract_client_data(doc):   

    try:    
        time.sleep(2)

        print("passou1")

        venda = driver.find_element(by=By.XPATH, value="//span[contains(@title, 'Venda')]")
        venda.click()

        print("passou2")

        wait_time()  

        print("passou3")
        
        wait_time()
        
        documento = driver.find_element(by=By.NAME, value="s_1_1_11_0")
        documento.send_keys(str(doc) + Keys.ENTER)
        
        print("passou4")
        wait_time()
        print("passou5")
        
        tr = True
        i = 1
        while tr:
           
            try:
                product_name_path = f'//*[@id="{i}_s_4_l_Product_Name"]/span'
                install_date_path = f'//*[@id="{i}_s_4_l_Install_Date"]'
                product_name = driver.find_element(by=By.XPATH, value = product_name_path)
                install_date = driver.find_element(by=By.XPATH, value = install_date_path)
                print(product_name.text)
                print(install_date.text)

                i += 1
            except Exception as e:
                print(e)
                tr = False
    
    
    except Exception as e:
        login_smart.open_smart()
        print(e)
        wait_time()

                

    
        
        


        

    