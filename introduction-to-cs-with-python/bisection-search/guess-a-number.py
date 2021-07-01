'''
The program works as follows: you (the user) thinks of an integer between 0 (inclusive) and 100 (not inclusive). 
The computer makes guesses, and you give it input - is its guess too high or too low? 
Using bisection search, the computer will guess the user's secret number!
'''

print('Please think of a number between 0 and 100!')

minimum = 0
maximum = 100


while True:
    guess = (minimum + maximum) // 2

    print('Is your secret number', guess, "?")

    question = input(
        "Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")

    if question == 'l':
        maximum = guess
        continue

    elif question == 'h':
        minimum = guess
        continue

    elif question == 'c':
        print("Game over. Your secret number was:", guess)
        break

    else:
        print("Only, 'h', 'l' or 'c' will work")
        continue
