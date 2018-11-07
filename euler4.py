s = 0
for x in range(3,10000000000000000000000000000):
  c =0 
  for i in range(2,x+1):
    if x%i == 0:
      c = c+1
  if c < 0:
     s = s+1
  if s == 10001:   
       print(x)         
