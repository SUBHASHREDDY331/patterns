n = int(input())
for i in range(1,n+1):
    print(" "*(n-i)+"*"*i)

for i in range(n):
    for k in range(1,n-i):
        print(" ",end='')
    for j in range(i+1):
        print("*",end='')
    print()
        