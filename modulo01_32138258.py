# Roberto Solis Robles
# Matricula 361772

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
