#S3 Opt3 Stefan Yuzhao Heng
x = 0b101

def testBit(field,bit):
    mask = 1 << bit
    # field = mask & field
    return (mask & field)>>bit 

def setBit(field,bit):
    mask = 1 << bit
    return mask | field


def clearBit(field,bit):
    mask = ~(1 << bit)
    return mask & field

def toggleBit(field,bit):
    mask = 1 << bit
    return mask ^ field

print(testBit(x,0))
print(setBit(x,1))
print(clearBit(x,2))
print(toggleBit(x,3))

