for _ in range(int(input("Enter Passes"))):

    l=list(map(int,input("Enter list:").split()))

    def heapify(l,n,i):
        largest=i
        left = 2*i + 1
        r = 2*i + 2
        if left<n and l[i]<l[left]:
            largest=left

        if r<n and l[largest]<l[r]:
            largest=r

        if largest!=i:
            l[i],l[largest]=l[largest],l[i]
            heapify(l,n,largest)


    def heapsort(l):
        n=len(l)
        #t=n//2
        for i in range(n//2,-1,-1):
            heapify(l,n,i)


        for i in range(n-1,0,-1):
            l[i],l[0] = l[0] ,l[i]
            heapify(l,i,0)



    heapsort(l)
    print("Sorted list",l)
