#Develop a program that prompts the user to enter their current temperature in Celsius and 
#prints out whether they should wear a jacket (if temperature is below 20°C) or not

tem=int(input("enter the calsius temperature: "))

if tem<20:
    print("wear a jacket")
else:
    print("not wear a jacket")