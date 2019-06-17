for _ in range(int(input("Enter Passes"))):
    l=[int(i) for i in input().split()]

    def bubblesort(l):
        n=len(l)
        for i in range(n):
            swapped=False

            for j in range(n-1-i):

                if l[j] > l[j+1]:
                    l[j] , l[j+1] = l[j+1],l[j]
                    swapped=True
                  
            if swapped==False:
                break
             
    
            
    bubblesort(l)
    print(l)
    
    
