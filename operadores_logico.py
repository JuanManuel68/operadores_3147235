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
'''
