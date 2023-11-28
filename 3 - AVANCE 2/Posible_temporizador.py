
#Temporizador

import time
import sys

inicio = time.time()

segundos = 0 
minutos = 0

while True:
    try:
        sys.stdout.write('\r{minutos}:{segundos}'.format(minutos=minutos,segundos=segundos))
        sys.stdout.flush()
        time.sleep(1)
        segundos = int(time.time() - inicio) - minutos * 60
        
        if segundos >=60:
            minutos += 1
            segundos = 0
    
    except KeyboardInterrupt:
        break
    