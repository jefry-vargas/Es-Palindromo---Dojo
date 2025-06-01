
import string

def limpiar_texto(texto):
    texto = texto.lower()
    texto = texto.replace(" ", "")
    texto = texto.translate(str.maketrans("", "", string.punctuation))
    return texto

def es_palindromo(texto):
    texto_limpio =  limpiar_texto(texto)
    return texto_limpio == texto_limpio[::-1]

if __name__ == "__main__":
    palabra = input("Escribe una palabra o frase :")
    if es_palindromo(palabra):
        print("Es un palindromo")
    else:
        print("No es un palindromo")
