MINA  = -1
 
def contaMinas(campo, lin, col):
    m = len(campo)
    n = len(campo[0])
    minas = 0
    for i in range(lin-1,lin+2):
        for j in range(col-1,col+2):
            if i >= 0 and i < m and j >= 0 and j < n:
                if i != lin or j != col:   #para desconsiderar a posição central (lin,col)
                    if campo[i][j] == MINA:
                        minas += 1
    return minas