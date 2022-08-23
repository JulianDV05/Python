#print("Verificación de acceso")

#edad_usuario=int(input("Introduzca su edad por favor: "))

#if edad_usuario < 18:
#	print("No puede pasar.")
#elif edad_usuario > 100:
#	print("Edad incorrecta.")
#elif edad_usuario>18:
#	print("Puede pasar")

#print("Programa finalizado")

print("Verificación de acceso")

nota=float(input("Introduzca su nota, por favor: "))

if nota<5:
	print("Insuficiente")
elif nota<6:
	print("suficiente")
elif nota<7:
	print("Bien")
elif nota<9:
	print("Notable")
else:
	print("Sobresaliente")