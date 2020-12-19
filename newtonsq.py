num =int(input("enter a number"))
def newtonsq(num):
    a=num
    b=num
    for i in range (num):
      a=(a+b/a)/2
      print(a)
newtonsq(num)        
