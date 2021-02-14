import random
 
MINA  = -1
LIVRE = 0
 
def criaMatriz(m, n, valor):
    matriz = []
    for i in range(m):
        linha = []
        for j in range(n):
            linha.append(valor)
        matriz.append(linha)
    return matriz
 
def embaralha(matriz):
    m = len(matriz)
    n = len(matriz[0])
    for i in range(m):
        for j in range(n):
            ii = random.randrange(0,m)
            jj = random.randrange(0,n)
            matriz[i][j], matriz[ii][jj] = matriz[ii][jj], matriz[i][j]
 
def criaCampo(m, n, nminas):
    campo = criaMatriz(m, n, LIVRE)
    k = 0
    for i in range(m):
        for j in range(n):
            if k < nminas:
                campo[i][j] = MINA
                k += 1
    embaralha(campo)
    return campo

# import random
#  
# MINA  = -1
# LIVRE = 0
#  
# def criaCampo(m, n, nminas):
#     C = [MINA]*nminas + [LIVRE]*(m*n - nminas)
#     random.shuffle(C)
#     campo = []
#     for i in range(m):
#         campo.append(C[i*n:(i+1)*n])
#     return campo