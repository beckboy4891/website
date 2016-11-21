from random import randint
print ('Welcome to the omniverse please enter your name!')
name = input ("Name:")
c = ("Your name is")
print (c , name)
print ("would that be okay?")
choice = input ("Yes or No? :")
print ("You will be")
c1 = ("wizard,")
print (c1 , name)
if choice == ("Yes"):
    print ("wonderful")
    print ("your first quest lays in the dark forest!")
    print ("The king has chosen you to kill a monster that has been causing trouble")
    print ("do you accept?")
    choice1 = input ("Yes or No:")
elif choice == ("No"):
    print ("Please restart to choose a diffrent name.")
else :
    print ("make sure to capatilize the first letter of the answer!")
if choice1 == ("Yes"):
        print ("You head towards the dark forest with a sword and food for a day.")
        print ("You plan to be back before night fall the monster is known for killing the")
        print ("strongest of men but you are a young weak wizard..who knows what will happen")
        print ("you hear a loud growl behind you you slowly turn on your heel to find a large")
        print ("bear like creature and you have two choices cast a spell or hit it with your sword")
elif choice1 == ("No"):
           print ("You need to make the right choice and not disrespect the king")
else : print ("make sure to capatilize the first letter of the answer!")
damage1 = (randint(70,100))
damage2 = (randint(90,100))
playerhealth = 100
bearhealth = 100
a = ("The monster has")
b = ("health remaining")
print ("The wild bear appears choose 1 for sword or 2 for spell.")
attack = input ("put attack here! :")
if attack == ("1"):
    remaininghealth = bearhealth - damage1
    print (a,remaininghealth,b)
elif attack == ("2"):
    remaininghealth = bearhealth - damage2
    print (a,remaininghealth,b)
else:
    print ("Please enter a valid attack")
if remaininghealth > 0:
    print ("The bear attacks You but misses!")
    print ("you are lucky and get to attack again!")
    attack2 = input ("put attack here! :")
elif remaininghealth <= 0:
    print ("congradulations you beat the beast!")
else:
    print ("please enter a valid attack")
if attack2 == ("1"):
    remaininghealth1 = remaininghealth - damage1
    print (a,remaininghealth1,b)
elif attack2 == ("2"):
    remaininghealth1 = remaininghealth - damage2
    print (a,remaininghealth1,b)
else:
    print ("please enter a valid attack")
if remaininghealth1 > 0:
    print ("The bear quickly rises and slams down on you!")
    print ("You Cannot move away, you died")
elif remaininghealth1 <= 0:
    print ("The bear falls to your feet surronded by a pool of red blood!")
    print ("You have Slain the beast!")
elif remaininghealth1 < 0:
    print ("The bear falls to your feet surronded by a pool of red blood!")
    print ("You have Slain the beast!")
else:
    print ("good job you have officaialy fooled me I don't even know how you got here")
