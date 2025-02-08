#RPS.py
#Name:
#Date:
#Assignment:
import random

def main():
  wins = 0
  ties = 0
  losses = 0

  #loop start
  while True:
    #random rock paper scissors result
    choices = ['Rock', 'Paper', 'Scissors'] 
    computer_choice = random.choice(choices)

    #ask for player input
    player_choice = input("Choose your Weapon (Rock, Paper, Scissors): ").capitalize()
    while player_choice not in choices:
       print("Invalid input! Please enter 'Rock', 'Paper', or 'Scissors'.")
       player_choice = input("Enter your choice (Rock, Paper, Scissors): ").capitalize()

    #display computer choices (PUT # SO THAT IT DOESNT DISPLAY RESULTS 2x)
    #if computer_choice == 'Rock':
      #print('Computer chose Rock')
    #elif computer_choice == 'Paper':
      #print('Computer chose Paper')
    #elif computer_choice == 'Scissors':
      #print('Computer chose Scissors')

    #display player choices
    #if player_choice == 'Rock':
      #print('Player chose Rock')
    #elif player_choice == 'Paper':
      #print('Player chose Paper')
    #elif player_choice == 'Scissors':
      #print('Player chose Scissors')
    
    #who wins?
    if player_choice == computer_choice:
      print(f"Both chose {player_choice}. It's a tie!")
      ties += 1
    elif (player_choice == 'Rock' and computer_choice == 'Scissors') or \
      (player_choice == 'Paper' and computer_choice == 'Rock') or \
      (player_choice == 'Scissors' and computer_choice == 'Paper'):
      print(f"You chose {player_choice} and the computer chose {computer_choice}. You win!")
      wins += 1
    else:
      print(f"You chose {player_choice} and the computer chose {computer_choice}. You lose.")
      losses += 1

    # Ask if the player wants to play again
    play_again = input("Do you want to play again? (Y/N): ").capitalize()
    if play_again != 'Y':
      break

    # In the end, print the stats
    print("\nGame Stats:")
    print("Wins \t Ties \t Losses")
    print("---- \t ---- \t ------")
    print(wins, "\t", ties, "\t", losses)

if __name__ == '__main__':
    main()
