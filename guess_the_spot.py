name = input("enter your name: ")

print("Level 1\nhello " +name+ ", find the number 5 between the S alphabets")
guess_the_number_level1 = [
    "S","S","S","S","S","S","S","S","S","S",
    "S","S","5","S","S","S","S","S","S","S",
    "S","S","S","S","S","S","S","S","S","S",
    ]
guess_the_number_level2 = [
    "O","O","O","O","O","O","O","O","O","O",
    "O","O","O","O","O","O","O","0","O","O",
    "O","O","O","O","O","O","O","O","O","O",
    ]
guess_the_number_level3 = [
    "E","E","E","E","E","E","E","3","E","E",
    "E","E","E","E","E","E","E","E","E","E",
    "E","E","E","E","E","E","E","E","E","E",
    ]
print(guess_the_number_level1)
the_number_spot_level1 = "13"
#don't you dare cheat and look at the answer in the code >:(
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False
while guess != the_number_spot_level1 and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = (input("enter the number's spot: "))
        guess_count += 1
    else:
        out_of_guesses = True
if out_of_guesses:
    print("You lost, try again " + name )
else:
    print("congrats " + name + "! You won!")
if guess == the_number_spot_level1:
    print("Level 2\nfind the number 0 between the O alphabets")
    print(guess_the_number_level2)
the_number_spot_level2 = "18"
#you shouln't look here >:(
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False
while guess != the_number_spot_level2 and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = (input("enter the number's spot: "))
        guess_count += 1
    else:
        out_of_guesses = True
if out_of_guesses:
    print("You lost, try again " + name )
else:
    print("congrats " + name + "! You won!")
if guess == the_number_spot_level2:
    print("Level 3\nfind the number 3 between the E alphabets")
    print(guess_the_number_level3)
the_number_spot_level3 = "8"
#don't you even think about doing it >:(
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False
while guess != the_number_spot_level3 and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = (input("enter the number's spot: "))
        guess_count += 1
    else:
        out_of_guesses = True
if out_of_guesses:
    print("You lost, try again " + name )
else:
    print("Congrats " + name + "! you won the game!")
    
     

