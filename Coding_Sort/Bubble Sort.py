# S3 Opt3 Stefan Yuzhao Heng
x = [2,5,3,4,1]

n = len(x)-1
for i in range (n):
    for j in range (n):
        if x[j] > x[j+1]:
            temp = x[j]
            x[j] = x[j+1]
            x[j+1] = temp
    n = n-1

print(x)
