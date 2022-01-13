print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')

print()
print('Welcome to treasure Island!')
print('Hopefully, you will be able to find the treasure.')
print("Or be toasted, for dinner.")

print()
print()

print('As you pass through the island gates, they are mysteriously shut behind you.')
print('Ahead, you see a hole and think you could jump over or search for a log.')
print()

first_choice = input('Which do you do? jump or search\n>').lower()

if first_choice == 'search':
    print()
    print('You wisely look around for a log.')
    print('You find one however, it is suprisingly heavy.')
    print('You lift it anyways and place it above the ditch and walk across.')
    print()
    print("You've been walking for hours now, already exhausted.")
    print('Just when you are about to sit down to rest, you see two separate paths ahead.')
    print('Confused, you try to look for a hint to the right path.')
    print('You see on a monumental stone written: ')
    print('"The right path is the left path."')
    print('However, there is a left arrow is pointing right')
    print('and a right arrow is pointing leftwards.')
    print()
    
    second_choice = input('Even more confused, what path do you take? left or right \n>').lower()
    
    if second_choice == 'left':
        print()
        print('Hesistantly, you pick the left path.')
        print('The path looks very frightening.')
        print('It seems like you made the wrong choice.')
        print('Eventually, you get to a stream of water.')
        print('You are relieved as you careful scoop water with your palms and drink.')
        print('After you are satisfied, you brace up for whatever and continue you journey.')
        print()
        print("You have been walking for hours and it's dark already.")
        print('To your surprise, you see an odd cottage and lamplight shining from the inside.')
        print('You guess that they are adventurers like you and decide to go seek shelter.')
        print('As soon as you are about to knock, a second thought flashes through your mind...')
        print('What if it is a trap of some sort?')
        print()

        third_choice = input('Very scared and exhausted, you paused to decide: run or knock \n>').lower()
        
        if third_choice == 'run':
            print()
            print('Very terrified, you cowardly withdraw from the house and flee.')
            print('You run until the cottage is no longer in sight.')
            print('You stop to catch your breath and contemplate on how stupid you were to not have knocked.')
            print('However, fear would not let you go back, so you just keep going.')
            print()
            print('You had not walk so much when your foot hit something.')
            print('Painfully, you shriek silently in pain.')
            print('Then you look down at what you had kicked.')
            print('You blurringly see a tree stump.')
            print('However, in front of the stump is a hole and a scarecrow with a sign that reads:')
            print("This is the spot marked 'x'")
            print('Perharps, this is the treasure point.')
            print('Or a trick to trap you.')
            print('You sit on the stump to carefully analyse all the happenings of the day.')
            print('It is a tough decision.')
            print()
        
            fourth_choice = input('But, you have chosen to: jump or ignore \n>').lower()
            
            if fourth_choice == 'jump':
                print()
                print('Even though every fiber of your body objects,')
                print('A small part of you wants to see what is below.')
                print('You curse your adventure spirit as you gently put your legs into the hole.')
                print('You slide down sharply into a tunnel but landed unhurt.')
                print('You certainly are trapped.')
                print()
                print('Right ahead, you see some yellow light')
                print('Almost immediately, you remember the cottage earlier.')
                print('However, your adventure spirit kicks in again and you run to feed your curiousity.')
                print('Alas! You meet the source of the light.')
                print('You have found the treasure.')
                print('It is probably all the gold in the world.')
                print('You are rich, super rich!')
                print('You win!')
                print()
                print()
                print('But then...')
                print('How do you leave the hole?')
                print()
                print('Game over!')
                print()
            
            else:
                print()
                print('You believe it is a trick.')
                print('You hurriedly walk away from the scene.')
                print('As you walk away from the hole, you think deeply about your decision.')
                print('Then you satisfactorily smile at your wisdom.')
                print('You title yourself "The wisest that art".')
                print('You smile broadly at your ability to have detected the trap.')
                print('This achievement blinds your consciousness as your walk on halfheartedly.')
                print('Until you step on an unusual mass of soil.')
                print()
                print('The paths on the island are not smooth.')
                print('Why then did you feel this abnormal soil?')
                print('maybe it is because your happiness had faded.')
                print('Or it is because...')
                print('what you had stepped on was alive.')
                print('Before you can confirm what you had stepped on, you feel a sharp pain on your neck.')
                print('You fall immediately as you grief whilst holding your neck.')
                print('You lie partly unconscious as the venom spread through your body.')
                print("Alas! You have become a cobra's dinner")
                print()
                print('Game over!')
                print()

        else:
            print()
            print('You are quite sure that the house is empty.')
            print('You knock softly at the door...')
            print('No response...')
            print('You were right, there is no one in it.')
            print('As soon as you touch the door to push it open, it opens itself mysteriously.')
            print()
            print('But the door did not exactly open by itself.')
            print('Behold in front of you...')
            print('three very wrinkled old women in clean rags.')
            print('They welcome you joyously')
            print('as though you are a long lost relative.')
            print('One hands you a glass of milk with a smile, showing off her tooth cavities.')
            print('You immediately gulp the milk and return the glass with a belch.')
            print('You are now fully conscious and try to introduce yourself.')
            print('However, they shush you saying "Come in! Dear child"')
            print('You respectfully walk in whilst inspecting the room.')
            print('It is a lttle foul but bearable, at least for the night.')
            print('They show you a ragged couch to sit on.')
            print('You drop flat on the couch, tiredly.')
            print('You manage to say "Thank you" before you dose off.')
            print()
            print('You wake up to see yourself naked, tied to a tree stump.')
            print('It was midnight and you can see a full moon.')
            print('You are surrounded by the old women, each holding a knife and a plate.')
            print('Alas! You realize...')
            print('It was a home of witches and you were drugged.')
            print('You are gonna be used for a sacrifice or something.')
            print('You cry profusely knowing this is your end.')
            print()
            print('Game over!')
            print()


    else:
        print()
        print('Very convinced, you take the right path.')
        print('But, it did not take you long to question your decision.')
        print('You cut leaves and drop them on the path as trails.')
        print('After walking for some time, you realize your mistake.')
        print()
        print('Alas! You have been trapped in a maze of some sort.')
        print('You try to find your way back to the crossway.')
        print('You eventually give up after several fruitless attempts.')
        print('You are lost and is never heard of again.')
        print()
        print('Game over!')
        print()

else:
    print()
    print('You think you can jump over and leap.')
    print('Unfortunately, you forget that it is a mysterious island.')
    print('As you spring into the air, the hole seem to increase.')
    print('You never could have jumped over afterall.')
    print('You fall into the ditch and is never heard of again.')
    print()
    print('Game over!')
    print()