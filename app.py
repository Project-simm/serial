import serial
import datetime
import time
'''
minha ideia é mandar um "tick" ou um sinal para verificar a cada minuto ao ESP se bateu o horario a cada minuto
a cada minuto ele iria tirar a informação do BD, que la terá os dados dos horarios dos remedios 
(deixando claro que o ESP ja teria essa informação) e armazenaria numa variavel ou poderia pxar a cada hora no proprio BD mesmo
e a cada 60 seg ele verificaria com um IF se seria o horario, se sim tocaria o alarme
'''
# serial connection
var = "variavel que puxaria o horario do BD"
var_all = "variavel que puxaria nome e quantidade (pode ser uma lista ou dicionario ou mais uma variavel so para a quantidade)"
while True:
    date = datetime.datetime.now()  
    time.sleep(60)
    #ser = serial.Serial(port="COM3",19200, timeout=1)
    #codigo do ESP abaixo 
    if var == date:
        pass
        #ser.write(b'alarme') #alarme
    else:
        pass
        #ser.write(b'off') #off
    print(date)
