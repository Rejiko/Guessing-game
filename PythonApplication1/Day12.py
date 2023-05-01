import random
RANDOM_NUM = random.randint(1,100)

def game(num):
    for i in range(num, 0, -1):
        print(f"You have {i} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess == RANDOM_NUM:
            print(f"You guessed correctly, the number was {RANDOM_NUM}")
            break
        elif guess > RANDOM_NUM:
            print("Too high")
        elif guess < RANDOM_NUM:
            print("Too low")
        if i > 1:
            print("Guess again")
    if guess != RANDOM_NUM:
        print(f"You have ran out of attempts, the correct number was {RANDOM_NUM}")

def difficulty():
    if difficulty_choice == 'easy':
        game(10)
    elif difficulty_choice == 'hard':
        game(5)

print("Welcome to the Number Guessing Game!")
print("I'm thiking of a number between 1 and 100.")
difficulty_choice = input("Choose a difficulty. Type 'easy' or 'hard': ")
difficulty()