import time

start = time.time()

x = int(input("enter the number"))
sum = 0

for i in range(2,x):
    c =0
    for j in range(2,i):
        if i%j == 0:
            c = c+1
    if c < 1:
        #print(i)
        sum = sum +i
elapsed = time.time() - start
print("Time elapsed: {}".format(elapsed))
print(sum)       
    
