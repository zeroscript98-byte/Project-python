import random
print(f"{"="*10}GUESS THE NUMBER BETWEEN 0 TO 100{"="*10}")
while True:
  val=True
  val2=True
  chache=0
  mistakes=0
  number=random.randint(0,100)
  print("Number created")
  while True:
    diff=str(input("Select the difficulty:\n1.Easy (15 chance) \n2.Medium (10 chache) \n3.Hard (5 chache) \n "))
    if diff == "1":
      chache = 15
      print(f"The difficulty has been set to easy \n you have 15 chache to try")
      break
    elif diff == "2":
      chache = 10
      print(f"The difficulty has been set to medium \n you have 10 chache to try")
      break
    elif diff == "3":
      chache = 5
      print(f"The difficulty has been set to hard \n you have 5 chache to try")
      break
    else:
      print("Input incorrect!\n ")
  while True:
    guess=int(input("Guess: \n"))
    if guess == number:
      print(f"Correct!!! the number is {number}")
      break
    elif guess > number and guess <= 100:
      print("Too high")
      print("Try again!")
      mistakes += 1
    elif guess < number:
      print("Too low")
      print("Try again!")
      mistakes += 1
    elif guess > 100:
      print("The number is out of range!")
      mistakesl += 1
    else:
      print("Input incorrect!")
    if mistakes == chache:
      print("Your chance is over",end=" ")
      print(f"The number is {number}")
      break
  while True:
    play=input("Want to play again(y/n)?")
    if play == "y":
     break
    elif play == "n":
     val=False
     break
    else:
      print("Input incorrect!")
      break
  if val == False:
    break