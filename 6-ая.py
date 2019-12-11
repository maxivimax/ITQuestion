n=100
a=[i+1 for i in range(n)]
print(a)
for i in range(len(a)):
    if (a[i]%2!=0 or a[i]==2) and (a[i]%3!=0 or a[i]==3 ) and (a[i]%5!=0 or a[i]==5) and (a[i]%7!=0 or a[i]==7):
        print(a[i])
