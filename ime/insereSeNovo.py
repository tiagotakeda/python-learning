def insereSeNovo(x, lista):
    i = 0
    achou = False
    while i < len(lista) and not achou:
        if lista[i] == x:
            achou = True
            ind = i
        i += 1
    if not achou:
        lista.append(x)
        ind = len(lista)-1
    return ind

def main():
    lista = list(map(int, input().split()))
    contadores = []
    for i in range(len(lista)):
        num = int(input("Digite num: "))
        ind = insereSeNovo(num, lista)
        if ind >= len(contadores):
            contadores.append(0)
        contadores[ind] += 1

    for i in range(len(lista)):
        print("%.2f aparece %d vezes"%(lista[i], contadores[i]))

if __name__ == "__main__":
    main()