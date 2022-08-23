def generaPares(limite):

    num=1

    while num<limite:

        yield num*2
        num+=1

devuelvepares=generaPares(10)

print(next(devuelvepares))
print("Aquí podría ir más codigo...")
print(next(devuelvepares))
print("Aquí podría ir más codigo...")
print(next(devuelvepares))
#for i in devuelvepares:
 #   print(i)