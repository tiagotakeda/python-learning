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

def main():
    print("CRIE A SUA MATRIZ AQUI")
    linhas = int(input("Número de linhas: "))
    colunas = int(input("Número de colunas: "))
    matriz = cria_matriz(linhas, colunas)

    print("\nA matriz gerada foi: \n")
    for i in range(linhas):
        print("\t", matriz[i])      
            
    print()

main()