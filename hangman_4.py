import random
from words import words
from hangman_visual import lives_visual_dict
import string



# getting word without space and dash
def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    
    return word.upper()



def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    # a to z assigned to alphabet
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 7

    while len(word_letters) > 0 and lives > 0:

        print("You have used these letter: ",''.join(used_letters))

        word_list = [letter if letter in used_letters else '-' for letter in word]

        print(lives_visual_dict[lives])

        print("Current Word: ", ''.join(word_list))
 
        user_letter = input("Guess a letter: ").upper()

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')
            else:
                lives = lives - 1
                print("\nYour letter ,", user_letter, "is not in word" )
        
        elif user_letter in used_letters:
            print("You already used this latter, please try other letter")

        else:
            print("Invalid character, please try again")

    if lives == 0: 
        print(lives_visual_dict[lives])
        print("You deid, sorry. The word was", word)
    else:
        print("Yay! You guessed the word,", word,"!")

hangman()



