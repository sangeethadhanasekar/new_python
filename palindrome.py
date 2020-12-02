print("***program_to_find_a_number_as_palindrome_or_not***")
a=input("enter a number: ")
for i in a :
   reverse=a[::-1]
if reverse==a:
    print("the given number",a,"is a palindrome")
else:    
    print("the given number",a,"is not a palindrome")
