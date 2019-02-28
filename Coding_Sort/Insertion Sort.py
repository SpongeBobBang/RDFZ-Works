#S3 Opt3 Stefan Yuzhao Heng
x = [53,21,60,18,42,19]

y = [0 for i in range(6)]
y[0] = x[0]
for i in range(1,len(y)):
    newItem = x[i]
    currP = i-1
    while y[currP] > newItem and currP >= 0:
        y[currP+1] = y[currP]
        currP = currP -1
    y[currP+1] = newItem

print(y)
