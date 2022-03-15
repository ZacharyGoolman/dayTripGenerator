

# lists created for users random selection

Destinations = ["New York" , "Washington" , "North Carolina" , "Ohio"]

Mode_of_transportation = ["Rental car" , "Subway" , "Bus" , "Limousine"]

Restaurants = ["Aces perfect Pizza" , "Barmini" , "Mayflower Seafood" , "Pies's And Pints"]

Entertainment = ["Broadway musical" , "Indy car race" , "Hike Mt Rainier" , "Snowboarding"]

#Destinations randomizer function from [list] for user
import random

location = (random.choice(Destinations))
print(location)

def destination():
   
   users_choice = ("No")
   
   while users_choice == ("No"):
      
      users_choice = (input("Does this destination sound Ideal?"))
      
      if users_choice == ("Yes"):
         print("Awesome I'm glad that locatin worked out!")
      
      elif users_choice == ("No"):
         location = (random.choice(Destinations))
         print("How do this location sound" + " " + location)
      
destination()         

# Transportation randomizer function from [list] for user

transportation = (random.choice(Mode_of_transportation))
print(transportation)

def travel_means():
   
   users_choice = ("No")
   while users_choice == ("No"):
      
      users_choice = (input("Do you like this mode of Transportation?"))

      if users_choice == ("Yes"):
         print("Awesome were glad that we were able to find a suitable mode of transportation for you!")
      
      elif users_choice == ("No"):
         transportation = (random.choice(Mode_of_transportation))
         print("I'm sorry that transportation was'nt well suited for you how about a" + " " + transportation + "?")

travel_means()


#Restaurants randomizer function from [list] for user

food = (random.choice(Restaurants))
print(food)

def choice_of_food():
   
   users_choice = ("No")
   while users_choice == ("No"):
      
      users_choice =(input("Does this dining option sound like a good choice?"))
      
      if users_choice == ("Yes"):
         print("Great choice! This is a local favorite")
      
      elif users_choice == ("No"):
         food = (random.choice(Restaurants))
         print("Does this" + " " + food + " " + "sound like a better option?")

choice_of_food()

#Entertainment randomizer function from [list] for user

enjoyment = (random.choice(Entertainment))
print(enjoyment)

def activities():
   
   users_choice = ("No")
   while users_choice == ("No"):
      
      users_choice =(input("Does this activity sound enjoyable?"))
      
      if users_choice == ("Yes"):
         print("What a fantastic choice, you are going to have a great time!")
      
      elif users_choice == ("No"):
         enjoyment = (random.choice(Entertainment))
         print("Does" + " " + enjoyment + " " + "sound to you?")

activities()


def confirm():
   print("We are excited to tell you that you have completed all the necessary step required of you and now you can relax knowing that your vacation is planned")
   users_choice = ("No")
   while users_choice == ("No"):
      
      users_choice = (input("Please Re read your selections above and confirm with a simple Yes or No that what is listed is correct and too your satisfaction"))
      if users_choice == ("Yes"):
         print("Thank you for your comnfirmation")
      elif users_choice == ("No"):
         print("Thats ok let's start over and create your dream day no need to settle!")


confirm()

def display():
   print("As confirmed above we are excited to present to you a breakdown of your completed Vacation day trip and we know you are going to have a wonderful time. Thank you for using DayTrip and we hope you have the best randomly created vacation ever!")
   for items in location ,transportation ,food, enjoyment:
      print(items)

display()
