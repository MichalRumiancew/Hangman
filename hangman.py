####################################################
###########      HANGMAN       #####################
####################################################

import random
import os
os.system("cls || clear")

word_list = ["ONE", "TWO", "THREE", "FOUR"]

def counter(tries):

    if tries == 3:
        print(" ##############  YOU HAVE MAXIMUM LIFE  ###################")
    elif tries == 2:
        print("  |       \n  |       \n  |      \n  | \n------")
    elif tries == 1:
        print("   ______\n  |      |\n  |      |\n  |       \n  |       \n  |      \n  | \n------")
    elif tries == 0:
        print("   ______\n  |      |\n  |      |\n  |      O\n  |      |/\n  |      | \n  |     /|  \n  |      \n  | \n------")
   

def menu():
    name = input(" PLEASE ENTER YOUR NAME: ")
    print("\n##############################\n\n          HI ", name, "\n\n##############################\n")
    print(" SELECT OPTION :")
    print(" NEW GAME -- PRESS -- 1 ")
    print(" END GAME -- PRESS -- 2 ")


def input_function1():

    user_input1 = input(" CHOOSE :   ")

    try:
        number1 = int(user_input1)
        return number1
    except ValueError:
        return


def game_function():
    word = str(word_list[random.randint(0,len(word_list)-1)])
    word_completion = list(word)
    for i in range(len(word)):
         word_completion[i] = "_"

    tries = 3
    #print(word_completion)
    print("\n LET'S START THE GAME")
    print(" YOU HAVE ", str(tries), " LIVES\n\n")
    print("  ".join(word_completion))
    print("\n\n")
    counter(tries)
    score = 0
   
    
    while tries > 0:    
         user_input1 = input("\n CHOOSE WISELY LETTER OR WORD:  ").upper()
         if len(user_input1) == 1 :
             if user_input1 in word:
                print("\n BRAWO YOU GUESSED THE LETTER", user_input1, "\n")
                for i in range(len(word)):
                    if(word[i] == user_input1):
                     word_completion[i] = user_input1
                     print(" ".join(word_completion))
                if "".join(map(str,word_completion)) == word:
                 print(" ")
                 print("\n YOU ENDED A GAME WITH  ", str(tries), " LIVES\n")
                 print("  ".join(word_completion))
                 print("############    YOU WIN!!!   ###############")
                 score = tries + len(word)
                 print("YOUR RESULT :", score)
                                 
                 return None
                
             
             else: 
                print("   ", user_input1, " IS NOT IN THE WORD\n\n")
                tries -= 1
                counter(tries)
                print("\nYOU HAVE ", tries, " LIVES LEFT \n")

         elif len(user_input1) != 1 :
             if user_input1 in word:
                 print("\n BRAWO YOU GUESSED THE WORD", user_input1, "\n")
                 print(" ")
                 print("\n YOU ENDED A GAME WITH  ", str(tries), " LIVES\n")
                 print("  ".join(word_completion))
                 print("############    YOU WIN!!!   ###############")
                 counter(tries)
                 score = tries + len(word)
                 print("YOUR RESULT :", score)
                     
                 return None
                     
             else: 
                 print("   ", user_input1, " IS NOT IN THE WORD\n\n")
                 tries -= 1
                 counter(tries)
                 print("\nYOU HAVE ", tries, " LIVES LEFT \n")
                     
          
    else:
        print("YOU LOSE!!! THE WORD WAS : " + word + "\n\n############## END GAME ###############\n")
                
        
def main():

    menu()

    user_number1 = input_function1()
    while user_number1 is None:
        user_number1 = input_function1()

    if user_number1 == 1:

        game_function()

        while input("PLAY AGAIN? (Y/N)").upper() == "Y":           
            game_function()
            return

    elif user_number1 == 2:
        print("\n\n#########    END GAME    #########")
        print("\n\n")
        while input("PLAY AGAIN? (Y/N)").upper() == "Y":
            game_function()
            return


main()