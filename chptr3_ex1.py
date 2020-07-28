a=3010
x=int(input("Enter the password: "))
if x!=a:
    print("*****Access Denied*****")
else:
    print("*****Enter the game!!*****")
    import random
    n=random.randint(1,50)
    guess_num=int(input("Enter Any number between 1 to 50: "))
    if guess_num==n:
        print("You are a winner: ")
    else:
        if guess_num>=n:
            print(f"TOOO highhhh\nWrong number!!!!!!\n Better luck next time!!\n The Correct number was {n}")
        else:
            print(f"TOOO lowwww\n Wrong Number!!!!!!\nBetter Luck next time !!!!\n The Correct number was {n}")


