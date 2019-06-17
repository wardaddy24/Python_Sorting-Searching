for _ in range(int(input())):

    def insertionsort(l):

        for i in range(1 , len(l)):

            key = l[i]
            j=i-1

            while j>=0 and key < l[j]:
                l[j+1] = l[j]
                j-=1

            l[j+1] = key

    l=[int(i) for i in input().split()]

    insertionsort(l)
    print("Sorted List",l)
            
                  
