import random

logo = """"

 _____                          _    _                                      _                 
|  __ \                        | |  | |                                    | |                
| |  \/ _   _   ___  ___  ___  | |_ | |__    ___   _ __   _   _  _ __ ___  | |__    ___  _ __ 
| | __ | | | | / _ \/ __|/ __| | __|| '_ \  / _ \ | '_ \ | | | || '_ ` _ \ | '_ \  / _ \| '__|
| |_\ \| |_| ||  __/\__ \\__ \ | |_ | | | ||  __/ | | | || |_| || | | | | || |_) ||  __/| |   
 \____/ \__,_| \___||___/|___/  \__||_| |_| \___| |_| |_| \__,_||_| |_| |_||_.__/  \___||_|   
                                                                                              
                                                                                              
                                                                       

"""
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
number = random.randint(1, 100)
# print(f"Pssst, the correct answer is {number}")

live = 11
ask = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
is_game_end = False
while not is_game_end:
    if ask == 'easy':
        if live - 1 > 0:
            print(f"You have {live - 1} attempts remaining to guess the number.")
            guess = int(input("Make a guess: "))
            if guess == number:
                print(f"You got this! Answer was {number}")
                is_game_end = True
            elif guess > number:
                print("Too high\nGuess again.")
            else:
                print("Too low\nGuess again.")
        else:
            print(f"You ran out of live. Answer was {number} Game over")
            is_game_end = True

    elif ask == 'hard':
        if live - 6 > 0:
            print(f"You have {live - 6} attempts remaining to guess the number.")
            guess = int(input("Make a guess: "))
            if guess == number:
                print(f"You got this! Answer was {number}")
                is_game_end = True
            elif guess > number:
                print("Too high\nGuess again.")
            else:
                print("Too low\nGuess again.")
        else:
            print(f"You ran out of live. Answer was {number} Game over")
            is_game_end = True
    else:
        print("You have written non-existing input.")
        is_game_end = True
    live = live - 1
