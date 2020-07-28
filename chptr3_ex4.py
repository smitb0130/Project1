print("This is a program to calculate indivdual sum of a number")
x=input("Enter a number more than one digit: ")
n=len(x)
sum=0
i=0
while i<=(n-1):
    sum=int(sum)+int(x[i])
    i+=1
print(sum)


