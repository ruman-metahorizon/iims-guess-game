import random

random_number = random.randint(0,100)

while True:
  user_input = int(input("Enter a number: "))
  if user_input == random_number:
    print("You won")
    break
  elif user_input > random_number:
    print("Too high")
  else:
    print("Too low")