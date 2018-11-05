def pallen(k):
        sum=0
        p = k
        while k>0:
            r = k%10
            sum = sum*10 + r
            k = k//10
        if p == sum:
          return True
        else:
          return False
max = 0
for i in range(100,1000):
    for j in range(100,1000):
        product = i*j
        if pallen(product):
            if product > max:
              max = product
print(max)
print("end")
        

