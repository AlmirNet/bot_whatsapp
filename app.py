# 1. Importar bibliotecas necessárias
import pywhatkit 
import keyboard 
import time 
from datetime import datetime 

# 2. Definir para quais contatos iremos enviar as msgs
contatos = ['+5561996573533','+5561996374752']
# 3. Definir intervalo de envio
while len(contatos) >= 1:
    # enviar mensagens 
    pywhatkit.sendwhatmsg(contatos[0],'VAMOS AUTOMATIZAR TUDO!', datetime.now().hour,datetime.now().minute + 2)
    del contatos[0]
    time.sleep(60)
    keyboard.press_and_release('ctrl + w')
# 4. Testar !