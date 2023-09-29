'''
Ejercicio 2

Crea una lista e inicialízala con 5 cadenas de caracteres leídas por teclado.
Copia los elementos de la lista en otra lista, pero en orden inverso, y
muestra sus elementos por la pantalla.
'''

cadenas =[]

def main():
    for i in range(5):
        cadena = input(f"Ingrese la cadena de texto #{i+1} (; ")
        cadenas.append(cadena)
    new_cadenas = cadenas.copy()
    new_cadenas.reverse()
    print("\nCadena normal")
    for i in cadenas:
        print(i,end =" | ")
    print("\nCadena inversa")
    for i in new_cadenas:
        print(i,end=" | ")

if __name__=="__main__":       
    main()  



    
'''    
cadenas = []

def solicitar_cadena(i):
    """Solicita una cadena de texto al usuario."""
    while True:
        cadena = input(f"Ingrese la cadena de texto #{i + 1}: ")
        if cadena.strip():  # Verifica si la cadena no está vacía
            return cadena
        

def imprimir_cadenas(mostrar, mensaje):
    """Imprime las cadenas de texto."""
    print(mensaje)
    print(" | ".join(mostrar))

def main():
    for i in range(5):
        pedir = solicitar_cadena(i)
        cadenas.append(pedir)
    
    new_cadenas = cadenas.copy()
    new_cadenas.reverse()

    imprimir_cadenas(cadenas, "Cadena normal")
    imprimir_cadenas(new_cadenas, "Cadena inversa")

if __name__ == "__main__":
    main()
        
'''