#Decorador para clases
def singleton(cls):

    instances = dict()#Diccionario de clases

    def wrap(*args, **kwargs): #Listado de argumentos y diccionario de argumentos
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        
        return instances[cls]

    return wrap

@singleton #Sobre cada clase
class User(object):
    def __init__(self, username):
        self.username = username

if __name__ == "__main__":

    user1 = User("Cody")
    user2 = User("facilito")

    print(user1 is user2)