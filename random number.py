import random
from colorama import Fore, Style, init
import os

init()

# Clear screen function
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Game function
def play_game():
    number = random.randint(1, 100)
    attempts = 0

    print(Fore.CYAN + "\n🎮 Welcome to Number Guessing Game 🎮" + Style.RESET_ALL)
    print(Fore.YELLOW + "Guess a number between 1 and 100\n" + Style.RESET_ALL)

    while True:
        try:
            guess = int(input(Fore.GREEN + "Enter your guess: " + Style.RESET_ALL))
            attempts += 1

            if guess < number:
                print(Fore.BLUE + "📉 Too Low!\n" + Style.RESET_ALL)

            elif guess > number:
                print(Fore.MAGENTA + "📈 Too High!\n" + Style.RESET_ALL)

            else:
                print(Fore.YELLOW + f"\n🎉 Correct! The number was {number}" + Style.RESET_ALL)
                print(Fore.CYAN + f"✅ You guessed it in {attempts} attempts.\n" + Style.RESET_ALL)
                break

        except ValueError:
            print(Fore.RED + "❌ Please enter a valid number!\n" + Style.RESET_ALL)

# Main loop
while True:
    clear_screen()
    play_game()

    again = input(Fore.GREEN + "Do you want to play again? (yes/no): " + Style.RESET_ALL).lower()

    if again != "yes":
        print(Fore.RED + "\n👋 Thanks for playing!" + Style.RESET_ALL)
        break