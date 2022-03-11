def fibR(n):  # 0, 1, 1, 2, 3, 5, 8, 13, ...
   """
  Fibonanci function that give the value of an element in fibonanci series .

  Input n -> integer 
  Output :Integer value (the value of the nth number in fibonanci series)

   """
   if n==0 or n==1:
     return n
   
   elif n >=2 :
     return fibR(n-1)+fibR(n-2)
   else :
     return False


def lucas(n):  #2, 1, 3, 4, 7, 11, 18, 29, ...
    """
  lucas function that give the value of an element in lucas series .

  Input n -> integer 
  Output :Integer value (the value of the nth number in lucas series)

   """
    if n ==0 :
      return 2
    elif n == 1:
      return 1
    else :
      return lucas(n-2)+lucas(n-1)



def sum_series(n, x=0,y=1):
        """
  sum_series function that give the value of an element in sum_series series each element is result of summation
  of the brevious integer and the last 3rd one.

  Input n -> integer 
  Output :Integer value (the value of the nth number in sum_series )
  """
        if x == 0 and y==1:
            return fibR(n)
        elif x==2 and  y==1:
            return lucas(n)
        else:
          if n==0:
            return 0
          elif n==1:
             return 1
          elif n==2:
            return 3
          else:
            return sum_series(n-1) + sum_series(n-3)     
print(sum_series(4,4,6))


     
  
 



 