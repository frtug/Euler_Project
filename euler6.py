import time
start = time.time()

for i in range(1,1000):
    for j in range(1,1000):
        l = 1000 - i - j
        if j > i:
          
           break
        if i**2 + j**2 == l**2:
            print(i , j ,l)
            print("Product: {}".format(i*j*l))
print(time.time()-start)
