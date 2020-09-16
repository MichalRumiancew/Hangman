def counter(tries):

    if tries == 3:
        print(" +_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+")
    elif tries == 2:
        print("  |       \n  |       \n  |      \n  | \n------")
    elif tries == 1:
        print("   ______\n  |      |\n  |      |\n  |       \n  |       \n  |      \n  | \n------")
    elif tries == 0:
        print("   ______\n  |      |\n  |      |\n  |      O\n  |      |/\n  |      | \n  |     /|  \n  |      \n  | \n------")


def choose_word():
    word = random.choice(word_list)
    print(word)
    return word.upper()

    

def menu():

    print(" +_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+")
    print(" SELECT OPTION :")
    print(" NEW GAME -- PRESS -- 1 ")
    print(" END GAME -- PRESS -- 2 ")


def input_function1():

    user_input1 = input(" CHOOSE WISELY :   ")

    try:
        number1 = int(user_input1)
        return number1
    except ValueError:
        return 



def game_function(word):
    word_completion = " _ " * len(word)   
    shoot_letters = []
    tries = 3
    print(shoot_letters)
    print(" LET'S START THE GAME")
    counter(tries)
    print(word_completion + "")
    while tries > 0:
        user_input1 = input("\n CHOOSE WISELY :   \n").upper()
        if len(user_input1) == 1 :
            if user_input1 in word:
                print("BRAWO YOU GUESSED THE LETTER", user_input1)
            elif user_input1 not in word:
                print(user_input1, " IS NOT IN THE WORD")
                tries -= 1
                shoot_letters.append(user_input1)
            else:
                print("BRAWO " + user_input1 + " IS IN THE WORD!!!")
                shoot_letters.append(user_input1)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == user_input1] 
                for index in indices:
                    word_as_list[index] = user_input1
                word_completion = "".join(word_as_list)
                if " _ " not in word_completion:
                    shoot_letters = True


                
            
        else:
            print("WRONG LETTER")
        counter(tries)
        print(word_completion + "")
    if shoot_letters:
        print("############    YOU WIN!!!   ###############")
    else:
        print(" YOU LOSE!!! THE WORD WAS" + word + "\n ############## END GAME ###############")

    



def main():

    menu()

    user_number1 = input_function1()
    while user_number1 is None:
        user_number1 = input_function1()

    if user_number1 == 1:

        word = choose_word()
        game_function(word)

        while input("PLAY AGAIN? (Y/N)").upper() == "Y":
            word = choose_word()
            game_function(word)
            return 
    
    elif user_number1 == 2:
        print("\n\n#########    END GAME    #########")
        print("\n\n")
        while input("PLAY AGAIN? (Y/N)").upper() == "Y":
            word = choose_word()
            game_function(word)
            return 
        
       

main()