if __name__ == '__main__':
    arr = list(map(int, input().split()))

    maior = arr[0]
    runnerup = arr[1]
    
    for i in range(len(arr)-2):
        if(arr[i+2] > maior):
            runnerup = maior
            maior = arr[i+2]
        
        if(arr[i+2] < maior):
            if(runnerup >= maior):
                runnerup = arr[i+2]

        print("runnerup =", runnerup)

        for k in range(len(arr)-2): 
            if(arr[k+2] >= runnerup):
                if(arr[k+2] < maior):
                    runnerup = arr[k+2]

    print(runnerup)