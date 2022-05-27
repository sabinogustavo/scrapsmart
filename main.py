import leitura_base
import scrap_smart
import login_smart
import time


df = leitura_base.read_base()

time.sleep(3)

login_smart.open_smart()

login_smart.login_smart()

for doc in df:
    try:
        contact = scrap_smart.extract_client_data(str(doc).zfill(14))
        print(contact)
        leitura_base.save_result(str(doc).zfill(14), contact)

    except Exception as e:
        print( e)


