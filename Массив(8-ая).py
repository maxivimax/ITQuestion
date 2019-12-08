import random
min = 101
max = -101
n = 5
a = [[random.randint(-100,100) for j in range(n)] for i in range(n)]
for i in range(n):
    for j in range(n):
        print("{:4d}".format(a[i][j]), end="")
    print()

for i in range(n):
    for j in range(n):
        if (i>j or i==j) and a[i][j]<min:
            min=a[i][j]

for i in range(n):
    for j in range(n):
        if (i+j<n+1 or i+j==n+1) and a[i][j]>max:
            max=a[i][j]

for i in range(n):
    for j in range(n):
        if (i>j or i==j) and a[i][j]==min:
            print(min)
            print(j+1,',', i+1)

for i in range(n):
    for j in range(n):
        if (i+j<n+1 or i+j==n+1) and a[i][j]==max:
            print(max)
            print(j+1,',', i+1)

for i in range(n):
    for j in range(n):
        if a[i][j]==max:
            a[i][j]=min
        elif a[i][j]==min:
            a[i][j]=max

for i in range(n):
    for j in range(n):
        print("{:4d}".format(a[i][j]), end="")
    print()

