def bubbleSort(seq):
  n = len(seq)
  for i in range(n-1, 0, -1):
    for j in range(0,i):
      if seq[j] > seq[j+1]:
        troca(seq, j, j+1)