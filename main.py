import os
import sys
from datetime import datetime
import random




global generated_number , difficulty_chance ,high_score_dict
generated_number = random.randint(1,100)
difficulty_chance ={ '1': 10 , "2":5 ,"3":3 }
high_score_dict ={
    "1":  [None,None],
    "2":  [None,None],
    "3":  [None,None]
    }

def hint_sys(number):
    if number < generated_number :
        print(f"The number is bigger than {number}")
    else :
        print(f"The number is less than {number}")


def score_saver(Dura,att,dif_id):

    if  high_score_dict[str(dif_id)][0] == None :
        print("sssssssssssssssssssssss")
        high_score_dict[str(dif_id)][0] =att
        high_score_dict[str(dif_id)][1] =Dura
    elif att < high_score_dict[str(dif_id)][0] :
        print("uuuuuuuuuuuuuuuuuuu")
        high_score_dict[str(dif_id)][0] =att
        high_score_dict[str(dif_id)][1] =Dura




def start_the_game(imp=0):
    global high_score_dict
    start_time = datetime.now()

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
                end_time = datetime.now()
                Duration = end_time - start_time
                print('Duration: {}'.format(Duration))

                score_saver(Duration,chance,difficulty_ID ) 
                guessed=True
                print(f""" Congratulations! You guessed the correct number in {chance} attempts""")
                break
            else :
                print(f"Your guess is not correct , you have {difficulty-1-chance} chances left ")
                hint_sys(guess)
        else :
            print(f"Your input is not valid!! , you lost one chance you still have {difficulty-1-chance} chances left ,try again with number between 1-100.")

    if guessed == False :
        print(f"Unfortunately! You did not guess the correct number which was {generated_number} in {chance+1} attempts ")
    again = input("Do you want to play again ?? [yes/no]")


    while again not in ["yes","no"]:
        print("Your input key is not valid write yes or no ")
        again= input("\t Do you want to play ?? [yes/no]")
    
    if again == "yes" :
        generated_number = random.randint(1,100)
        start_the_game()
    elif  again == "no":
        print("Okay bye bye !!!")
        print(f'''This is your highest scores  :
            1. Easy ({high_score_dict["1"][0]} attempts )
            2. Medium ({high_score_dict["2"][0]} attempts )
            3. Hard ({high_score_dict["3"][0]} attempts )
        ''')
        
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


