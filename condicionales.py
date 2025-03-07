''' 
CONDICIONAL:
Exprecion que, al ser evaluada da como resultado un valor verdadero o falso 
Por tanto, en una condicional deben haber 
operadores relacionales o logicos 
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
#ejemplo de condicional
a=3
b=2
c=1
d=4
r=not(a**2-b>c**2)and((a*3+c)/2<d)or True
print(r)
#ejemplo de condicional
x=5
y=10
z=5
r=(x==z+(8/z)) and not ((y+3)*(4/(z+1)))==z
print(r)
