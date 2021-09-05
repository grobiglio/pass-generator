import random
from typing import Counter

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("¡Bienvenido al generador de contraseñas!")

try:
    nr_letters= int(input("¿Cuántas letras querés que tenga la contraseña?\n")) 
    nr_symbols = int(input("¿Cuántos símbolos?\n"))
    nr_numbers = int(input("¿Cuántos números?\n"))
except ValueError:
    print("Debés ingresar un caracter válido.")
    quit()

composicion = list("L"*nr_letters+"S"*nr_symbols+"N"*nr_numbers)
random.shuffle(composicion)

contrasena = ""
for tipo_caracter in composicion:
    if tipo_caracter == "L":
        contrasena += random.choice(letters)
    elif tipo_caracter == "S":
        contrasena += random.choice(symbols)
    else:
        contrasena += random.choice(numbers)

print(f"Tu contraseña es: {contrasena}")
