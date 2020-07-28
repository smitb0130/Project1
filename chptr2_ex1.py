print("*****This is a program of Chapter 2 Excercise 1*****")
print("*****Input NOT in one line*****")
firstNum=int(input("Enter the first number:"))
secondNum=int(input("Enter the second number:"))
thirdNum=int(input("Enter the third number:"))
sum=firstNum+secondNum+thirdNum
average=sum/3.0
print("Sum:" + str(sum) + "\nAverage:" + str(average))
print("The sum is {} and the average is {} ".format(sum,average))
print("*****Input IN one line*****")
f1,f2,f3=input("Enter three numbers: ").split(",")
s=int(f1)+int(f2)+int(f3)
avg=s/3.0
print(f"The sum is {s} and the average is {avg}")
