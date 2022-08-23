from datetime import datetime
from random import randint
#Se importa de asyncio
from asyncio import coroutine, sleep, Task, get_event_loop #El equivalente al Thread o al Process, en asyncio se llama Task
#Task es una cosa que está corriendo haciendo cosas

info = []
results = []

#Ahora las funciones son corrutinas, y se definen con async
async def generate_info():
    while True:
        #Pausa explícita
        await sleep(1) #Aquí cambia por el await, antes era pausar por un segundo, es pausar y dejar que otros corran.
        info.append(f"something at {datetime.now()}")
        print("New info added")

async def process_info():
    while True:
        await sleep(1)#Espera con un el await, espera un segundo. Y mientras se pausa, que otro pueda correr
        print("Cheking for new info")
        if info:#Entre el if y el new info no hay ninguún await
            #Por lo tanto las siguientes instrucciones se van a ejecutar siempre en orden hasta volver con el while al siguiente await.
            new_info = info.pop()
            results.append(new_info + "processed")
            print("New info processed")


#Necesitamos el loop al usar async, el que va corriendo cada corrutina hasta su pausa
loop = get_event_loop()#Llama a get_event_loop para obtener el loop
generator = loop.create_task(generate_info())#Dentro del loop, creo las tareas con las corrutinas definidas
processor1 = loop.create_task(process_info())
processor2 = loop.create_task(process_info())
loop.run_forever()#Le digo loop corre para siempre. Mientras haya corrutinas corriendo, sigue...