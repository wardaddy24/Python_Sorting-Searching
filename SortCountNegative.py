for _ in range(int(input("Enter number of runs: "))):
    l=list(map(int,input("Enter list: ").split()))

    def countsort(l):

        mini =  min(l)
        if mini<0:
            t=mini*(-1)
            for i in range(len(l)):
                l[i]=l[i]+t
                
                
        maxi= max(l)
        
        count = [0 for i in range(maxi+1)]

        

        for i in range(len(l)):
            count[l[i]]+=1

        count[0]=count[0]-1
               

        for i in range(1,maxi+1):
            count[i]+=count[i-1]

        output = [None]*len(l)


        for i in range(len(l)-1,-1,-1):
            output[count[l[i]]]= l[i]
            count[l[i]]-=1

        if mini<0:
            for i in range(len(output)):
                output[i]=output[i]+mini
                
        print(output)


    countsort(l)
            
            
