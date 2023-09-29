import random

'''
Ejercicio 1

Realizar un programa que inicialice una lista con 10 valores aleatorios (del
1 al 10) y posteriormente muestre en pantalla cada elemento de la lista
junto con su cuadrado y su cubo.
'''

#Generamos la lista de nuemros entre 1 y 10 aleatoriamente 
aleatorio = random.sample(range(1,11),10)

#Hacemos los calculos correspondientes
def cuadrado_cubo():
    cuadrado = [mul**2 for mul in aleatorio]
    print(f"{cuadrado}")
    cubo = [mult**3 for mult in aleatorio]
    print(f"{cubo}")
    
    
if __name__=="__main__":
    cuadrado_cubo()        