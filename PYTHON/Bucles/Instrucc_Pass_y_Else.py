from __future__ import barry_as_FLUFL


class Miclase:
    pass

email=input("Introduce tu email, por favor: ")

for i in email:
    if i=="@":
        arroba=True
        break;
else:
    arroba=False

print(arroba)