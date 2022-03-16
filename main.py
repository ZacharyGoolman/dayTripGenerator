

# lists created for users random selection

Destinations = ["New York" , "Washington" , "North Carolina" , "Ohio"]

Mode_of_transportation = ["Rental car" , "Subway" , "Bus" , "Limousine"]

Restaurants = ["Aces perfect Pizza" , "Barmini" , "Mayflower Seafood" , "Pies's And Pints"]

Entertainment = ["Broadway musical" , "Indy car race" , "Hiking Mt Rainier" , "Snowboarding"]

#Destinations randomizer function from [list] for user
import random
location = (random.choice(Destinations))


def destination():
   
   print("Thank you so much for choosing Day Trip. Allow us to remove all of the stress of creating your Vacation, so that you may enjoy it to your fullest capability!")
   
   users_choice = ("No")
   
   while users_choice == ("No"):
      location = (random.choice(Destinations))
      users_choice = (input("We have selected" + " " + location + " " + "for you? How does this sound? Please confirm with a Yes or No"))
      
      if users_choice == ("Yes"):
         print("Awesome, we're glad that location worked out! Now that we have confirmed where you would like to travel too lets decide on transportation.")
      
      elif users_choice == ("No"):
         print("Sorry that didnt work lets try to select another option")
      
destination()         

# Transportation randomizer function from [list] for user
transportation = (random.choice(Mode_of_transportation))

def travel_means():
   
   users_choice = ("No")
   
   while users_choice == ("No"):
      transportation = (random.choice(Mode_of_transportation))
      users_choice = (input("We have selected a" + " " + transportation + " " + "for your means of Transportation. How does this sound? Please confirm with Yes or No."))

      if users_choice == ("Yes"):
         print("Awesome, now that we have Transportation taking care of lets work on finding you a fantastic place to eat!")
      
      elif users_choice == ("No"):
         print("I'm sorry that transportation was'nt well suited for you. Let's try to find a better option.")

travel_means()


#Restaurants randomizer function from [list] for user
food = (random.choice(Restaurants))
def choice_of_food():
   
   users_choice = ("No")

   while users_choice == ("No"):
      food = (random.choice(Restaurants))
      users_choice =(input("We have selected" + " " + food + " " + "for the choice of dining. How does this sound? Please confirm with a Yes or No."))
      
      if users_choice == ("Yes"):
         print("Great choice! This is a local favorite. Now that we have your Dining for the evening taken care of let's find you some Entertainment/activities!")
      
      elif users_choice == ("No"):
         print("Sorry that did'nt work out. Lets see if we can find a better Dining option more suited for you.")

choice_of_food()

#Entertainment randomizer function from [list] for user
enjoyment = (random.choice(Entertainment))

def activities():
   
   users_choice = ("No")
   while users_choice == ("No"):
      enjoyment = (random.choice(Entertainment))
      users_choice =(input("We have selected" + " " + enjoyment + " " + "for you. Does this sound like a great activity for the day? Please Confirm with a Yes or No."))
      
      if users_choice == ("Yes"):
         print("What a fantastic choice, you are going to have a great time!")
      
      elif users_choice == ("No"):
         print("That's Ok let's pick another activity for you to do while on your trip.")

activities()

def display():
   print("Congratulations! You have completed your trip itenary")
   print("As confirmed above in your selections we are excited to present to you a breakdown of your completed Vacation day trip and we know you are going to have a wonderful time. Thank you for using DayTrip and we hope you have the best randomly created Vacation ever!")
   for items in location ,transportation ,food, enjoyment:
      print(items)

display()
