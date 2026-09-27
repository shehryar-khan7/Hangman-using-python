import random

word_list = ["aadvark", "baboon", "camel"]

choosen_word = random.choice(word_list)
print(choosen_word)  

placeholder = ""
word_leangth = len(choosen_word)
for position in range(word_leangth):
    placeholder += "_ "
print(placeholder)

game_over = False
correct_letter = []
lives = 6

while not game_over:
    guess = input("Guess a letter: ").lower()

    display = ""
    for letter in choosen_word:
        if letter == guess:
            display += letter + " "
            correct_letter.append(guess)
        elif letter in correct_letter:
            display += letter + " "
        else:
            display += "_ "

    print(display)

    if guess not in choosen_word:
        lives -= 1
        print(f"That letter isn't in the word. You have {lives} lives left.")
        if lives == 0:
            game_over = True
            print(f"You lose. The word was {choosen_word}.")

    if "_" not in display:
        game_over = True
        print("You win!")

