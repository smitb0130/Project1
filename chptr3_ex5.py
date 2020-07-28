print("Tough Excercise!!!!")
name=input("Enter your name: ")
i=0
temp=""
while i<=(len(name)-1):
    if  name[i] not in temp:
        temp+=name[i]
        print(f"{name[i]} occurs {name.count(name[i])} times")
    
    i+=1

