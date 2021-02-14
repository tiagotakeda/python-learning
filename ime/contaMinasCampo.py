MINA  = -1
 
def contaMinasCampo(campo):
    m = len(campo)
    n = len(campo[0])
    for i in range(m):
        for j in range(n):
            if campo[i][j] != MINA:
                campo[i][j] = contaMinas(campo, i, j)
