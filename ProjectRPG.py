def user_hp_distance(start):
    invintory = 0


user_input1 = input("Greatings! This is the very start do your adventure. If you are ready to start please type your name.")
print(f'Nice you meet you {user_input1}!' )

user_input2 = input(" To continue on your adventure press w to walk or i to veiw HP and invintory.' ")

def user_distance():
    while True:
        if user_input2 == "w":
            print("You have walked 1 mile. press w to contunie walking or press i to veiw HP and Invintory. ")
        elif user_input2 == "i":
            print(f"You have 100 and nothing in your invintory. press w to contunie walking or press i to veiw HP and Invintory. ")
        else:
            print("Invalid input please type w or i ")


import random

player_hp = 100
enemy_hp = 100

def attack_enemy():
    while True:
        if player_hp > 0:
            your_attack = random.randint(10,100)
            print(f"you attacked the enemy for {your_attack} damage!")
            enemy_hp -= your_attack
        
        if enemy_hp > 0:
            enemy_attack = random.randint(10, 100)
            print(f"The enemy attacked you for {enemy_attack} damage!")
            player_hp -= enemy_attack

            if player_hp <= 0:
                print("You died! Better luck in the next world...")
                break
            elif enemy_hp <= 0:
                print("You killed the snake!")
                print("You have earned 30 hp and an item in your inventory!")
                player_hp += 30
                break

import random 

mylist = [1,2,3,4,5]

n = random.choice(mylist)

fight_input = input(" You have come across a Snake! Do you choose to fight? (fight/run) ")
if fight_input == 'fight':
    attack_enemy(player_hp, enemy_hp)
if fight_input == 'run':
    print("You tried running and escaped.")
if player_hp < 0:
    print("You survived and have earned coins. ")
elif player_hp <= 0:
    print("You died! Better luck in the next world...")




mylist = [1,2,3,4,5]

n = random.choice(mylist)

fight_input = input(" You have come across a Goblin! Do you choose to fight? (fight/run) ")
if fight_input == 'fight':
    attack_enemy(player_hp, enemy_hp)
if fight_input == 'run':
    print("You tried running but the golblen caught up to you. you have died.")
elif player_hp <= 0:
    print("You died! Better luck in the next world...")


import random


def attack_enemy():
    while True:
        if player_hp > 0:
            your_attack = random.randint(10,100)
            print(f"you attacked the enemy for {your_attack} damage!")
            enemy_hp -= your_attack
        
        if enemy_hp > 0:
            enemy_attack = random.randint(10, 100)
            print(f"The enemy attacked you for {enemy_attack} damage!")
            player_hp -= enemy_attack

            if player_hp <= 0:
                print("You died! Better luck in the next world...")
                break
            elif enemy_hp <= 0:
                print("You killed the golblin!")
                print("You have earned 15 hp and an item in your inventory!")
                player_hp += 15
                break


mylist = [1,2,3,4,5]

n = random.choice(mylist)

fight_input = input(" You have come across a spider! Do you choose to fight? (fight/run) ")
if fight_input == 'fight':
    attack_enemy(player_hp, enemy_hp)
if user_input2 == 'r':
    print("You have choosen to run and escaped!")
elif player_hp <= 0:
                print("You died!")

import random


def attack_enemy():
    while True:
        if player_hp > 0:
            your_attack = random.randint(10,100)
            print(f"you attacked the enemy for {your_attack} damage!")
            enemy_hp -= your_attack
        
        if enemy_hp > 0:
            enemy_attack = random.randint(10, 100)
            print(f"The enemy attacked you for {enemy_attack} damage!")
            player_hp -= enemy_attack

            if player_hp <= 0:
                print("You died! Better luck in the next world...")
                break
            elif enemy_hp <= 0:
                print("You killed the golblin!")
                print("You have earned 15 hp and an item in your inventory!")
                player_hp += 15
                break

            