# d1 = int(input("Dia: "))
# m1 = int(input("Mês: "))
# a1 = int(input("Ano: "))
# 
# d2 = int(input("Dia: "))
# m2 = int(input("Mês: "))
# a2 = int(input("Ano: "))
# 
# if a1 > a2:
#     print("Data 1 é maior")
# elif a1 == a2:
#     if m1 > m2:
#         print("Data 1 é maior")
#     elif m1 == m2:
#         if d1 > d2:
#             print("Data 1 é maior")
#         elif d1 == d2:
#             print("As datas são iguais")
#         else:
#             print("Data 2 é maior")
#     else:
#         print("Data 2 é maior")
# else:
#     print("Data 2 é maior")

# Primeira data.
d1 = int(input("Dia: "))
m1 = int(input("Mês: "))
a1 = int(input("Ano: "))
# Segunda data.
d2 = int(input("Dia: "))
m2 = int(input("Mês: "))
a2 = int(input("Ano: "))
 
if a1>a2 or (a1==a2 and m1>m2) or (a1==a2 and m1==m2 and d1>d2):
     print("Data1 é maior!")
elif a1==a2 and m1==m2 and d1==d2:
     print("Datas são iguais!")
else:
     print("Data2 é maior!")