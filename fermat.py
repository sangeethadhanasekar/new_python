"""Program to find whether Fermat theorem  was right or wrong!"""
def check_fermat(a,b,c,n):
    if (n>2):
        a=a**n
        b=b**n
        c=c**n
        if  a+b==c:
  
            print("holy smokes,fermat was wrong")
        else:
            print("no,that doesn't work")

def prompt_user():
    a=int(input("enter the number a:"))
    b=int(input("enter the number b:"))
    c=int(input("enter the number c:"))
    n=int(input("enter the power"))
    check_fermat(a,b,c,n)
    
prompt_user()
