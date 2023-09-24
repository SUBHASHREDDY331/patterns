n = int(input())
for i in range(n-2):
    if i==0 or i==n-3:
        print("*  "*n)
    else:
        print("*  "+"   "*(n-2)+"*" )