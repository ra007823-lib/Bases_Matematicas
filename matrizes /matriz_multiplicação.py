def imprime_matriz(M,nome):
    print(nome,'=')
    linhas = len(M)
    colunas = len(M[0])
    for i in range(linhas):
        for j in range(colunas):
            print('[',M[i][j],']','',end='')
        print()
    print()

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

a = [
    [1,2],
    [3,4]
]

b = [
    [5,6],
    [7,8]
]
c = multiplicação(a,b)

imprime_matriz(a,'a')
imprime_matriz(b,'b')
imprime_matriz(c,'a x b')
