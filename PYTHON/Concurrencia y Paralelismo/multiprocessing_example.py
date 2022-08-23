import time
from datetime import datetime
from random import randint
#Importo multiprocessing y manager que me permite compartir memoria.
from multiprocessing import Process, Manager

shared_memory = Manager()

info = shared_memory.list([])#Info ya no es una lista. Es dame una lista que sea compartida en memoria
results = shared_memory.list([])#Lo mismo con resultados


def generate_info(info): #La funcion
    while True: #infinitamente está haciendo el while true
        time.sleep(1) #espera 1 segundo
        info.append(f"something at {datetime.now()}") #agrega un elemento a la lista de info
        print("New info added")

def process_info(info, results):
    while True: #Bucle Infinito
        time.sleep(1)#Que cada un segundo
        print("Cheking for new info")
        if info:#Sef ija si hay cosas en la lista de info
            new_info = info.pop() #Y si hay algo, lo saca
            results.append(new_info + "processed") #y lo agrega a la lista de de resultados
            print("New info processed")#Cambia diciendo que ya está procesado

#Instansio hilos y A cada Process le digo, con Target cual es la función que tiene que ejecutar y la lista se tiene que dar como parámetros
generator = Process(target=generate_info, args=[info])#El generador, que es un hilo que llama a la primera función. La que genera datos
processor1 = Process(target=process_info, args=[info, results])#Dos procesadores que son hilos que llaman a la funcion de procesar cosas
processor2 = Process(target=process_info, args=[info, results])# Osea hay una función que está metiendo a la lista de info y hay dos que están sacando

#Se le dice a cada hilo start y ya, el programa tiene esos 3 nuevos hilos que están corriendo
generator.start()
processor1.start()
processor2.start()

generator.join()