print("WELCOME TO THE NUMBER GUESSING GAME")
def greet():
  print("welcome to the game")
greet()
secret_number = 15
chances = 3
while chances > 0:
    guess_number = int(input(" Enter the number : "))
    if guess_number == secret_number:
       print("you win the game!")
       break
    else:
       chances-=1
       print("wrong guess.try again")
       print("remaing chances:",chances)
if chances == 0:
   print("GAME OVER")
   print("secret number was:",secret_number) 

  

  