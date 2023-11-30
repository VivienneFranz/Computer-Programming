def user_hp_distance(start):
    HP = 100
    invintory = 0


user_input1 = input("Greatings! This is the very start do your adventure. If you are ready to start please type your name.")
print(f'Nice you meet you {user_input1}!' )

user_input2 = input(" To continue on your adventure press w to walk or i to veiw HP and invintory.' ")


if user_input2 == "w":
    print("You have walked 1 mile. press w to contunie walking or press i to veiw HP and Invintory. ")
elif user_input2 == "i":
    print(f"You have 100 and nothing in your invintory. press w to contunie walking or press i to veiw HP and Invintory. ")
else:
    print("Invalid input please type w or i ")

import random 

mylist = [1,2,3,4,5]

n = random.choice(mylist)

for i in range(5):
    if i > 3:
        print(f" {user_input1} You have run into a snake choose to fight f or run r.")
    else: 
        print(f" {user_input1} You have walked 1 mile. press w to contunie walking or press i to veiw HP and Invintory. ")

if user_input2 == 'f':
    print("You have choosen to fight snake you attacked the snake and did 50 damage, the snake did 75 on you. ")
elif user_input2 == 'r':
    print("You have choosen to run and escaped!")
