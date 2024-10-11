import random

rock = '''
_________
|_ _ _(_ _)
|  _ _( _ _ _)
| _ _ (_ _ _ _)   
| __ _ (_ _ _ )     
| _ _ _ (_ _)         
'''

paper = '''
___________
|_ _  _ )
|_ _ _ _ _ )
| _ _ _ _ _)   
|_ _ _ _ _ )     
| _ _ _ _)         
'''

scissors = '''
|_ _ _ _ _ _
|  _ _( _ _ _)
|_- - -_ _ _
| __ _ (_ _ _ )     
|         
'''

game_images = [rock, paper, scissors]

user_choice = int(input('What do you choose?'
              'Type 0 for rock, 1 for paper, or 2 for scissors\n'))
print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print(f"Computer chose:")
print(game_images[computer_choice])

if user_choice < 0 or user_choice > 2:
    print("You typed an invalid number. You lose!")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and user_choice == 2:
    print("You lose!")
elif computer_choice > user_choice:
    print("You lose!")            
elif user_choice > computer_choice:
    print("You win!")
elif computer_choice == user_choice:
    print("It's a draw")



















