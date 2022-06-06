import leitura_base
import controle_smart
import time

smart = controle_smart

df = leitura_base.read_base()

smart.open_smart()

smart.login_smart()

for doc in df:
    smart.get_data(doc)


