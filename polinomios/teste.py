from sympy import *

x = symbols('x')
operacao = input('escolha a operação: adição(a) / subitração(s) / multiplicação(m) / divisão(d): ').lower()
a = sympify(input('digite o polinomio A(x): '))
b = sympify(input('digite o polinomio B(x): '))

if operacao == 'a':

    soma = a + b
    print(soma)

elif operacao == 's':

    subtracao = a - b
    print(subtracao)

elif operacao == 'm':

    multi = a * b
    print(multi)

elif operacao == 'd':

    q, r = div(a, b)

    print("Quociente:", q)
    print("Resto:", r)

else:
    print('opção invalida!')