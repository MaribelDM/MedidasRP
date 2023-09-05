import requests
import Adafruit_DHT
import datetime
import time

lista_humedades = []
lista_temperaturas = []

def agregar_a_lista(fecha, idSensor, valor, isHumedad):
    objeto = {'fecha': fecha, 'idSensor': idSensor, 'valor': valor}
    if isHumedad:
        lista_humedades.append(objeto)
    else:
        lista_temperaturas.append(objeto)

while True:
    #Lectura sensores
    sensor = Adafruit_DHT.DHT22
    pin = 4
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    print('medidad' + str(humidity))
    sensor = Adafruit_DHT.DHT22
    pin17 = 17
    humidity17, temperature17 = Adafruit_DHT.read_retry(sensor, pin17)
    print('medida17 ' + str(humidity17))
    now = datetime.datetime.now()
    now_string =  '{:%Y-%m-%d %H:%M:%S}'.format(now)

    #Llamada POST
    agregar_a_lista(now_string, '1', humidity, True)
    agregar_a_lista(now_string, '3', temperature, False)
    agregar_a_lista(now_string, '13', humidity17, True)
    header_enviar = {'Content-Type': 'application/json;charset=UTF-8'}

    resp1 = requests.post('http://192.168.245.129:8091/v1/sensores/medidas-humedad', json=lista_humedades, headers=header_enviar)

    resp2 = requests.post('http://192.168.245.129:8091/v1/sensores/medidas-temperatura', json =lista_temperaturas, headers= header_enviar)

    print('Medida humedad: ' + resp1.text + '. Medida temperatura: ' + resp2.text)

    time.sleep(60)
