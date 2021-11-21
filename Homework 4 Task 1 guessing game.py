import random
 
secret_number = random.randint(1, 111)
tries, guess = 0, 0
while guess != secret_number:
    guess = int(input("Guess a number between one and ten: "))
    if guess > secret_number:
        print("Lower...")
    elif guess < secret_number:
        print("Higher...")
    tries += 1
 
print('You guessed it! The number was {} in {} tries'.format(guess, tries))