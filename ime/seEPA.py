n = int(input("Digite n: "))

a1 = int(input("Digite um num: "))
i = 1
if n > 1:
    a2 = int(input("Digite um num: "))
    i = 2
    r = a2 - a1 #razao da PA
    ant = a2

pa = True
while i < n:
    ai = int(input("Digite um num: "))
    if ai - ant != r:
        pa = False
    ant = ai
    i += 1

if pa and n > 1:
    print("A sequencia é uma P.A. de razão", r)
elif pa:
    print("A sequência é uma P.A.")
else:
    print("A sequência não é uma P.A")