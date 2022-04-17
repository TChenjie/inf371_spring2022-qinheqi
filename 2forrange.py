import random
num=[]
for i in range(0,10):
    num.append(random.getrandbits(4))
for i in range(0,10):
    print (num[i])