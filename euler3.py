x = int(input("Enter Number"))
sum1 = 0
su = 0
for i in range(x+1):
    sum1 = sum1 + i*i
    su = su + i
print('square sums=',sum1)
sum2 = su*su
print('sum square = ',sum2)
print(sum2 - sum1)


    
