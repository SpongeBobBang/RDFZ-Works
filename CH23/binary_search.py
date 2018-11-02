#S3 Opt3 Stefan Yuzhao Heng
x = [12,19,23,27,33,37,41,45,56,59,60,62,71,75,80,84,88,92,99]
si = 37
found = False
fail = False

l = 0
h = len(x)

while found == False and fail == False:
    m = int((l+h)/2)
    print(l,h,m)
    if x[m] == si:
        found = True
    else:
        if l > h: fail = True
        else:
            if x[m] > si:
                h = m-1
            else:
                l = m+1
    print(found,fail)
if found == True:
    print(m,x[m])
else:
    print(-1)
