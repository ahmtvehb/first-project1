def fakto(n):
    if (n<0):
    elif (n==0):
        return 1
    else:
        return n*fakto(n-1)
n = int(input("enter number n="))
print(fakto(n))