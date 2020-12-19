"""program to check whether the given year is a leap year or not""" 
year=int(input("Enter the year:"))
if year%4==0  or year%400==0 or year%100!=0:
        output= "the year {years} is a leap year".format(years=year)
        print(output)
        
elif year:
        print("the year {years} is not a leap year".format(years=year))
