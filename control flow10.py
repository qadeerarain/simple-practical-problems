#Create a program that simulates a simple ATM machine. It should ask the user for their PIN, 
#verify it, and then allow them to withdraw money if the balance is sufficient.

balance=int(input("enter a balance: "))

if balance>200:
    print("balance is sufficient")
else:
    print("balance is not sufficient")