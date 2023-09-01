#Udacity
import time
def welcome_text():
  print("Hey friend! What's your name") 
  name = input("Enter name:")
  print("Hey " +  name)
  age = int(input("How old are you? "))
  if age < 9:
    print("Wow you're a baby!")
  elif age < 18:
    print("Hey! How's school are you looking forward         for highschool!")
  elif age < 25:
    print("How's college?")
  else: 
    print("how's work") 
  user_response = input("would you like to see a menu of other options I can do?(yes/no):")
  #W3schools
  if user_response.lower() == "yes":
    print("1.Great here are somethings I can do!")
    print("2.The Weather")
    print("3.The current time")
    print("4.Current news and events")
    print("5.Stop and Exit chat bot")
  elif user_response.lower() == "no": 
    print("okay maybe next time!")
    time.sleep(3)
    exit()
  user_choice = input("Choose a number ")
  if user_choice == "5":
    print("Okay, I'll talk to you later Bye!")
    time.sleep(3)
  exit()

  
welcome_text()





