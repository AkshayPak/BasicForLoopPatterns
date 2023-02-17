

def pattern(n):
    k = n
    for i in range(0,n+1):
        for j in range(0,i):
            print("*", end=" ")
        print("\r")
    for i in range(-(n-1),0):
        for j in range(i,0):
            print("*", end=" ")
        print("\r")

pattern(5)