#1 Classify a person age group: Chlid(<13),Teenager(13-19),Adult(20-59),Senior(60+)
# age = int(input("Provide a age number:"))
# if age < 13:
#     print("Child")
# elif age <20:
#     print("Teenager")
# elif age < 60:
#     print("Adult")
# else:
#     print("Senior")

#2 Movie tickets are priced based on age: $12 for adults(18 and over),$8 for children.Everyone gets a discount on Wednesday  

# age = int(input("Enter the age:"))
# day = input("Enter the following day:")

# price = 12 if age >= 18 else 8

# if day == "Wednesday":
#     price = price - 2

# print("Ticket price for you is $", price)

#3 Assign a letter grade based on a student score:A(90-100),B(80-89),C(70-79),F(below 60)
# marks = int(input("Enter the marks:"))
# if marks>=101:
#     print("Please verify your marks again")
#     exit()

# if marks>=90:
#     grade = "A"
# elif marks>=80:
#     grade = "B"
# elif marks>=70:
#     grade = "C"
# elif marks>=60:
#     grade = "D"
# else:
#     grade = "F"
# print("Grade:",grade)

# 4 Determine if a fruit is ripe,overripe,or unripebased on its colour
# fruit = input("Enter your fruit:")
# color = input("Enter yout fruit color:")

# if color == "green":
#     print("Status of fruit: Unripe")
# elif color == "yellow":
#     print("Status of fruit: Ripe")
# elif color == "brown":
#     print("Status of fruit: Overripe")

# 5 Suggest an activity based on whether

# weather = input("Enter today weather")

# if weather == "Sunny":
#     activity = "Go for a walk"
# elif weather == "Rainy":
#     activity = "Read a book"
# elif weather == "Snowy":
#     activity = "Build a snowman"
# else:
#     activity = "Invalid weather input,Pls try Sunny,Rainy,Snowy"

# print(activity)

# 6 Choose a mode of transportation based on distance
# distance =int(input("Enter the distance:"))

# if distance < 3:
#     transport = "Walk"
# elif distance <=15:
#     transport = "Bike"
# else:
#     transport = "Car"
# print("We recommends you the transport of:",transport)

#7 Customize a coffe order:Small,Medium,Large with extra shot of expresoo
# order_size = input("Enter coffee size:")
# extra_shot = input("Enter extra shot:")

# if extra_shot == "True":
#     coffee = order_size + "coffee with extra shot"
# else:
#     coffee = order_size + "coffee"

# print("Order:",coffee)

#8 Password strength checker
# password =input("Enter your password:")

# if len(password) < 6:
#     strength = "Weak"
# elif len(password) <= 10:
#     strength = "Medium"
# else:
#     strength = "Strong"

# print("Password strength is:",strength)

# 9 Determine its a leap year 
# year = int(input("Enter the year:"))

# if (year % 400 == 0) or (year % 4 == 0 and year % 100 !=0):
#     print(year,"is a leap year")
# else:
#     print(year,"is NOT a leap year")

# 10Recommned a type of pet food based on pet's species and age.(Dog:<2yrs-Puppy food,cat>5yrs Senior cat food)
species = input("Enter pet species:")
age = int(input("Enter the age:"))

if species == "Dog":
    if age <2:
        print("Recommend :Puppy Food")
    elif species == "Cat":
        if age <6:
            print("Recommend Senior cat food")
else:
    print("Sorry,we only have recommendation for dogs and cat this time")
    