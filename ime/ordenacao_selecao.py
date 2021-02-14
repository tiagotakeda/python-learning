def indice_maior(seq, n):
  imax = 0
  for i in range(1,n):
    if seq[i] > seq[imax]:
      imax = i
  return imax

def troca(seq, i, j):
  tmp = seq[i]   #Guarda cópia de backup do valor L[i] em tmp.
  seq[i] = seq[j]
  seq[j] = tmp

def ordenacao_selecao(seq):
  """Ordenação por seleção:
  A cada passo o maior elemento da lista é
  encontrado e colocado na sua posição
  final definitiva. O processo se repete para o
  trecho da lista remanescente."""
  n = len(seq)
  for tam in range(n, 1, -1):
    imax = indice_maior(seq, tam)
    troca(seq, imax, tam-1)

