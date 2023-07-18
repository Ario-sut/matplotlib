import matplotlib.pyplot as plt
import random

my_dict = {"R": "Rock", "P":"Paper", "S":"Scissor"}

#Initialize
user_count=0
comp_count=0

games = int(input("\nenter the number of games you want = "))

while games>0:
    games-=1
    flag=0

    userInput= input("\nUser's Input : ")[0]
    userInput= userInput.upper()

    for i in my_dict.keys():
        if userInput==i:
            flag=1
    if flag!=1:
        print("INVALID INPUT")
        continue

    compInput = random.choice(list(my_dict.keys()))

    print("Computer's input : ", my_dict[compInput])

    if((userInput=="R" and compInput == "P")or (userInput=="P" and compInput == "S") or (userInput=="S" and compInput == "R")):
        comp_count+=1
    elif((compInput=="R" and userInput == "P")or (compInput=="P" and userInput == "S") or (compInput=="S" and userInput == "R")):
        user_count+=1
    else:
        print("TIE")

    print("\nScore : ")
    print("User Score : ", user_count, "\tComp Score : ", comp_count, "\n")

print("\n\tFinal Score : ")
print("User Score : ", user_count, "\t\t\tComp Score : ", comp_count, "\n")

if user_count>comp_count:
    print("\n\tCongrats! You Won")
    player= "the winner is You"
elif user_count<comp_count:
    print("\n\t\tSorry! Try Again")
    player= "the winner is the Computer"
else:
    print("\n\t\tOOPS! TIE")
    player= "It's Tie"

plt.title(f"The Final Score, {player}")

x = ["Player", "Computer"]
y= [user_count, comp_count]

plt.plot(x, y)
plt.ylabel('Win Amount')

plt.show()