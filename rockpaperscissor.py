import random
print('welcome to Rock, Paper and scissor. goodluck')
user_choice = input("Choose Rock, Paper, or Scissors: ").lower()
if(user_choice == 'scissors' or user_choice == 'paper' or user_choice == 'rock'):
  print(f'user choice: {user_choice}')
  random_value = random.randint(1, 3)
  
  if random_value == 1:
      computer_choice = "rock"
  elif random_value == 2:
      computer_choice = "paper"
  elif random_value == 3:
      computer_choice = "scissors"
  else:
      print("Something went wrong with RANDOM")
  
  print(f'computer choice: {computer_choice}')
    #check who wins
  if user_choice == computer_choice:
    print('Draw!')
  elif user_choice == 'rock' and computer_choice == 'scissors':
    print('Rock smashes Scissors. You win!')
  elif user_choice == 'paper' and computer_choice == 'rock':
    print('Paper covers Rock. You win!')
  elif  user_choice == 'scissor' and computer_choice == 'paper':
    print('Scissors cut Paper. You win!')
  else:
    if user_choice == 'scissors' and computer_choice == 'rock':
      print('Rock smashes Scissors. You lose!')
    elif user_choice == 'rock' and computer_choice == 'paper':
      print('Paper covers Rock. You lose!')
    elif  user_choice == 'paper' and computer_choice == 'scissors':
      print('Scissors cut Paper. You lose!')
else:
  print('invalid input. Rock, Paper, and Scissors are the only choices allowed ')
    
  