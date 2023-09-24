n = int(input())
for i in range(n):
    if i == 0:
        print("*")
    elif i == n-1:
        print("*"*n)
    else:
        print("*"+" "*(i-1)+"*")


for i in range(n):
    if i==0:
        print(" "*(n-1)+"*")
    elif i==n-1:
        print("*"*(n))
    else:
        print(" "*(n-i-1)+"*"+" "*(i-1)+"*")