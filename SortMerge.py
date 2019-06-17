for _ in range(int(input("Enter number of runs: "))):
    l=list(map(int,input("Enter list: ").split()))

    def mergesort(l):
        if len(l)>1:
            mid=len(l)//2

            left=l[:mid]
            right=l[mid:]
            
            mergesort(left)
            mergesort(right)


            i=0
            j=0
            k=0

            while i<len(left) and j<len(right):
                if left[i]<=right[j]:
                    l[k]=left[i]
                    i+=1
                else:
                    l[k]=right[j]
                    j+=1
                k+=1

            while i<len(left):
                l[k]=left[i]
                i+=1
                k+=1

            while j<len(right):
                l[k]=right[j]
                j+=1
                k+=1

            

    mergesort(l)
    print("Sorted list",l)
