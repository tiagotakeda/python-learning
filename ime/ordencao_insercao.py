def ordenacao_insercao(seq):
  n = len(seq)
  for i in range(0,n-1):
    # Insere seq[i+1] em seq[0],...,seq[i].
    x = seq[i+1]
    j = i
    while j >= 0 and seq[j] > x:
      seq[j+1] = seq[j]
      j -= 1
    seq[j+1] = x