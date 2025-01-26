import string
import itertools

def fuerza_bruta(contraseña_objetivo):
    caracteres = string.ascii_letters + string.digits
    intentos = 0
    print("comenzando a adivinar...")

    for longitud in range(1, 4): #4 caracteres
        for intento in map(''.join, itertools.product(caracteres, repeat=longitud)):
            intentos += 1
            if intento == contraseña_objetivo:
                print(f"contraseña encontrada: {intento}")
                print(f"He tardado: {intentos} intentos")
                return
    print("no se encontro la contraseña")

contraseña = "1b1" # Cambiar la contraseña de 3 digitos
fuerza_bruta(contraseña)