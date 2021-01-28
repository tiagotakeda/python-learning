def somaMatrizes(mA, mB, lin, col):
    soma = []

    for i in range(lin):
        for j in range(col):
            soma[i][j] = mA[i][j] + mB[i][j]

    return soma