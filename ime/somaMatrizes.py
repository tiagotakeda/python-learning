def soma(mA, mB, lin, col):
    soma = []

    for i in range(lin):
        linhas = []
        for j in range(col):
            s = int(mA[i][j]) + int(mB[i][j])
            linhas.append(s)
        soma.append(linhas)

    return soma

if __name__ == '__main__':
    import sys
    soma(int(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]))