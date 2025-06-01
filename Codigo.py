
import string

def limpiar_texto(texto):
    texto = texto.lower()
    texto = texto.replace(" ", "")
    texto = texto.translate(str.maketrans("", "", string.punctuation))
    return texto

