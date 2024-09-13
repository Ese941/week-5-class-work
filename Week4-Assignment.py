print("Hello, please select the app you want to use.")
print(" 1. Menu \n 2. Calculator \n 3. Age Checker \n 4. String Manipulator \n 5. Quiz \n 6. Treasure Island Game \n")
user=input("Enter the name of the app you want to use: ")
if user == "Menu":
  print(" Hello,welcome to Aloine Drink Store.I am here to assist you with your order.\n")
  print("Here's a list of what's available:")
  print(" Cappuccino \n Latte \n Americano \n Espresso \n Mocha \n")
  feed=input("What would you like to order? \n").lower()
  if feed == "cappuccino":
    print("What a great choice! that would cost you $5.00")
  if feed == "latte":
    print("What a great choice! that would cost you $4.00")
  if feed == "americano":
    print("What a great choice! that would cost you $9.00")
  if feed == "espresso":
    print("What a great choice! that would cost you $11.00")
  if feed == "mocha":
    print("What a great choice! that would cost you $20.00")

  payment=input("How would you like to pay? \n").lower()
  if payment == "cash":
    print("Please pay to the lady at the counter.")
  elif payment == "card":
    print("Please swipe your card at the counter.")
  
  print("Thank you for your order, We will be with you shortly once payment has been made.")

if user == "Calculator":
  print("Hello, welcome to xendo calculator. I am here to assist you with some basic calculations like: \n Addition \n Subttraction \n Multiplication \n Division. \n")
  user=input("Which of these mathematical operations would you like to perform? \n").lower()
  if user == "addition":
    print("What two numbers would you like to add?")
    num1=float(input("Enter first number:"))
    num2=float(input("Enter second number:"))
    print(f"The addition of  both numbers is", ( num1 + num2))

  elif user == "subtraction":
    print("What two numbers would you like to subtract?")
    num1=float(input("Enter first number:"))
    num2=float(input("Enter second number:"))
    print(f"The subtractraction of both numbers is", (num1 - num2))

  elif user == "multiplication":
    print("What two numbers would you like to multiply?")
    num1=float(input("Enter first number:"))
    num2=float(input("Enter second number:"))
    print(f"The multiplication of both numbers is", (num1 * num2))

  elif user == "division":
    print("What two numbers would you like to divide?")
    num1=float(input("Enter first number:"))
    num2=float(input("Enter second number:"))
    print(f"The division of both numbers is", (num1 / num2))

  else:
    print("We don't perform that operation here.")

if user == "Age Checker":
  print("Hello, welcome to the age checker app. I am here to assist you with determining your age group")
  age=int(input("What is your age? \n"))
  if age <=12:
    print("You are a child")
  elif age <=18:
    print("You are a teenager")
  elif age <=30:
    print("You are a young adult")
  elif age <=50:
    print("You are an adult")
  elif age <=100:
    print("You are a senior")
  else:
    print("You are a centenarian")

if user == "String Manipulator":
  print("Welcome to  String Manupulator App! ")
  print("Choose one: \n 1. Switch to uppercase \n 2. Switch to lowercase \n 3. Reverse the string \n 4. Calculate the length \n 5. Find a letter in the string \n 6. Replace a letter in the string \n")
  user=input("Which of these would you like to perform ? ")
  if user == "1": 
    word=input("Enter a word:")
    print(word.upper())
   

  if user == "2":
    word=input("Enter a word:")
    print(word.lower())

  if user == "3":
     word=input("Enter a word:")
     print(word[::-1])

  if user == "4":
     word=input("Enter a word:")
     print(len(word))

  if user == "5":
     word=input("Enter a word:")
     letter=input("Enter a letter:")
     print(word.find(letter))

  if user == "6":
     word=input("Enter a word:")
     letter=input("Enter the first letter of the word:")
     letter2=input("Enter the letter you want to replace it with:")
     print(word.replace(letter,letter2))

if user == "Quiz":
  print("Welcome to the Quiz App! \n")
  name=input("Enter your name: ")
  print("Hello" + " " + name + " " + "lets begin the quiz")
  print("NOTE: \n -If your spelling is incorrect then it is considered as a wrong answer \n -Your answers must start with a capital letter")
  score = 0
  question_no = 0
  play=input("Do you want to play? (yes/no):")
  if play == "yes":
    question_no +=1
    ques = input(f" {question_no}. What is the capital of France? ")
    if ques == "Paris":
      score+=1
      print("Correct!")

    else:
       print("Incorrect!")
       print("The correct answer is Paris")
    question_no +=1
    ques = input(f" {question_no}. What is the capital of Germany? ")
    if ques == "Berlin":
      score+=1
      print("Correct!")

    else:
      print("Incorrect!")
      print("The correct answer is Berlin")

    question_no +=1
    ques = input(f" {question_no}. What is the capital of the United States? ")
    if ques == "Washington DC":
      score+=1
      print("Correct!")

    else:
        print("Incorrect!")
        print("The correct answer is Washington DC")

    
  else:
      print("You are out of the game")

  print(f"Number of questions is {question_no} ")
  print(f"Your score is {score}")
  print(f" {(score/question_no)*100}% of your answers were correct!")

if user == "Treasure Island Game":
  print("Welcome to Treasure Island Game. Your mission is to find the treasure.")
  direction=input("You are at a crossroad. Where do you want to go? Type 'left' or 'right' \n")
  if direction == "left":
      print("You have come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across.")
      action=input("What would you like to do?")
      if action == "wait":
         print("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?")
         colour=input("Which colour do you choose?")
         if colour == "red":
            print("It's a room full of fire. Game Over.")
         if colour == "yellow":
            print("You found the treasure! You Win!")
         if colour == "blue":
            print("You enter a room of beasts. Game Over.")

      elif action == "swim":
          print("You get attacked by an angry trout. Game Over.")

  elif direction == "right":
      print("You fell into a hole. Game Over.")

  print("Nice playing with you!")

  