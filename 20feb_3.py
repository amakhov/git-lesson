list = [1, 2, 3, 8, 14, 89, 45, 6, 16, 77]
print (list)
n=len(list)
m=n-1
while m>0:
    for i in range(m):
        if (list[i]>list[i+1]):
            x=list[i]
            list[i]=list[i+1]
            list[i+1]=x
    m=m-1
print(list)
