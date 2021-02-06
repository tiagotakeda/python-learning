import cria_matriz
import somaMatrizes
import multiplicaMatrizes

def main():
    print("Para proseguir escolha uma das opções: ")
    print("1) Impressão de uma simples matriz")
    print("2) Soma de duas matrizes")
    print("3) Multiplicação de duas matrizes")
    print("4) Multiplicação de matriz por constante")
    print("5) Digite qualquer outro número para sair do programa")

    modo = int(input())

    while modo == 1 or modo == 2 or modo == 3 or modo == 4:
        if modo == 1:
            linhas = int(input("Número de linhas: "))
            colunas = int(input("Número de colunas: "))
            matriz = cria_matriz.cria(linhas, colunas)

            print("\nA matriz gerada foi: \n")
            for i in range(linhas):
                print("\t", matriz[i])      
                    
            print()

        elif modo == 2:
            print("Defina a primeira matriz\n")
            linhas = int(input("Número de linhas: "))
            colunas = int(input("Número de colunas: "))
            mA = cria_matriz.cria(linhas, colunas)

            print("\nDefina a segunda matriz\n")
            mB = cria_matriz.cria(linhas, colunas)

            soma = somaMatrizes.soma(mA, mB, linhas, colunas)

            print("\nA soma das matrizes: \n")
            for i in range(linhas):
                print("\t", soma[i])      
                    
            print()

        elif modo == 3:
            print("Defina a primeira matriz\n")
            linhas = int(input("Número de linhas: "))
            colunas = int(input("Número de colunas: "))
            mA = cria_matriz.cria(linhas, colunas)

            print("\nDefina a segunda matriz\n")
            mB = cria_matriz.cria(linhas, colunas)

            mult = multiplicaMatrizes.matrizes(mA, mB)

            print("\nA multiplicação das duas matrizes: \n")
            for i in range(linhas):
                print("\t", mult[i])      
                    
            print()

        elif modo == 4:
            linhas = int(input("Número de linhas: "))
            colunas = int(input("Número de colunas: "))
            matriz = cria_matriz.cria(linhas, colunas)

            mult = int(input("Digite o multiplicador: "))

            result = multiplicaMatrizes.matrizConstante(matriz, mult)

            print("\nA matriz resultante é: \n")
            for i in range(linhas):
                print("\t", result[i])      
                    
            print()

        print("Para proseguir escolha uma das opções: ")
        print("1) Impressão de uma simples matriz")
        print("2) Soma de duas matrizes")
        print("3) Multiplicação de duas matrizes")
        print("4) Multiplicação de matriz por constante")
        print("5) Digite qualquer outro número para sair do programa")
        modo = int(input())    

if __name__ == '__main__':
    main()