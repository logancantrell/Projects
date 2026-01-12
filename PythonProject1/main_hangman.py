import random
import hangman_words
import hangman_art
# TODO-1: - Update the word list to use the 'word_list' from hangman_words.py

lives = 6

# TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.

chosen_word = random.choice(hangman_words.word_list)
print(chosen_word)
print(hangman_art.logo)
placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []
while not game_over:

    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()


    if guess in correct_letters:
        print("You have already guessed {guess}.")

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)


    if guess not in chosen_word:
        print(f"You guessed {guess} witch is not in the word! You lose a life :(")
        lives -= 1

        if lives == 0:
            game_over = True

            print(f"It was {chosen_word}! YOU LOSE")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")


    print(hangman_art.stages[lives])
