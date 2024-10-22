import random

word_list = ["Hello", "Apple", "Computer", "Whiteboard"]
chosen_word = random.choice(word_list).lower()
list_of_user_guess = set()
lives = 10

listword = list(chosen_word)

emptylist = ["_" for i in range(len(listword))]

print(emptylist)

while lives > 0:
  user_guess = input("Guess a letter: ").lower()
  if user_guess in list_of_user_guess:
    print("You have already guessed this letter. Try another one.")
    continue
  else:
    list_of_user_guess.add(user_guess)
    if user_guess in listword:
      n = len(listword)
      for i in range(n):
        if user_guess == listword[i]: emptylist[i] = user_guess
    else:
      lives -= 1
      print("You have " + str(lives) + " lives left.")
      print("The letter is not in the word. Try again.")
    print("".join(emptylist))
    if "_" not in emptylist:
      print("You won the game!")
      break
if lives == 0:
  print("You ran out of lives. Try again.")
