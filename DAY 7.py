word_list = ["python", "banana", "cricket", "elephant", "mango"]
import random
def show_welcome():
    print("WELCOME TO WORD SCRAMBLE GAME!")
    print("UNSCRAMBLE THE WORD TO WIN!")

def show_result(won, chosen_word):
    if won:
        print(" Correct! You Win!")
    else:
        print(f" Game Over! Word was: {chosen_word}")

show_welcome()

chosen_word = random.choice(word_list)

scrambled = random.sample(chosen_word, len(chosen_word))
scrambled_word = "".join(scrambled)

lives = 3

while lives > 0:

    print(f"\nScrambled Word: {scrambled_word}")

    guess_word = input("Enter your guess word: ").lower()

    if guess_word == chosen_word:
        show_result(True, chosen_word)
        break

    else:
        lives -= 1
        print(f" Wrong! {lives} lives remaining")

        if lives == 0:
            show_result(False, chosen_word)