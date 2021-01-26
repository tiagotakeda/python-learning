# entrada
print("Cálculo dos n primeiros múltiplos de i ou de j")
n = int(input("Digite n: "))
i = int(input("Digite i: "))
j = int(input("Digite j: "))

cont = 0
candidatoM = 0
while cont < n:
    if candidatoM%i == 0 or candidatoM%j == 0:
        print(candidatoM)
        cont += 1
    candidatoM += 1