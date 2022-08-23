edad=input("Digite su edad: ")
#print(edad.isdigit())

while(edad.isdigit()==False):
    
    print("Por favor, introduce un valor numérico.")
    edad=input("Digite su edad: ")

if (int(edad)<18):
    print("No puede pasar")
else:
    print("Puede pasar")