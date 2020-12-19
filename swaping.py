print("'program to swap TWO numbers'")
num1=369
num2=30
print("num1 before swaping:",num1)
print("num2 before swaping:",num2)
def with_variable(num1,num2):
      temp=num1
      numaf1=num2
      numaf2=temp
      print("\n*******   using temporary variable   *******")
      print("num1 after swaping:",numaf1)
      print("num2 after swaping:",numaf2)
def with_operator(num1,num2):
    num1=num1+num2
    num2=num1-num2
    num1=num1-num2
    print("\n*******   using arithmetic operator   *******")
    print("num1 after swaping:",num1)
    print("num2 after swaping:",num2)
def another_method(num1,num2):
    print("\n------------- OTHER METHOD TO SWAP--------------")
    num1=num1^num2
    num2=num1^num2
    num1=num1^num2
    print("\n*******   using bitwise XOR   *******")
    print("num1 after swaping:",num1)
    print("num2 after swaping:",num2)
with_variable(num1,num2)
with_operator(num1,num2)
another_method(num1,num2)
