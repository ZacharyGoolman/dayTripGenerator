# make 4 lists. lists should be the only thing outside of the function. 


Destinations = ["New York" , "Washington" , "North Carolina" , "Ohio"]

Mode_of_transportation = ["Rental car" , "Subway" , "Bus" , "Limousine"]

Restaurants = ["Aces perfect Pizza" , "Barmini" , "Mayflower Seafood" , "Pies's And Pints"]

Entertainment = ["Broadway musical" , "Indy car race" , "Hike Mt Rainier" , "Snowboarding"]

#Destinations  list Function
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

  
#    if users_choice == True: 
#       print("Awesome, I'm glad we found your destination!")
#    else:
#       print("I'm sorry lets try another selection")


# #call my function

# print("Would" " " + random.choice(Destinations) +  " " "be better suited for your travel?") 
# print("Ok great lets find you some Transportation!")









# print(random.choice(Mode_of_transportation))
# print(random.choice(Restaurants))
# print(random.choice(Entertainment))
