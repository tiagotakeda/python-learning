# def bubbleSort(seq):
#   n = len(seq)
#   for i in range(n-1, 0, -1):
#     for j in range(0,i):
#       if seq[j] > seq[j+1]:
#         troca(seq, j, j+1)

def troca(seq, i, j):
  tmp = seq[i]   #Guarda cópia de backup do valor L[i] em tmp.
  seq[i] = seq[j]
  seq[j] = tmp

def bubbleSort(seq):
  n = len(seq)
  for i in range(n-1,0,-1):
    houvetroca = False
    for j in range(0,i):
      if seq[j] > seq[j+1]:
        troca(seq, j, j+1)
        houvetroca = True
    if not houvetroca:
      break