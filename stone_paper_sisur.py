import random
while True:
    user=input("Enter your choice: ")
    computer=random.choice([1,2,3])
    dist={"stone":1, "paper":2, "scissor":3}
    you=dist[user.lower()]
    reDist={1:"stone",2:"paper",3:"scissor"}
    computerStr=reDist[computer]
    if computer==you :
        print("Tye match.")
    else:
        if computer==1 and you==2:
             print(f"Your Win! your choice is {user} and computer's     {computerStr}")
        elif  computer==1 and you==3:
            print(f"You Lose!  your choice is {user} and computer's     {computerStr}")
        elif computer==2 and you==1:
            print(f"Your Lose  your choice is {user} and computer's     {computerStr}")
        elif computer ==2 and you == 3:
            print(f"Your Win!  your choice is {user} and computer's     {computerStr}")
        elif computer==3 and you ==1:
            print(f"You Win  your choice is {user} and computer's   {computerStr}")
        elif computer==3 and you == 2:
            print(f"You lose  your choice is {user} and computer's  {computerStr}")
