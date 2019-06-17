import random

for _ in range(int(input("Enter Number of Test Sorts:"))):

    l=list(map(int,input("Enter list").split()))

                                        #This is the implementation of partition function for end element as pivot
    
    '''def partition(l,start,end):
        pivot=l[end]
        i=start-1

        for j in range(start,end):
            if l[j]<=pivot:
                i=i+1
                l[i],l[j]=l[j],l[i]
        l[i+1],l[end]=l[end],l[i+1]
        return i+1'''

                                        #This is the implementation for random QuickSort

    '''def randompartition(l,start,end):
        r=random.randint(start,end)
        l[r],l[end]=l[end],l[r]
        return partition(l,start,end)'''

                                        #This is the implementation of partition function for start element as pivot

    def partition(l,start,end):
        pivot=l[start]
        i=start

        for j in range(start+1,end):
            if l[j]<=pivot:
                i=i+1
                l[i],l[j]=l[j],l[i]
        l[i],l[start]=l[start],l[i]
        return i
            

    def Quicksort(l,start,end):
        if start < end:
            #p=randompartition(l,start,end)

            p=partition(l,start,end)
            Quicksort(l,start,p-1)
            Quicksort(l,p+1,end)

    Quicksort(l,0,len(l))                           #This is for start element as pivot
    
    #Quicksort(l,0,len(l)-1)                        #This is for end element as pivot
    
    print("Sorted Array is",l)


    

            
            
           
    
