#S3 Opt3 Stefan Yuzhao Heng
x = [53,21,60,18,42,19]

for p in range(1,len(x)):
    iti = x[p]
    ci = p - 1
    while x[ci] > iti and ci >= 0:
        x[ci+1] = x[ci]
        ci = ci - 1
    x[ci+1] = iti

print(x)
