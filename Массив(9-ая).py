import random
n = 5
s = 0
z = 0
min1=101
min2=101
a = []
b = []
c = []
x = [[random.randint(-100,100) for j in range(n)] for i in range(n)]
for i in range(n):
    for j in range(n):
        print("{:4d}".format(x[i][j]), end="")
    print()
for i in range(n):
    for j in range(n):
        if x[i][j]%2==0:
            a +=[x[i][j]]
            s=s+1
        else:
            b+=[x[i][j]]
            z=z+1
print (a)
print (b)
list.sort(a)
c = sorted(b)
print (a)
print (c)

