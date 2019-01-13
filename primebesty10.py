x = input('Enter the Number')
x = int(x)
sum = 0
prime = [True for i in range(x+1)]
p = 2
while p*p <= x:
    if prime[p] == True:
        for i in range(p*p,x+1,p):
            prime[i] = False
    p += 1
for p in range(2,x):
    if prime[p]:
        sum =sum + p
print(sum)
