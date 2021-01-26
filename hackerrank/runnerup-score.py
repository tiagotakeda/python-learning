if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    maior = arr[0]
    runnerup = arr[1]

    if maior < runnerup:
        temp = runnerup
        runnerup = maior
        maior = temp
    
    for i in range(2, n):     
        if(arr[i] > maior):
            runnerup = maior
            maior = arr[i]
        
        if(arr[i] < maior):
            if(runnerup >= maior):
                runnerup = arr[i]

        for k in range(2, n): 
            if(arr[k] >= runnerup):
                if(arr[k] < maior):
                    runnerup = arr[k]

    print(runnerup)