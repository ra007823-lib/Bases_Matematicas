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

a = [
    [1,2],
    [3,4]
]

d = diagonal(a)

det = determinante(a)

imprime_matriz(a,'a')
print('Diagonal Principal =',d)
print('Determinante =',det)