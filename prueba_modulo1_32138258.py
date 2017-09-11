# Leon Edward Quezada Reyes
# Matricula 32138258
from modulo01_361772 import *

print( "La constante MINUSCULAS_SPA_UNICODE tiene el siguiente valor:" )
print( MINUSCULAS_SPA_UNICODE )

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


