import random

# Game setup
print('Welcome to The Guessing Game!')
number_of_guesses = 3  # User has 3 guesses before losing the game.
user_won = False

# Computer guesses a random number between 1 and 10.
correct_answer = random.randint(1, 10)
print(correct_answer)

while number_of_guesses > 0:
    # User guesses the number.
    user_guess = input('Guess my number: ')

    # Computer tells the user whether guess was too high or low.
    user_guess = int(user_guess)
    if user_guess == correct_answer:
        print('Good guess!')
        print('You are correct!')
        user_won = True
        break
    elif user_guess > correct_answer:
        print('Sorry, your guess is too high!')
    elif user_guess < correct_answer:
        print('Sorry, your guess is too low!')

    number_of_guesses -= 1

if user_won == True:
    print('You won!')
else:
    print('You lost!')
