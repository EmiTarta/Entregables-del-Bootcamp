#Poner aqui las funciones creadas en el ejercicio_funciones para poder importarlas en el ultimo ejercicio

# Ejercicio 1
def conversor (num):
    num = num*num 
    return f"Tu numero es: {num}"

# Ejercicio 2
def piramide(filas):
    for num in range(filas, 0, -1): 
        for num in range(num, 0, -1): 
            print(num, end=" ") 
        print()

# Ejercicio 3
def compara (num1, num2):
    if num1 == num2:
        return f'{num1} y {num2} son iguales'
    if num1 > num2:
        return f' {num1} es mayor que {num2}'
    if num1 < num2:
        return f'{num2} es mayor a {num1}'

# Ejercicio 4    
def contar_letras (texto, letra):
    if letra in texto:
       x = texto.count(letra)
       return x

# Ejercicio 5    
dic_frase = {}
def diccio_cuenta (frase):
    for letra in frase:
        if letra in dic_frase:
            dic_frase[letra] = dic_frase[letra] + 1
        else:
            dic_frase[letra] = 1
    return dic_frase

# Ejercicio 6
def agrega_elimina (lista, comando, elemento = None):
    if comando == "add":
        lista.append(elemento)
        return lista
    elif comando == "remove":
        if elemento in lista:
            lista.remove(elemento)
            return lista
        else:
            return "Ese elemento no esta en la lista"

# Ejercicio 7        
def palabras(*args):
    return " ".join(args)

# Ejercicio 8
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Ejercicio 9
#     
import math 

def area_cuadrado(lado):
    area = lado * lado
    return area

def area_triangulo(base, altura):
    area = (base * altura)/2
    return area 

def area_circulo(radio):
    area = math.pi * (radio **2)
    return area