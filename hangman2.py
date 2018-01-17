
import os
import random


def get_puzzle():
    file_names = os.listdir("data")

    for i, f in enumerate (file_names):
        print(str(i+1) + " ) " + f)

    choice = input ("which one?")
    choice = int(choice)

    file = "data/" + file_names[choice-1]

    with open (file, 'r') as f:
        lines = f.read().splitlines()


    category = lines[0]
    puzzle = random.choice(lines[1:])

    return puzzle



def start_screen():
    art_names = os.listdir("art")
    file = "art/" + art_names[1]

    with open(file, 'r') as f:
        line = f.read()
        print(line)
        
def get_solved(puzzle, guesses,):
    solved = ""

    for letter in puzzle:
        if letter in guesses:
            solved += letter
        else:
            solved += "-"
    return solved

def get_guess(name):
    alpha = 'qwertyuiopasdfghjklzxcvbnm'
    while True:
        guess = input(" Enter a letter " + str (name) + "" +  ".")

        if len(guess) >= 2:
            print (" sorrybuy that is to long")
        elif guess not in alpha:
            print("guess an a letter that is in the alphabet.")
        else:
            return guess

def display_board(solved, used, miss):
    print (solved)
    print (" you have " + str(miss) + " tries left.")




    if miss == 5:
        print ( """    .-.:|.-.
   .'   ''   '.
   ;          ;
   '-.         :
     }         :
   .-'         :
   :          ;
   '.        :
     '-_.._-'

""")

    if miss == 4:
        print ("""            .:'
         __ :'__
      .'`__`-'__``.
     :__________.-'
     :_________:
      :_________`-;
      `.__.-.__.'
   """)

    if miss == 3:
        print (""" .-.:|.-.
   .'   ''   '.
   '-.        ;
     }      .-'
     }      {
     }      '-.
   .-'        ;
   '.        :
     '-_.._-'
""")


    if miss == 2:
        print (""" .-.:|.-.
   .'   ''   '.
   '-.      .-'
     }      {
     }      {
     }      {
   .-'      '.
   '.        :
     '-_.._-' """)

    if miss == 1:
        print("""     .-.:|.-.
   .'   ''   '.
   '-.      .-'
     }"~".  {
     } } }  {
     } ' }  {
   .-'"~"   '.
   '.        :
     '-_.._-'
 """)


    if miss == 0:
        print("""   .-.:|.-.
   .'   ''   '.
   '-.      .-'
     }"~"."~{
     } } } '{
     } ' } :{
   .-'"~"~"~'.
   '.        :
     '-_.._-'

    YOU LOSE!!!

     """)








    print (" Guessed letters: " + used )



def play_again():

        while True:


            again = input(" would you like to play again? yes or no?")

            if again == "y" or again == "yes":
                return True

            elif again == "no" or again == "n":
                return False

            else:
                print (" I'm sorry I don't understand, please enter yes or no")


def show_result(miss, puzzle):
   if miss == 0:
       print (" you lost the word was " + puzzle + " . ")

   else:
        print ("you win. Thanks for playing!!")



def name():

    print ("what is your name?")
    name = input()
    return name


def play(player):


    puzzle = get_puzzle()
    guesses = ""
    solved = get_solved(puzzle, guesses)
    miss = 6
    used = ""

    print(solved)

    while solved != puzzle and miss != 0:
        letter = get_guess(player)
        used += letter

        if letter not in puzzle:
            print (" sorry human but you got it wrong. try again.")
            miss -= 1



        guesses += letter
        solved = get_solved(puzzle, guesses)
        display_board(solved, used, miss)

    show_result(miss, puzzle)


#game starts here

start_screen()

player = name()


playing = True

while playing:
    play(player)
    playing = play_again()

end_credits()
