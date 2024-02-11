#Implement a program that takes a user's input of a year and month and prints out the number 
#of days in that month, considering leap years

year=int(input("enter a year: "))
month=int(input("enter a mouth: "))

if year%4:
    print("leap year")
else:
    print("not leap year")