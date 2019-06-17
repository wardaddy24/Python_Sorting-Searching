for _ in range(int(input())):
    l=[int(i) for i in input().split()]

    def countsort(l,exp):
        n=len(l)
        count=[0]*(10)
        for i in range(0,n):
            index=(l[i]//exp)
            count[index%10]+=1

        for i in range(1,10):
            count[i]+=count[i-1]

        output =[0]*n

        i=n-1
        while i>=0:
            index = l[i]//exp
            output[count[(index)%10]-1] = l[i]
            count[(index)%10]-=1
            i-=1

        i=0
        for i in range(len(l)):
            l[i]=output[i]
               



    def radixsort(l):
        max1=max(l)
        exp=1
        
        while max1/exp > 0:
            countsort(l,exp)
            exp*=10
            

    radixsort(l)
    print(l)
