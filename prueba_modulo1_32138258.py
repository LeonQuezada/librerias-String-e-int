# Leon Edward Quezada Reyes
# Matricula 32138258
from modulo01_32138258 import *

#------Modulo que ayudo a la pruebas
def my_strtr(cadena, reemplazo):    
    """Reemplazo múltiple de cadenas en Python."""
    import re
    regex = re.compile("(%s)" % "|".join(map(re.escape, reemplazo.keys())))
    return regex.sub(lambda x: str(reemplazo[x.string[x.start() :x.end()]]), cadena)

#------ fin de Modulo que ayudo a la pruebas


print("----------------------------------------------------------------")
print( "La constante MINUSCULAS_SPA_UNICODE tiene el siguiente valor:" )
print( MINUSCULAS_SPA_UNICODE )
print("----------------------------------------------------------------")
print( "La constante MAYUSCULAS_SPA_UNICODE tiene el siguiente valor:" )
print( MAYUSCULAS_SPA_UNICODE )
print("----------------------------------------------------------------")
print( "La constante DIGITOS_DECIMALES tiene el siguiente valor:" )
print( DIGITOS_DECIMALES )
print("----------------------------------------------------------------")

print("")
#----------------Prueba 0---------------------
A = "Roberto Solis Robles"
B = "es el profesor de cómputo paralelo"

print( "Demostramos ahora la función capitaliza" )
print( "con los strings '",A,"' y '",B,"'", sep="")
A1 = capitaliza(A)
B1 = capitaliza(B)
A2 = A[0].upper()+A[1:]
B2 = B[0].upper()+B[1:]
print( "Mi función genera '",A1,"' y '",B1,"'", sep="")
print( "Usando str.upper genera '",A2,"' y '",B2,"'", sep="")
print( "Correctos: "+str(A1==A2 and B1==B2) )
print("----------------------------------------------------------------")
print()
#----------------Fin Prueba 0---------------------

#----------------Prueba 1---------------------
A="123"
B="hola"

A1=es_alfa(A)
B1=es_alfa(B)
A2=A.isalpha()
B2=B.isalpha()

print( "Demostramos ahora la función es_alfa" )
print( "con los strings '",A,"' y '",B,"'", sep="")
print( "Mi función genera '",A1,"' y '",B1,"'", sep="")
print( "Usando str.isalpha genera '",A2,"' y '",B2,"'", sep="")
print( "Correctos: "+str(A1==A2 and B1==B2) )
print("----------------------------------------------------------------")
print()
#----------------Fin Prueba 1---------------------

#----------------Prueba 2---------------------
A="1"
B="123e"

A1=es_digito(A)
B1=es_digito(B)

A2=A.isdigit()
B2=B.isdigit()
print( "Demostramos ahora la función es_digito" )
print( "con los strings '",A,"' y '",B,"'", sep="")
print( "Mi función genera '",A1,"' y '",B1,"'", sep="")
print( "Usando str.isdigit genera '",A2,"' y '",B2,"'", sep="")
print( "Correctos: "+str(A1==A2 and B1==B2) )
print("----------------------------------------------------------------")
print()
#----------------Fin Prueba 2---------------------

#----------------Prueba 3---------------------
A="hoLa"
B="HOLA"

A1=a_minus(A)
B1=a_minus(B)

A2=A.lower()
B2=B.lower()

print( "Demostramos ahora la función a_minus" )
print( "con los strings '",A,"' y '",B,"'", sep="")
print( "Mi función genera '",A1,"' y '",B1,"'", sep="")
print( "Usando str.lower genera '",A2,"' y '",B2,"'", sep="")
print( "Correctos: "+str(A1==A2 and B1==B2) )
print("----------------------------------------------------------------")
print()
#----------------Fin Prueba 3---------------------

#----------------Prueba 4---------------------
A="hoLa"
B="hola"

A1=a_mayus(A)
B1=a_mayus(B)

A2=A.upper()
B2=B.upper()

print( "Demostramos ahora la función a_mayus" )
print( "con los strings '",A,"' y '",B,"'", sep="")
print( "Mi función genera '",A1,"' y '",B1,"'", sep="")
print( "Usando str.upper genera '",A2,"' y '",B2,"'", sep="")
print( "Correctos: "+str(A1==A2 and B1==B2) )
print("----------------------------------------------------------------")
print()
#----------------Fin Prueba 4---------------------

#----------------Prueba 5---------------------
A="Hola Como estas"
B="que tal amigo"
C = "o"

A1=encuentra_chr(A,C)
B1=encuentra_chr(B,C)

A2=A.find(C)
B2=B.find(C)

print( "Demostramos ahora la función encuentra_chr" )
print( "con los strings '",A,"' y '",B,"'"," Con el patron: ","'" ,C, "'", sep="")
print( "Mi función genera '",A1,"' y '",B1,"'", sep="")
print( "Usando str.upper genera '",A2,"' y '",B2,"'", sep="")
print( "Correctos: "+str(A1==A2 and B1==B2) )
print("----------------------------------------------------------------")
print()
#----------------Fin Prueba 5---------------------

#----------------Prueba 6---------------------
A="Hola Como estas"
B="que tal amigo hola"
C = "la"

A1=encuentra_str(A,C)
B1=encuentra_str(B,C)

A2=A.find(C)
B2=B.find(C)

print( "Demostramos ahora la función encuentra_str" )
print( "con los strings '",A,"' y '",B,"'"," Con el patron: ","'" ,C, "'", sep="")
print( "Mi función genera '",A1,"' y '",B1,"'", sep="")
print( "Usando str.upper genera '",A2,"' y '",B2,"'", sep="")
print( "Correctos: "+str(A1==A2 and B1==B2) )
print("----------------------------------------------------------------")
print()
#----------------Fin Prueba 6---------------------

#----------------Prueba 7---------------------
A="hola como estas"
B="que tal amigo"

letra1="o"
letra2="a"
patron="z"

A1=reemplaza_chr(A,letra1,patron)
B1=reemplaza_chr(B,letra2,patron)

A2=my_strtr(A,{'o':'z'})
B2=my_strtr(B,{'a':'z'})
print( "Demostramos ahora la función reemplaza_chr" )
print( "con los strings '",A,"' y '",B,"'"," Con el patron: ","'" ,patron, "'"," Con el letra1: ","'" ,letra1, "'"," Con el letra2: ","'" ,letra2, "'", sep="")
print( "Mi función genera '",A1,"' y '",B1,"'", sep="")
print( "Usando str.upper genera '",A2,"' y '",B2,"'", sep="")
print( "Correctos: "+str(A1==A2 and B1==B2) )
print("----------------------------------------------------------------")
print()
#----------------Fin Prueba 7---------------------

#----------------Prueba 8---------------------

A="holass"
B="que tal amigo"

letra1="la"
letra2="am"
patron="zs"

A1=reemplaza_str(A,letra1,patron)
B1=reemplaza_str(B,letra2,patron)

A2=my_strtr(A,{'la':'zs'})
B2=my_strtr(B,{'am':'zs'})

print( "Demostramos ahora la función reemplaza_str" )
print( "con los strings '",A,"' y '",B,"'"," Con el patron: ","'" ,patron, "'"," Con el letra1: ","'" ,letra1, "'"," Con el letra2: ","'" ,letra2, "'", sep="")
print( "Mi función genera '",A1,"' y '",B1,"'", sep="")
print( "Usando str.upper genera '",A2,"' y '",B2,"'", sep="")
print( "Correctos: "+str(A1==A2 and B1==B2) )
print("----------------------------------------------------------------")
print()
#----------------Fin Prueba 8---------------------