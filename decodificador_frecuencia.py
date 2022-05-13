class TablaFrecuencia:
    asignacion = ""
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
        lista.append(TablaFrecuencia(caracteres[i],frecuencia[i]))
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
def desencriptar(mensaje,codigo):
    desencriptado = ""
    for m in range(len(mensaje)):
            for n in range(len(codigo)):
                if mensaje[m] == codigo[n].dato:
                    desencriptado += codigo[n].frecuencia   
    print(desencriptado)

def asignarCaracter(caracteres,frecuencia):
    for c in range(len(caracteres)):
        if caracteres[c].asignacion == "":
            caracteres[c].asignacion = frecuencia[0]
            del frecuencia[0]
            break

def frecuenciaTabla(caracteres, frecuencia):
    frecuenciaCaracteres = []
    caracteresAsignados = []

    for c in caracteres:
        if c.asignacion != "":
            caracteresAsignados.append(c.asignacion)
    for f in frecuencia:
        frecuenciaBigrama.append(TablaFrecuencia(f,0))

    for b in frecuenciaCaracteres:
        for c in caracteresAsignados:
            if c in b.dato:
                b.frecuencia += 1

    frecuenciaCaracteres = ordenarCaracteres(frecuenciaCaracteres)
    imprimirTablaAsignacion(frecuenciaCaracteres)

def asignarCaracteres(caracteres, frecuenciaCaracteres):
    
    for f in frecuenciaCaracteres:
        if f.frecuencia > 0:
            pass

def imprimirTablaAsignacion(caracteres):
    print("********************************************************")
    for i in range(len(caracteres)):
        print("[",caracteres[i].dato,"][",caracteres[i].frecuencia,"][",caracteres[i].asignacion ,"]")
    print("********************************************************")

mensajeEncriptado = "53‡‡†305))6*;4826)4‡.)4‡);806*;48†8¶60))85;1‡(;:‡*8†83(88)5*†;46(;88*96*?;8)*‡(;485);5*†2:*‡(;4956*2(5*—4)8¶8*;4069285);)6†8)4‡‡;1(‡9;48081;8:8‡1;48†85;4)485†528806*81(‡9;48;(88;4(‡?34;48)4‡;161;:188;‡?;"
# tablaCaracteres = "ethosnairdflbmgyuvpc"
tablaCaracteres = ["e","t","a","o","i","n","s","h","r","d","l","c","u","m","w","f","g","y","p","b","v","k","j","x","q","z"]
tablaBigramas = ["th", "he", "in", "en", "nt", "re", "er", "an", "ti", "es", "on", "at", "se", "nd", "or", "ar", "al", "te", "co", "de", "to", "ra", "et", "ed", "it", "sa", "em", "ro"]
tablaTrigramas = ["the","and","tha","ent","ing","ion","tio","for","nde","has" ,"nce" ,"edt" , "tis", "oft" ,"sth" , "men"]

caracteresOriginales = dividirCaracteres(mensajeEncriptado)
#imprimirTablaAsignacion(caracteresOriginales)
caracteresOrdenados = ordenarCaracteres(caracteresOriginales)
#imprimirTablaAsignacion(caracteresOrdenados)
asignarCaracter(caracteresOrdenados,tablaCaracteres)
asignarCaracter(caracteresOrdenados,tablaCaracteres)
imprimirTablaAsignacion(caracteresOrdenados)
frecuenciaTabla(caracteresOrdenados,tablaTrigramas)
frecuenciaTabla(caracteresOrdenados,tablaBigramas)
print(tablaCaracteres)


#codigo = asignarCaracteres(caracteres,tablaCaracteres)
desencriptar(mensajeEncriptado,caracteresOrdenados)