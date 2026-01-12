import os
import sys
import datetime
import random

global generated_number , difficulty_chance
generated_number = random.randint(1,100)
difficulty_chance ={ '1': 10 , "2":5 ,"3":3 }



def start_the_game(imp=0):
    global generated_number

    while imp == 0 :

        difficulty_ID= input('''Please select the difficulty level by its id:
            1. Easy (10 chances)
            2. Medium (5 chances)
            3. Hard (3 chances)
            ''')
        try:
            difficulty_ID = int(difficulty_ID)
        except :
            print("The Difficulty ID is not exist use one of [1,2,3]")
        if difficulty_ID not in [1,2,3] :
            print("The Difficulty ID is not exist use one of [1,2,3]")
        else :
            difficulty = int(difficulty_chance[str(difficulty_ID)])
            imp = 1 


    guessed= False

    for  chance in range(0,difficulty) :
        guess = input("Enter your guess:")
        try:
            guess = int(guess)
        except :
            print(f'Your input is not valid!! , you lost one chance you still have {difficulty-1-chance} chances left ,try again with number between 1-100.')
            continue
        if  isinstance(guess, int) and ((int(guess) < 100) and (int(guess) > 0) ):
            if guess == generated_number :
                guessed=True
                input_text = f""" Congratulations! You guessed the correct number in {chance} attempts ,
                Do you want to play again ?? [yes/no]"""
                again = input(input_text)
                break
            else :
                print(f"Your guess is not correct , you have {difficulty-1-chance} chances left ")
        else :
            print('''Your input is not valid!! , you lost one chance you still have {(difficulty-1)-chance} chances left ,
             try again with number between 1-100.''')

    if guessed == False :
        print(f"Unfortunately! You did not guess the correct number which was {generated_number} in {chance+1} attempts ")
        again = input("Do you want to play again ?? [yes/no]")

    if again in ["yes","no"]:
        pass
    else:
        while again not in ["yes","no"]:
            input_text2 ="Your input key is not valid write yes or no "
            again= input(input_text2)
    
    if again == "yes" :
        generated_number = random.randint(1,100)
        start_the_game()
    elif  again == "no":
        print("Okay bye bye !!!")
    else :
        print("Error input ")
        

    
if __name__ == "__main__":

    print('''*** Welcome to the Number Guessing Game! ***
    I'm thinking of a number between 1 and 100.
    You have many chances to guess the correct number. ''')
    first_input = input("\t Do you want to play ?? [yes/no]")

    while first_input not in ["yes","no"]:
        print("Your input key is nat valid write yes or no ")
        first_input = input("\t Do you want to play ?? [yes/no]")

    if first_input == 'yes':
        
        start_the_game()

    elif first_input == "no":
        print("Okay bye bye !!!")
    else :
        print("Error input ")


