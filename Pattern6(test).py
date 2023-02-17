
def pattern(n):
    for i in range(1,n):

        if i%2 == 0:
            for j in range(1,i):
                print("*", end=" ")
            print("\r")

        else:
            for j in range(1, i):
                print(j, end=" ")
            print("\r")

pattern(8)