for i in ["Pildoras", "Informaticas","ATS"]:
    print("Hola", end=" ")

email=False
correo=input("\nIntroduzca su correo electrónico: ")

for i in correo:
    if(i=="@" and i=="."):
        
        email=True

if email==True:
    print("\nEmail correcto")
else:
    print("\nEl email es incorrecto")