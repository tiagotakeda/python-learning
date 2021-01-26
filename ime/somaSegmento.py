def somasegmento(ini,fim,L):
    soma = 0.0
    i = ini
    while i < fim:
        soma += L[i]
        i += 1
    return soma

# def somasegmento(ini,fim,L):
#     soma = 0.0
#     for i in range(ini, fim):
#         soma += L[i]
#     return soma
 
def main():
    n = int(input("Digite n: "))

    # lista = []
    # for i in range(n):
    #     num = float(input("Digite num: "))
    #     lista.append(num)

    lista = list(map(int, input().split()))    
 
    smax = lista[0]
    imax,fmax = 0,1
    for i in range(n):
        for f in range(i+1,n+1):
            s = somasegmento(i,f,lista)
            if s > smax:
                smax = s
                imax = i
                fmax = f
 
    print("Soma máxima =",lista[imax],end=" ")
    for i in range(imax+1,fmax):
        if(lista[i] < 0.0):
            print(lista[i],end=" ")
        else:
            print("+",lista[i],end=" ")
    print("=",smax)
 
main()