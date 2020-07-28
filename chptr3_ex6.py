print("New modified game****")
import random
n=random.randint(1,50)
guess=1

x=int(input("Guess any number between 1 to 50: "))
for a in range(1,50):
    if x==n:
        print(f"Congratulations You win!! and you guessed the number {guess} times ")
        break
    elif x>n:
        print("Too High!!")
        x=int(input("Guess again: "))
        guess+=1
        continue
    else:
        print("Too loww!!")
        x=int(input("Guess again: "))
        guess+=1
        continue
    
