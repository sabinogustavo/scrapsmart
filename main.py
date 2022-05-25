import leitura_base
import scrap_smart
import login_smart
import time


leitura_base.read_base()
time.sleep(3)
login_smart.open_smart()

login_smart.login_smart()

try:
    scrap_smart.extract_client_data()
    scrap_smart.justificativa()

except Exception as e:
    print("Erro ao enviar msg", e)


