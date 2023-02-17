
def pattern(n):
    k = n
    for i in range(0,n):
        print(end = (k-i)*" ")
        for j in range(0, i+ 1):
            print("*", end=" ")
        print("\r")


pattern(5)