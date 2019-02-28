def myrev(a):
    s = []
    for i in range(len(a)):
        temp = a.pop()
        s.append(temp)
    print(s)

myrev([1,2,3,4])
