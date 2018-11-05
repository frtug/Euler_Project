s = 0
for x in range(2,100000000000000000000000):
  c =0 
  for i in range(2,x):
    if x%i == 0:
      c = c+1
  if c > 0:
    continue
  else:
     s = s+1
     if s == 10001:   
        break
print(x)
         
