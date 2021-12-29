print("Welcome to the most Awesome Game!")
name = input("What's your name? ")
age = int(input("How old are you? "))

if age <= 20:
    print("Sorry, you are not eligible to play the game")
    exit()
else:
    print("First contestant's name is ", name, "and they are", age, "years old!")

wants_to_play = input("Are you ready to play?")
if wants_to_play == "Yes":
    print("Let's start our 1st round!")
else:
    print("No problem! Who is our next contestant?")
