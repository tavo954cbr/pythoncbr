import random

def choose_options():
  options = ('piedra','papel','tijera')
  user_option = input("piedra, papel o tijera =>")
  user_option = user_option.lower()

  if not user_option in options:
    print('Esa opcion no es valida')
    #continue
    return None, None

  computer_option = random.choice(options)

  print('User option =>', user_option)
  print('Computer option =>', computer_option)
  return user_option,computer_option

def check_rules(user_option, computer_option, user_wins, computer_wins):
  if user_option == computer_option:
    print("Empate!")
  elif user_option == "piedra":
    if computer_option == "tijera":
      print("piedra gana a tijera")
      print("user gano!")
      user_wins += 1
    else:
      print("papel gana a piedra")
      print("computer gano!")
      computer_wins += 1
  elif user_option == "papel":
    if computer_option == "piedra":
      print("papel le gana a piedra")
      print("user gano!")
      user_wins += 1
    else:
      print("tijera le gana a papel")
      print("computer gano!")
      computer_wins += 1
  elif user_option == "tijera":
    if computer_option == "papel":
      print("tijera le gana a papel")
      print("user gano!")
      user_wins += 1
    else:
      print("piedra le gana a tijera")
      print("computer gano!")
      computer_wins += 1
  return user_wins, computer_wins

def check_winer(user_wins, computer_wins):

    if computer_wins == 2:
      print('El computador gano!!')
      exit()
  
    if user_wins == 2:
      print('El usuario gano es pro!!')
      exit()

def run_game():
  computer_wins = 0
  user_wins = 0
  round = 1

  while  True:
  
    print('*' * 10)
    print('ROUND', round)
    print('*' * 10)
  
    print('conteo computador', computer_wins)
    print('conteo usuario', user_wins)
    round += 1
  
    user_option, computer_option = choose_options()
    user_wins, computer_wins = check_rules(user_option, computer_option,user_wins, computer_wins)
    check_winer(user_wins,computer_wins)
run_game()

#si puedes agregar emojis o algo mas es bien recibido, para mejorar el codigo.

