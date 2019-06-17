def bsearch(a,key):
    start=0
    end=len(a)-1
    while(start<=end):
        mid=int((start+end)/2)
        if a[mid]==key:
            return mid           
        elif a[mid]>key:
            end=mid-1        
        elif a[mid]<key:
            start=mid+1
            
a=[]
x=int(input("Enter the number of elements you wish to enter:"))
a=list(map(int,input().split()))[0:x]
a.sort()
print(a)    
key=int(input("Enter the number you wish to search:"))
index=bsearch(a,key)
if index!=None:
    print("Element Found at index:",index,",position:",index+1)
else:
    print("Not found")
