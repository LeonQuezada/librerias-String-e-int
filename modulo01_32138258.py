# Leon Edward Quezada Reyes
# Matricula 32138258

MINUSCULAS_SPA_UNICODE = "abcdefghijklmnñopqrstuvwxyzáéíóúü"
MAYUSCULAS_SPA_UNICODE = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZÁÉÍÓÚÜ"
DIGITOS_DECIMALES = "0123456789"

def capitaliza( original ):
    " Esta función convierte a mayúscula el primer caracter del string"
    # Verificamos el primer caracter del string original
    if original[0] not in MINUSCULAS_SPA_UNICODE:
        # No esta en minuscula, por tanto copia la original
        nueva = original[:]
    else:
        # Primer caracter es minuscula, lo convertimos a mayuscula
        # y copiamos el resto del string original.
        nuevochar = chr( ord( original[0] ) - 32 )
        nueva = str( nuevochar ) + original[1:]
    return nueva

def es_alfa(texto):
    salida = False
    for i in range(len(texto)):
        if texto[i] in MINUSCULAS_SPA_UNICODE or texto[i] in MAYUSCULAS_SPA_UNICODE:
            salida=True
        else:
            salida=False
            break
    return salida

def es_digito(entero):
    salida = False
    for i in range(len(str(entero))):
        if str(entero)[i] not in DIGITOS_DECIMALES:
            salida=True
        else:
            salida=False
            break
    return salida

def a_minus(texto):
    nuevoTexto=[]
    salidaTexto=""
    for i in range(len(texto)):
        if not es_digito(texto[i]):
            nuevoTexto.append(texto[i])
        if texto[i] in MAYUSCULAS_SPA_UNICODE:
            nuevoTexto.append(texto[i])
        else:
            for j in range(len(MINUSCULAS_SPA_UNICODE)):
                if MINUSCULAS_SPA_UNICODE[j] == texto[i]:
                    nuevoTexto.append(MAYUSCULAS_SPA_UNICODE[j])
    for i in range(len(nuevoTexto)):
        salidaTexto+=nuevoTexto[i]
    return salidaTexto

def a_mayus(texto):
    nuevoTexto=[]
    salidaTexto=""
    for i in range(len(texto)):
        if not es_digito(texto[i]):
            nuevoTexto.append(texto[i])
        if texto[i] in MINUSCULAS_SPA_UNICODE:
            nuevoTexto.append(texto[i])
        else:
            for j in range(len(MAYUSCULAS_SPA_UNICODE)):
                if MAYUSCULAS_SPA_UNICODE[j] == texto[i]:
                    nuevoTexto.append(MINUSCULAS_SPA_UNICODE[j])
    for i in range(len(nuevoTexto)):
        salidaTexto+=nuevoTexto[i]
    return salidaTexto

def encuentra_chr(texto,letra):
    if len(letra)==1:
        for i in range(len(texto)):
            if texto[i]==letra:
                return i
            else:
                return -1
    else:
        return -1

def encuentra_str(texto,cadena):
    return False