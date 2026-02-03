import random
import string

def generarLlaveDinamica(longitud):
    # caracteres ASCII que se pueden usar
    ascii_printable = string.printable
    llave = ""

    # se genera la llave caracter por caracter
    for i in range(longitud):
        caracter = random.choice(ascii_printable)
        llave = llave + caracter

    return llave

def cifrarLlaveTamanoFijo(mensaje, llave):
    cifrado = ""

    for i in range(len(mensaje)):
        valor_mensaje = ord(mensaje[i])

        # se reutiliza la llave usando el módulo
        posicion_llave = i % len(llave)
        valor_llave = ord(llave[posicion_llave])

        suma = valor_mensaje + valor_llave
        nuevo_valor = suma % 256

        cifrado = cifrado + chr(nuevo_valor)

    return cifrado

def cifradoLlaveDinamica(mensaje):
    # la llave tiene el mismo tamaño del mensaje
    llave = generarLlaveDinamica(len(mensaje))
    cifrado = ""

    for i in range(len(mensaje)):
        valor_mensaje = ord(mensaje[i])
        valor_llave = ord(llave[i])

        suma = valor_mensaje + valor_llave
        nuevo_valor = suma % 256

        cifrado = cifrado + chr(nuevo_valor)

    return cifrado, llave

def descifradoConLlave(mensaje_cifrado, llave):
    mensaje = ""

    for i in range(len(mensaje_cifrado)):
        valor_cifrado = ord(mensaje_cifrado[i])
        valor_llave = ord(llave[i % len(llave)])

        resta = valor_cifrado - valor_llave
        valor_original = resta % 256

        mensaje = mensaje + chr(valor_original)

    return mensaje

# llave = generarLlaveDinamica(10)
# print("Llave generada:", llave)

# mensaje = "CIFRADO DE INFORMACION"
# llave_fija = "KEY"

# cifrado = cifrarLlaveTamanoFijo(mensaje, llave_fija)
# print("Mensaje cifrado:", cifrado)


mensaje2 = "CIFRADO DINAMICO ASCII"

cifrado, llave_usada = cifradoLlaveDinamica(mensaje2)

print("Llave dinámica:", llave_usada)
print("Mensaje cifrado 2:", cifrado)
print("Mensaje descifrado: ", descifradoConLlave(cifrado, llave_usada))