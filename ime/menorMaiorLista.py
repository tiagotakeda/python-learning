def menorMaiorLista(lista):
    maior = lista[0]
    menor = lista[0]
    for x in lista:
        if x > maior:
            maior = x
        elif x < menor:
            menor = x
    return menor, maior

def main():
    print("Entre com a lista: (separando os elementos por espaços)")
    lista = list(map(int, input().split()))
    
    m, M = menorMaiorLista(lista)
    print("menor =", m, " maior =", M)

if __name__ == "__main__":
    main()