import random

class game():

    def __init__(self):
        self.hp = random.randrange(50,200)
        self.mp = random.randrange(20,100)
        self.atk = random.randrange(1,20)

    def attack(self):

        return self.atk

    def defend(self,damage):

        self.hp = self.hp - damage

    def low_mp(self,low):

        self.mp = self.mp - low

    def heal(self,mp):

        self.hp = self.hp + (mp * 2)
        self.mp = self.mp - mp

person = game()
computer = game()

turn = random.randrange(0,1)

while True:

    print("your HP:", person.hp, "                            enemy's HP:", computer.hp)
    print("your MP:", person.mp, "                            enemy's MP:", computer.mp)
    print("your atk:", person.atk, "                            enemy's atk:", computer.atk)

    if (person.hp <= 0 or computer.hp <= 0):
        if person.hp <= 0:
            print("you lose")
        else:
            print("you win")
        break
    elif turn == 0:
        atk = input("will you attack?(Y/N{heal = H})>>>")
        if atk == "Y" or atk == "y"and person.mp >= 0:
            person.low_mp(1)
            computer.defend(person.attack())
        turn = 1
        if atk == "H" or atk == "h" and person.mp >= 0:
            heal = int(input("how many mp use to heal?(1 mp = 2 heal)>>>"))
            person.heal(heal)
        if atk != "y" or atk != "Y":
            pass
        if person.mp <= 0:
            print("you all MP,you can't win!!!!!")
            break

    else:
        if computer.mp >= 0:
            computer.low_mp(1)
            print("you are attacked by computer")
            person.defend(computer.attack())
            turn = 0
        elif computer.mp <= 0:
            print("your enemy has no MP")
            print("you win")
            break
        if computer.hp <= 20 and computer.mp >= 100:
            computer.heal(80)
