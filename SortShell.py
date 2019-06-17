for _ in range(int(input())):
    x=[int(i) for i in input().split()]

    def shellsort(x):
        n=len(x)
        gap=n//2

        while gap >0:
            for i in range(gap,n):
                temp = x[i]
                j=i

                while j>=gap and x[j-gap]>temp:
                    x[j] = x[j-gap]
                    j-=gap
                x[j] = temp
            gap//=2
                    



    shellsort(x)
    print("Sorted Array",x)
