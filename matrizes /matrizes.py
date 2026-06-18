def matriz_a():
    linhas = int(input('quantas linhas deseja: '))
    colunas = int(input('quantas colunas deseja: '))
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            valor = int(input())
            linha.append(valor)
        matriz.append(linha)
    return matriz

def matriz_b():
    linhas = int(input('quantas linhas deseja: '))
    colunas = int(input('quantas colunas deseja: '))
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            valor = int(input())
            linha.append(valor)
        matriz.append(linha)
    return matriz

def imprime_matriz(M,nome):
    print(nome,'=')
    linhas = len(M)
    colunas = len(M[0])
    for i in range(linhas):
        for j in range(colunas):
            print('[',M[i][j],']','',end='')
        print()
    print()

def diagonal(A):
    return [A[i][i] for i in range(len(A))]
def determinante(A):
    return A[0][0] * A[1][1] - A[0][1] * A[1][0]

def multiplicação(a,b):
    n = len(a)
    p = len(b)
    m = len(b[0])
    c = [[0] * m for _ in range (n)]
    for i in range(n):
        for j in range(m):
            for k in range(p):
                c[i][j] = a[i][k] * b[k][j]    
    return c

def soma_matrizes(a,b):
    n = len(a)
    m = len(a[0])
    c = [[0] * m for _ in range (n)]
    for i in range(n):
        for j in range(m):
            c[i][j] = a[i][j] + b[i][j]
    return c

def subtrai_matrizes(a,b):
    n = len(a)
    m = len(a[0])
    c = [[0] * m for _ in range (n)]
    for i in range(n):
        for j in range(m):
            c[i][j] = a[i][j] - b[i][j]
    return c

def transposta(A):
    n = len(A)
    m = len(A[0])
    t = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            t[j][i] = A[i][j]
    return t

operacao = input('qual operação deseja realizar: Soma \033[1;31;43m(S)\033[m/ Subtrai \033[1;31;43m(Sub)\033[m/ Transposta \033[1;31;43m(T)\033[m / Multiplicação \033[1;31;43m(M)\033[m / Diagonal Principal e Determinante \033[1;31;43m(DPD)\033[m').lower()

if operacao =='s':

    a = matriz_a()
    b = matriz_b()

    c = soma_matrizes(a,b)
    imprime_matriz(a,'a')
    imprime_matriz(b,'b')
    imprime_matriz(c,'a + b')

elif operacao =='sub':

    a = matriz_a()
    b = matriz_b()

    c = subtrai_matrizes(a,b)
    imprime_matriz(a,'a')
    imprime_matriz(b,'b')
    imprime_matriz(c,'a - b')

elif operacao =='t':

    a = matriz_a([])

    t = transposta(a)

    imprime_matriz(a,'a')
    imprime_matriz(t,'t')

elif operacao =='m':

    a = matriz_a()
    b = matriz_b()

    c = multiplicação(a,b)

    imprime_matriz(a,'a')
    imprime_matriz(b,'b')
    imprime_matriz(c,'a x b')

elif operacao =='dpd':

    a = matriz_a()

    d = diagonal(a)

    det = determinante(a)

    imprime_matriz(a,'a')
    print('Diagonal Principal =',d)
    print('Determinante =',det)

else:
    print('opção invalida!')