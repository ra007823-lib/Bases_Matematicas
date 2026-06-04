def imprime_matriz(M,nome):
    print(nome,'=')
    linhas = len(M)
    colunas = len(M[0])
    for i in range(linhas):
        for j in range(colunas):
            print('[',M[i][j],']','',end='')
        print()
    print()


def transposta(A):
    n = len(A)
    m = len(A[0])
    t = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            t[j][i] = A[i][j]
    return t

a = [
    [1,2,3],
    [4,5,6]
]

t = transposta(a)

imprime_matriz(a,'a')
imprime_matriz(t,'t')