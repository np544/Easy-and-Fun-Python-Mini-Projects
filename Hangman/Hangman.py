
import random
from hangman_words import word_list
from hangman_art import logo,stages

print(logo)
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6
print("Let's start the challenge!")

display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("\nGuess a letter: ").lower()

    if guess in display:
      print(f"Already guessed letter {guess}. Let's try another one.")

    for position in range(word_length):
        letter = chosen_word[position] 
        if letter == guess:
            display[position] = letter
    
  
    if guess not in chosen_word:
      print(f"{guess} not in the word. One life gone.")
      lives -= 1
      if lives == 0:
          end_of_game = True
          print(f"\nYou lose. Better luck next time.\n The actual word was {chosen_word}")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("\nCongratulations! You win.")


    print(stages[lives])
    