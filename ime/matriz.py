def cria_matriz(nLinhas, nColunas):
    matriz = []
    valor = 0
    for i in range(nLinhas):
        linhas = []
        for j in range(nColunas):
            print("Digite A[", i, "][", j, "]: ", sep="", end="")
            valor = int(input())
            linhas.append(valor)
        matriz.append(linhas)
    
    return matriz


def somaMatrizes(mA, mB, lin, col):
    soma = []

    for i in range(0, lin-1):
        linhas = []
        for j in range(0, col-1):
            s = int(mA[i][j]) + int(mB[i][j])
            linhas.append(s)
        soma.append(linhas)

    return soma

def main():
    print("Para proseguir escolha uma das opções: ")
    print("1) Impressão de uma simples matriz")
    print("2) Soma de duas matrizes")
    print("3) Digite qualquer outro número para sair do programa")

    modo = int(input())

    while modo == 1 or modo == 2:
        if modo == 1:
            linhas = int(input("Número de linhas: "))
            colunas = int(input("Número de colunas: "))
            matriz = cria_matriz(linhas, colunas)

            print("\nA matriz gerada foi: \n")
            for i in range(linhas):
                print("\t", matriz[i])      
                    
            print()

        elif modo == 2:
            print("Defina a primeira matriz\n")
            linhas = int(input("Número de linhas: "))
            colunas = int(input("Número de colunas: "))
            mA = cria_matriz(linhas, colunas)

            print("\nDefina a segunda matriz\n")
            mB = cria_matriz(linhas, colunas)

            soma = somaMatrizes(mA, mB, linhas, colunas)

            print("\nA soma das matrizes: \n")
            for i in range(0, linhas-1):
                print("\t", soma[i])      
                    
            print()

        print("Para proseguir escolha uma das opções: ")
        print("1) Impressão de uma simples matriz")
        print("2) Soma de duas matrizes")
        print("3) Digite qualquer outro número para sair do programa")
        modo = int(input())
    

main()