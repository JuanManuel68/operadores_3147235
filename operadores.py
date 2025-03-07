'''
JERARQUIA DE SIMBOLOS DE PYTOHN 
1.        (  )
2.         ** 
3.      /, *, %
4.        +, -
5.          =

-si hay operaciones en el mismo nivel de jerarquia, se resuelven de izquierda a derecha
-si hay parentesis dentro del parentesis se resuelve el parentesis interno
'''

a = 3
b = 2 
c = 1
x=5
y = c/(c+2)<c*a-c+1-b*2
print(y)  # Salida: 7

''' 
OPERADORES RELACIONALES 
Las operaciones aritmeticas resultan en un valos numerico:
LAS OPERACIONES RELACIONALES 
Resultan en un valor booleano:
True o False(v, f, si o no)
>,<,>=,<=,!=,==
JERARQUIA DE OPERADORES 
(Incluyendo los relacionales)
1.        (  )
2.         **
3.      /, *, %
4.        +, -
5.  <, >, <=, >=, !=, ==
6.        =
'''
a = 2
b = 3 
c = 7
x=5
y=c/(x+2)<c*a-c+1-b*2
print(y)  # Salida