
def pattern(n):
    k = n
    for i in range(-n,0):
        print(end =(k+i)*" ")
        for j in range(0,-i):
            print("*", end=" ")
        print("\r")


pattern(10)
