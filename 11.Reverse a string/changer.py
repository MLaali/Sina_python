def changer(a):
 b=0
 f=0
 while a/10<=0:
  b=b+1
 for c in range (1,b+2):
  d=a/10**c
  e=d**c
  f=e+f
 return f*10
print(changer(123))
