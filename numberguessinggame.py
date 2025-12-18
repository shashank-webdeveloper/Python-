import random

def number_guessing_game():
    print("The Number Guessing Game!")
    

    low_value = int(input("Enter the lower bound of the range: "))
    high_value = int(input("Enter the upper bound of the range: "))
    
    secret_number = random.randint(low_value, high_value)
    attempts = 0
    
    print(f"Guess the number between {low_value} and {high_value}!")
    
    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            
            if guess < low_value or guess > high_value:
                print(f"Please guess within range {low_value} to {high_value}.")
            elif guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed Number{secret_number} in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

number_guessing_game()
