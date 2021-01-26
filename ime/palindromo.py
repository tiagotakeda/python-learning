# Escreva uma função que recebe um número inteiro e retorna uma lista 
# contendo os seus dígitos. Os dígitos podem estar em ordem reversa.

def listaDeDigitos(n):
    lista = []
    while n > 0:
        dig = n%10
        lista.append(dig)
        n = n//10
    return lista
 
# Escreva uma função que recebe uma lista e retorna uma lista contendo 
# os seus elementos em ordem reversa.
 
def ordemReversa(lista):
    inv = []
    i = len(lista)-1
    while i >= 0:
        inv.append(lista[i])
        i -= 1
    return inv
 
# Escreva uma função que recebe 2 listas (l1 e l2) e devolve True caso:
# - l1 e l2 tem o mesmo tamanho e
# - os elementos de l1 e l2 são todos iguais e na mesma ordem.
# Caso contrário, a função deve devolver False.

def iguais(l1, l2):
    if len(l1) != len(l2):
        return False
    i = 0
    while i < len(l1):
        if l1[i] != l2[i]:
            return False
        i += 1
    return True
 
# Escreva um programa que leia um número inteiro n > 0 e determina se ele é ou 
# não palíndromo usando as funções anteriores. Um número inteiro é palíndromo se 
# ele possui a mesma sequência de dígitos quando lido tanto da direita para a 
# esquerda como da esquerda para a direita.

def main():
    n = int(input("Digite n: "))
 
    lista = listaDeDigitos(n)
    inv = ordemReversa(lista)
 
    if iguais(lista, inv):
        print(n,"é palíndromo")
    else:
        print(n,"não é palíndromo")
 
main()