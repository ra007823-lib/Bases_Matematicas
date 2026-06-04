def imprime_matriz(M,nome):
    print(nome,'=')
    linhas = len(M)
    colunas = len(M[0])
    for i in range(linhas):
        for j in range(colunas):
            print('[',M[i][j],']','',end='')
        print()
    print()


def soma_matrizes(a,b):
    n = len(a)
    m = len(a[0])
    c = [[0] * m for _ in range (n)]
    for i in range(n):
        for j in range(m):
            c[i][j] = a[i][j] + b[i][j]
    return c

a = [
    [1,2],
    [3,4]
]
b = [
    [5,6],
    [7,8]
]
c = soma_matrizes(a,b)
imprime_matriz(a,'a')
imprime_matriz(b,'b')
imprime_matriz(c,'a + b')