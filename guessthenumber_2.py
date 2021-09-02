import random

x = int(input("You left side limit is 1 and Enter right side limit: "))

def guess(x):
    ran_num = random.randint(1,x)
    guess = 0
    while guess != ran_num:
        guess = int(input(f'Guess number between 1 and {x}: '))

        if guess > ran_num:
            print("your guess is high")
        elif guess < ran_num:
            print("your huess is low")
    print(f'yay congrats. You have guessed the number {ran_num} correctly!!')
    quit()

guess(x)