class Caracter:
    def __init__(self, dato,frecuencia):
        self.dato = dato
        self.frecuencia = frecuencia 

def dividirCaracteres(mensaje):
    caracteres = []
    frecuencia = []
    lista = []
    for m in mensaje:
        if m not in caracteres:
            caracteres.append(m)
            frecuencia.append(1)
        else:
            frecuencia[caracteres.index(m)] += 1

    for i in range(len(caracteres)):
        lista.append(Caracter(caracteres[i],frecuencia[i]))
        # print("[",caracteres[i],"],[",frecuencia[i],"]")
    return lista

def ordenarCaracteres(caracteres):
    caracteres = sorted(caracteres, key=lambda caracter : caracter.frecuencia, reverse=True)
    # print(sorted(caracteres, key=lambda caracter : caracter.frecuencia))
    return caracteres

def asignarCaracteres(caracteres,frecuencia):
    for i in range(len(caracteres)):
        caracteres[i].frecuencia = frecuencia[i]
    return caracteres

mensajeEncriptado = "53‡‡†305))6*;4826)4‡.)4‡);806*;48†8¶60))85;1‡(;:‡*8†83(88)5*†;46(;88*96*;8)*‡(;485);5 *†2:*‡ (;4956*2(5*—4)8¶8*;4069285);)6†8)4‡‡;1 (‡9;48081;8:8‡1;48†85;4)485†528806 *81(‡9;48;(88;4(‡?34; 48)4‡;161;:188;‡?;"
frequency = ["e","s","t","u","d","i","a","b","c","f","f","h","j","k","l","m","n","o","p","q","r","v","w","x","y"]

caracteres = dividirCaracteres(mensajeEncriptado)
caracteres = ordenarCaracteres(caracteres)
codigo = asignarCaracteres(caracteres,frequency)
