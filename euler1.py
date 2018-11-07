# First problem of Euler Project...............
def cal():
    x = int(input("enter the last value"))
    y = int(input("enter the first value"))
    c =0
    sum =0
    for i in range(y,x):
        if i%3 == 0 or i%5==0:
            print(i,end=" ")
            c = c+1
            sum = sum + i
        else:
            continue
    print("Count"+str(c))
    print("sum is",sum)
    
#call this function 
#//////////////////////////////////////////////////////////////
    
# 2nd Problem  Even Fibnocii Series 
def fib():
    x = int(input('enter the last number'))
    a = 0
    b = 1
    sum = 0  # Sum of the fibnocii of even number
    z = a +b
    while z < x:
        
        if z%2 == 0:
            sum = sum + z           
        a = b
        b = z
        z = a +b
    print(sum)
        
        
