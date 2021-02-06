import cria_matriz
import somaMatrizes

def matrizes(A, B):
    lin = len(B)
    col = len(A[0])
    n = len(A)

    if lin != col:
        print("Matrizes incompatíveis para multiplicação")
        return

    soma = []

    for i in range(lin):
        linhas = []
        for j in range(col):
            linhas.append(0)
        soma.append(linhas)
    
    for i in range(n):
        for j in range(lin):
            for k in range(col):
                soma[i][j] += int(A[i][k])*int(B[k][j])
    return soma
            
def matrizConstante(A, n):
    result = []
    for i in range(len(A)):
        result.append([])
        for j in range(len(A[0])):
            result[i].append(A[i][j]*n) 
    return result

if __name__ == '__main__':
    import sys
    matrizConstante(list(sys.argv[1], sys.argv[2]))