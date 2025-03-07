'''
OPERADORES LOGICOS
Los operadores logicos son:
- AND, or, not
obedecen las tablas de verdad
'''
op1 =True
op2 =True
op3 = op1 and op2
print(op3)

op1 =False
op2 =True
op3 = op1 or op2
print(op3)

op4 = not op2
print(op4)

'''
JERARQUIA DEFINITIVA DE OPERADORES 
1.        (  )
2.         ** 
3.      /, *, %
4.        +, -
5.   <, >, <=, >=, !=, ==
6.         not
7.         and
8.         or
9.          =
-si hay operaciones en el mismo nivel de jerarquia, se resuelven de izquierda a derecha
-si hay parentesis dentro del parentesis se resuelve el parentesis interno
'''

op1 =False
op2 =True
op3 =False
op4= True

r= not op1 and (op2 or op3 and not op1) and not op4
print(r)

