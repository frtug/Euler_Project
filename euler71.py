# Sum Of Prime Numbers in the range

x,y = map(float,input().split())
s = 0
for i in range(2,x):
        c = 0
        for j in range(2,i):
            if i%j == 0:
              c = c+1             
        if c <1:
         #print(i)
         s = s+i
print("\t End\t sum = ",s," y =",y)
'''         
w,m = map(float,input().split())
if w%5==0 and m>w+0.5:
	print("%f"%(m-w-0.5))
else:
	print("%f"%m)
'''
