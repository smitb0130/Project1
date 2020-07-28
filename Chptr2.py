#print("*****This is second chapter*****")
#first_name="Smit"
#second_name="Bhenjaliya"
#full_name=first_name+" "+second_name
#print(  full_name)
#name= input("What is  your name ")
#print("My name is "+name)
#firstName=input("Enter your first name: ")
#secondName=input("Enter your Last Name: ")
#fullName=firstName+" "+secondName
#print("Your first name is:" +firstName +"\n Your Surname is: "+secondName)
#print("Your full name is "+fullName )
#numberOne=int(input("Enter first number: "))
#numberTwo=int(input("Enter second number: "))
#total= int(numberOne+numberTwo)
#print("The total is "+ str(total))
#name,age="smit",18
#print("hello" + name + "Your age is" +str(age))
#name,age=input("Enter your name and age").split(",")
#print(name +"\n"+age)
#print(f"Hello {name} your age is {age}")
#print("*****The End*****")
#lang="python"
#print(lang[])
#name="hiiiiiiiiii"
#print(name.count("i"))
#name="     Smit     "
#surname="Bhenjaliya"
#print(surname+" "+ name.rstrip().lstrip())
#name="Smit_P_Bhenjaliya"
#length=len(name)
#first_i=name.find("i")
#second_i_pos=name.find("i",first_i+1)
#print(f" The length of the name {length} and is found on {second_i_pos} position ")
#Question: Ask the user for an input of the name and add two asterisk in the start of the name and two asterik in the end of the name
name =input("Enter your name: ")
print(name.center(len(name)+4,"*"))