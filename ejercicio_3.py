'''
Ejercicio 3
Se quiere realizar un programa que lea por teclado las 5 notas obtenidas
por un alumno (comprendidas entre 0 y 10). A continuación, debe mostrar
todas las notas, la nota media, la nota más alta que ha sacado y la menor

'''
notas = []

def pedir():
    for i in range(5):
        notes = float(input(f"Ingrese la nota #{i+1}"))
        notas.append(notes)
    
    print(f"El promedio de las notas es {(sum(notas) / len(notas))}")
    notamax = notas[0]
    notamin = notas[0]
    for i in notas:
        if i > notamax:
            notamax = i
    for i in notas:
        if i < notamin:
            notamin = i
    print(f"La nota maxima es {notamax}")
    print(f"La nota minima es {notamin}")       

if __name__=="__main__":
    pedir()    