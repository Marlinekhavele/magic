# This is a guess the number game. 
import random
secretNumber = random.randint(1,20)
print('Iam thinking of a number between 1 and 20')

# ask the player to guess sixtimes
for guessesTaken in range (1,7):
    print ('Take a guess.')
    guess = int(input())
if guess < secretNumber:
    print('your guess is to low.')
    
elif guess > secretNumber:
    print('Your guess is to high.')
else:
    # This condition is the correct guess
   if guess == secretNumber:    print('Good job! You guessed my number in ' + str(guessesTaken) + ' guesses!') 
   else:   
       print('Nope. The number I was thinking of was ' + str(secretNumber))

