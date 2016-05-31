import os
import sys
import time
from random import randint


class itemsClass():
    def __init__(self, value, inventory):
        self.name = name
        self.value = value
class Talisman_of_Truth(itemsClass):
    value = 100
    def add_tali(self):
        player.inventory.append('Talisman_of_Truth')
        player.gold = player.gold - 100
class Charm_of_Capitalism(itemsClass):
    value = 20
    def add_charm(self):
        player.inventory.append('Charm_of_Capitalism')
        player.gold = player.gold - 20
class playerClass:
    def __init__(self, location, health, victory, gold, inventory):
        self.location = location
        self.health = 100
        self.victory = False
        self.gold = 100
        self.inventory = []
    def status(playerClass):
        print('\n' * 100)
        print("player.inventory -",player.inventory,'\n'"Player Health -",player.health,'\n'"Player Gold -",player.gold)
        os.system("pause")

    def death(self):
        if (self.health < 0):
            death()
            print(".")
            time.sleep(0.5)
            print(".")
            time.sleep(0.5)
            print(".")
            time.sleep(0.5)
            print("You died horribly"'\n'"Try again?")
            sys.exit(0)

    def damage(self):
        damageran = (randint(0, 20))
        return damageran


    class actionClass():
        def __init__(self, location):
            self.location = location

        def north(self, location):
            self.location += 2

        def east(self, location):
            self.location += 1

        def south(self, location):
            self.location -= 2

        def west(self, location):
            self.location -= 1


class Main():
     def options(self):
        while True:
           print("\n" * 100)
           print("Available options:"'\n\n'"Travel - Travel to another part of the map"'\n'"Status - Show health and gold"'\n'"Area - Activate area interaction")
           main_input = input()
           if main_input == "Travel":
               if main_input.isalpha():
                   Travel()
                   break
               else:
                   continue
           elif main_input == "Status":
               if main_input.isalpha():
                   playerClass.status(playerClass)
           elif main_input == "Area":
               if main_input.isalpha():
                   Area()
                   break
           else:
               continue
def Travel():
    while player.health > 0 and player.victory == False:
        print("\n" * 100)
        if player.location == 2:
            user_input = input("You are currently at 'the crossroads', where would you like to go?"'\n'"North - Twilight Cave"'\n'"East - Hero's Shop"'\n'"South - Pool of Rejuvenation"'\n'"West - Plains of Grinding"'\n')
            if user_input == "North":
                print("\n" * 100)
                if 'Talisman_of_Truth' in player.inventory:
                    print("You win!"'\n'"Congratulations")
                    os.system("pause")
                    sys.exit(0)
                elif 'Talisman_of_Truth' not in player.inventory:
                    print("The Monster of Doom destroys you in one mighty smack")
                    playerClass.death(player)
                    os.system("pause")
                    sys.exit(0)
                else:
                    sys.exit(0)
            if user_input == "East":
                print("\n" * 100)
                player.actionClass.east(player, 0)
                print("You enter the shop and begin to browse around")
                os.system("pause")
                break
            if user_input == "South":
                print("\n" * 100)
                player.actionClass.south(player, 0)
                print("You enter the Pool of Rejuvination, spirits wait to soothe your pains")
                os.system("pause")
                break
            if user_input == "West":
                print("\n" * 100)
                player.actionClass.west(player, 0)
                print("You walk out into the Plains of Grinding, the monsters in the area are waiting for you to make a move at them")
                os.system("pause")
                break
        elif player.location == 4:
            user_input = input("You are currently at 'Twilight Cave' Win or lose")
            if user_input == "North":
                print("Can't do that")
                continue
            if user_input == "East":
                print("Can't do that")
                continue
            if user_input == "South":
                player.actionClass.south(player, 4)
                print("")
                break
            if user_input == "West":
                print("Can't do that")
                continue
        elif player.location == 3:
            user_input = input("You are currently at the 'Hero's Shop'"'\n'"West - The Crossroads")
            if user_input == "North":
                print("Can't do that")
                continue
            if user_input == "East":
                print("Can't do that")
                continue
            if user_input == "South":
                print("Can't do that")
                continue
            if user_input == "West":
                player.actionClass.west(player, 0)
                print("w")
                break
        elif player.location == 0:
            user_input = input("You are currently at the 'Pool of Regeneration'"'\n'"North - The Crossroads")
            if user_input == "North":
                player.actionClass.north(player, 2)
                print("Back in The Crossroads, where to next?")
                break
            if user_input == "East":
                print("Can't do that")
                continue
            if user_input == "South":
                print("Can't do that")
                continue
            if user_input == "West":
                print("Can't do that")
                continue
        elif player.location == 1:
            user_input = input("You are currently at the 'Plains of Grinding'"'\n'"East - The Crossroads")
            if user_input == "North":
                print("Can't do that")
                continue
            if user_input == "East":
                player.actionClass.east(player, 0)
                print("e")
                break
            if user_input == "South":
                print("Can't do that")
                continue
            if user_input == "West":
                print("Can't do that")
                continue
def Area():
    print("\n" * 100)
    if player.location == 2:
        print("\n" * 100)
        print("There is nothing to do here, might want to travel to another location")
        os.system("pause")
        print("\n" * 100)
    elif player.location == 4:
        if 'Talisman_of_Truth' in player.inventory:
            print("You win!"'\n'"Congratulations")
            os.system("pause")
        elif 'Talisman_of_Truth' not in player.inventory:
            print("The Monster of Doom destroys you in one mighty smack")
            playerClass.death(player)
            os.system("pause")
            sys.exit(Lose)
        else:
            sys.exit(0)
    elif player.location == 3:
        while True:
            print("\n" * 100)
            print("Welcome to the shop"'\n'"What would you like to buy?"'\n'"'Buy Charm' - Charm of Capitalism for 20 Gold"'\n'"OR"'\n'"'Buy Talisman' - Talisman of Truth for 100 gold"'\n'"OR"'\n'"'Status' - View gold, health and inventory"'\n'"OR"'\n'"'Exit' - Leave the store")
            buy_input = input()
            if buy_input == "Buy Charm":
                if player.gold >= Charm_of_Capitalism.value:
                    Charm_of_Capitalism.add_charm(player)
                    print("After that purchase you now have",player.gold,"gold remaining")
                elif player.gold < 19:
                    print("Sorry you can't afford this")
                    continue
                else:
                    print("oops")
                    break
            if buy_input == "Buy Talisman":
                if player.gold >= Talisman_of_Truth.value:
                    Talisman_of_Truth.add_tali(player)
                    print("After that purchase you now have", player.gold, "gold remaining")
                elif player.gold < 100:
                    print("Sorry you can't afford this")
                    continue
                else:
                    print("oops")
                    break
            if buy_input == "Status":
                    playerClass.status(playerClass)
                    os.system("pause")
                    continue
            if buy_input == "Exit":
                print("See you next time hero!")
                break
    elif player.location == 1:
        while True:
            grind_input = input("Kill Monster - Gain between 1 - 10 gold and lose between 0 - 20 health"'\n'"Run - go back to the available options"'\n'"'Status' - View gold, health and inventory")
            if grind_input == "Kill Monster":
                print("\n" * 100)
                if 'Charm_of_Capitalism' in player.inventory:
                    player.gold = player.gold + (randint(10, 100))
                else:
                    player.gold = player.gold + (randint(1,10))
                player.health = player.health - fightdamage
                print("Your health is now",player.health)
                print("You now have",player.gold,"gold in your pocket")
                continue
            if grind_input == "Run":
                break
            if grind_input != "Kill Monster" or gring_input != "Run":
                print("oops")
                break
            if ginrd_input == "Status":
                playerClass.status(playerClass)
                os.system("pause")
    elif player.location == 0:
        while True:
            print("\n" * 100)
            print("You feel the power of the pool rejuvenate you, really earns it's name doesn't it?")
            print("Your health is now back at",player.health)
            os.system("pause")
            break


print("You are stood at The Crossroads")
os.system("pause")
player = playerClass(2, 100, False, 0,[])
fightdamage = playerClass.damage(player)
while True:
    Main.options(None)