def feb(n):
    a=0
    b=1
    if n==1:
        print(a)
    else:
        print(a)
        print(b)
        k=0
        for i in range(2,n):
            k=a+b
            a=b
            b=k
            print(k)
feb(5)
