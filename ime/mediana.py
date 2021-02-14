def mediana(L):
    C = L[:]
    C.sort()
    if len(L)%2 != 0:
        m = len(L)//2
        return C[m]
    else:
        m = len(L)//2
        return (C[m-1]+C[m])/2.0