for _ in range(int(input())):
    l = [int(i) for i in input().split()]

    n=len(l)
    for i in range(n):

        min_index = i

        for j in range(i+1,n):
            if l[min_index] > l[j]:
                min_index = j

        l[min_index] , l[i] = l[i], l[min_index]

    print(l)
