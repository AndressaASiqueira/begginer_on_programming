from word_list import word_list 

from arts import stages


import random
chosen_word = random.choice(word_list)

from arts import logo
print(logo)

#print(f"chosen word is: {chosen_word}")


number_of_letters = len(chosen_word)
word_picked = []
for n in range(number_of_letters):
    word_picked += "_"
print(f"{' '.join(word_picked)}")

end_of_the_game = False

lives = 6

while not end_of_the_game:
    guess = input("Guess a letter: ").lower()
    
    if guess in word_picked:
        print(f"You've already guessed {guess}")


    for position in range(number_of_letters):
        letter = chosen_word[position]

        if letter == guess:
            word_picked[position] = letter
    
    if guess not in chosen_word:
            print(f"You guessed {guess}, that's not in the word. You lose a life.")
            lives -= 1
            if lives == 0:
                end_of_the_game = True
                print("You lose")

    print(f"{' '.join(word_picked)}")    
        
    
    if "_" not in word_picked:
        end_of_the_game = True
        print("You Win")

    print(stages[lives])
        
         
