choice=int(input("how many elements do you want in a list"))
list1=[]
for i in range(choice):
   inp=input("enter the elements in the list")
   list1.append(inp)
print("the given list is",list1)   
print("enter index 'n' ranges from 0 to",len(list1)-1)     
n=int(input()) 
revlist=list1[n:]+list1[:n]

print("given list:",list1)   
print("circulated list:",revlist)
