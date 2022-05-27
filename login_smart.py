from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

def open_smart():

    driver.get("https://vivovendas.vivo.com.br/sales_ext/start.swe")


def login_smart():

    user = 80836247
    password = "Grog@34av"

    user_login = driver.find_element(by=By.ID, value = "username")
    user_password = driver.find_element(by=By.ID, value = "password")

    user_login.send_keys(user)
    user_password.send_keys(password)

    input("Aperte ENTER após o login e tela de carregamento concluído \n")


