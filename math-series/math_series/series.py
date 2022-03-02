def fibR(n):
  try:

   if n==1 or n==2:
     return 1
   else:
     return fibR(n-1)+fibR(n-2)
  except:
    print("something wrong")

print(fibR(7))

def lucas(n):
  try:
    if n==0:
        return 2
    elif n==1:
        return 1
    else :
       return lucas(n-1)+lucas(n-2)  
  except:
     print(" wrong")
print(lucas(7))    