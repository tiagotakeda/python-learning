def cria(nLinhas, nColunas):
    matriz = []
    valor = 0

    constante = input("A matriz é de valores constantes / homogênea? (Sim ou Não): ")
    if(constante == "Sim" or constante == "S" or constante == "s" or constante == "sim"):
        nula = input("É uma matriz nula? (Sim o Não): ")

        if(nula == "Sim" or nula == "sim" or nula == "s" or nula == "sim"):           
            for i in range(nLinhas):
                linhas = []
                for j in range(nColunas):
                    linhas.append(valor)
                matriz.append(linhas)
        else:
            valor = input("Digite o valor dos elementos: ")
            for i in range(nLinhas):
                linhas = []
                for j in range(nColunas):
                    linhas.append(valor)
                matriz.append(linhas)
    else:
        for i in range(nLinhas):
            linhas = []
            for j in range(nColunas):
                print("Digite A[", i, "][", j, "]: ", sep="", end="")
                valor = int(input())
                linhas.append(valor)
            matriz.append(linhas)
    
    return matriz

if __name__ == '__main__':
    import sys
    cria(int(sys.argv[1], sys.argv[2]))