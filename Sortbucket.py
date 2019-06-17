for _ in range(int(input())):
    

    def insertionsort(l):
        
        for i in range(1 , len(l)):
            key = l[i]
            j=i-1
            while j>=0 and key < l[j]:
                l[j+1] = l[j]
                j-=1

            l[j+1] = key
        return l


    def bucketsort(x):
        arr=[]
        slot=10

        for i in range(slot):
            arr.append([])

        for j in x:
            index = int(slot*j)
            arr[index].append(j)

        for i in range(slot):
            arr[i]=insertionsort(arr[i])
        print(arr)

        k=0
        for i in range(slot):
            for j in range(len(arr[i])):
                x[k]=arr[i][j]
                k+=1
        return x
    

    x=[float(i) for i in input().split()]

    bucketsort(x)

    print("Sorted Array",x)
