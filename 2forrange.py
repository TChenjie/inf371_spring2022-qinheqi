import random
num=[]
for i in range(0,10):
    num.append(i)
  
random.shuffle(num)
for i in range(1,10):
    print(num[i]) 