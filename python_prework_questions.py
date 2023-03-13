#python_prework_questions
#Question 1
#Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below.
#def hello_name(user_name):
hello_name = input("What is your name? ")
print(f"hello_" + hello_name + "!")
#Question 2
#Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing
#def first_odds():
for i in range(1, 101, 2):
    print(i)
#Question 3
#Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.
#def max_num_in_list(a_list):
def max_num_in_a_list(a_list):
    if not a_list:
        return None
    max_num = a_list[0]
    for num in a_list:
        if num > max_num:
            max_num = num
    return max_num
#Question 4
#Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).
#def is_leap_year(a_year):
def is_leap_year(year):
    if year / 4 == 0:
        if year / 100 == 0:
            if year / 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    #Question 5
# Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.
# def is_consecutive(a_list):
def is_consecutive(a_list):
    if len(a_list) == 0:
        return False
    min_num = min(a_list)
    max_num = max(a_list)
    if max_num - min_num != len(a_list) -1:
        return False
    for i in range(len(a_list)):
        if a_list[i] != min_num + i:
            return False
    return True

# Chapter 2
print("Hello Python world!")
message = "Hello Python world!"
print(message)
message = "Hello Python Crash Course world!"
print(message)
message = "Hello Python Crash Course reader!"
print(message)
#2-1. Simple Message
weather_message = "It is currently 39 degrees fahrenheit"
print(weather_message)
#2-2. Simple Messages
weather_message2 = "It is mostly sunny out."
print(weather_message2)
weather_message2 = "It is raining."
print(weather_message2)
#name.py
name = "ada lovelace"
print(name.title())
name = "Ada Lovelace"
print(name.upper())
print(name.lower())
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print(full_name)
print("Hello, " + full_name.title() + "!")
message = "Hello, " + full_name.title() + "!"
print(message)
# using \t adds a tab to text
print("Python")
print("\tPython")
# \n: adds a new line in a string
print(("Languages:\nPython\nC\nJavaScript"))
# tabs and new lines can be combined
print("Languages:\n\tPython\n\tC\n\tJavaScript")
# white space can be stripped
favorite_language = 'python  '
print(favorite_language)
favorite_language.rstrip()
print(favorite_language.rstrip())
print(favorite_language)
favorite_language = 'python '
favorite_language = favorite_language.rstrip()
print(favorite_language)
favorite_language = ' python '
print(favorite_language.lstrip())
print(favorite_language.strip())
# use double quotes in messages instead of single quotes
message = "One of Python's strengths is its diverse community."
print(message)
#2-3 Personal Message
friend = "Sam"
print(friend)
message = "Hello" + " " + friend + "," + " " + "I am learning Python."
print(message)
#2-4 Name Cases
friend_2 = "Whitney"
print(friend_2.upper())
print(friend_2.lower())
print(friend_2.title())
#2-5 Famous Quote, use \ before quotation marks to have them printed
famous_person = "Walt Disney"
print(famous_person)
quote = famous_person + " " + "once said, \"If you can dream it, you can do it!\""
print(quote)
famous_person_2 = "Maya Angelou"
message = famous_person_2 + " " + "once said, \"We may encounter many defeats but we must not be defeated.\""
print(message)
# 2-6 Stripping Names
name = "\tMeg\n"
print(name)
print(name.lstrip())
print(name.rstrip())
print(name.strip())
# birthday.py - need to add "str" in front of a number if it will be part of a string
age = 32
birthday_message = "Happy " + str(age) + "nd Birthday!"
print(birthday_message)
#2-8 Number Eight
print(7+1)
print(2*4)
print(12-4)
print(16/2)
fav_num = 24
fav_num_message = "My favorite number is " + str(fav_num) + "."
print(fav_num_message)
# The Zen of Python, by Tim Peters
import this

# Chapter 3
# Lists
#bicycles.py
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0])
print(bicycles[0].title())
print(bicycles[1])
print(bicycles[3])
print(bicycles[-1])
message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)
# 3-1 Names
names = ['Sam', 'Meg', 'Whitney', 'Jon']
print(names[0])
print(names[1])
print(names[-1])
print(names[-2])
#3-2 Greetings
print("Hi " + names[0] + "! " "What are you doing this weekend?")
print("Hi " + names[1] + "! " "What are you doing this weekend?")
print("Hi " + names[2] + "! " "What are you doing this weekend?")
print("Hi " + names[3] + "! " "What are you doing this weekend?")
# 3-3 Your Own List
fav_cars = ['bmw convertible', 'ford mustang', 'chevy camaro']
print(fav_cars)
print("I would like to own a " + fav_cars[0].title() + "!")
print("I would like to own a " + fav_cars[1].title() + "!")
print("I would like to own a " + fav_cars[2].title() + "!")
# Modifying a List
#bicycles.py
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles[0] = 'ducati'
print(motorcycles)
# Adding elements to a list
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.append('ducati')
print(motorcycles)
# You can start with a blank list [] and then add to it with .append
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)
# You can insert items into a specific spot in a list
motorcycles = ['honda', 'yamaha', 'suzuki'] 
motorcycles.insert(0, 'ducati')
print(motorcycles)
# Removing an item using del (will no longer be able to access the value)
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
del motorcycles[0]
print(motorcycles)
del motorcycles[1]
print(motorcycles)
# pop() method removes the last item off the list and stores it in the pop value
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()
print("The last motorcycle I owned was a " + last_owned.title() + ".")
# pop() can also be used to remove an item from a specific place in a list
motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print('The first motorcycle I owned was a ' + first_owned.title() + '.')
# An item can be removed by value
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)
# Printing a reason for removing it from the list
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")
# 3-4 Guest List
guest_list = ['Walt Disney', 'Albert Einstein', 'Wolfgang Mozart']
invitation = ", " + "You are invited over for dinner on Friday at 7pm."
print(guest_list[0] + invitation)
print(guest_list[1] + invitation)
print(guest_list[2] + invitation)
# 3-5 Changing Guest List
print(guest_list[1] + " " + "is unable to make it to dinner.")
print(guest_list[0] + "," + " " + "Dinner will still occur as per your original invitation.")
print(guest_list[2] + "," + " " + "Dinner will still occur as per your original invitation.")
guest_list.remove('Albert Einstein')
print(guest_list)
#3-6 More Guests
print(guest_list[0] + "," + " " + "We have found a bigger table and two more guests will be invited.")
print(guest_list[1] + "," + " " + "We have found a bigger table and two more guests will be invited.")
guest_list.insert(0, 'Lucille Ball')
guest_list.insert(2, 'Leonardo Davinci')
guest_list.append('Abraham Lincoln')
print(guest_list)
print(guest_list[0] + "," + " " + "You are oficially invited to dinner at my house at 7pm on Friday.")
print(guest_list[1] + "," + " " + "You are oficially invited to dinner at my house at 7pm on Friday.")
print(guest_list[2] + "," + " " + "You are oficially invited to dinner at my house at 7pm on Friday.")
print(guest_list[3] + "," + " " + "You are oficially invited to dinner at my house at 7pm on Friday.")
print(guest_list[4] + "," + " " + "You are oficially invited to dinner at my house at 7pm on Friday.")
# 3-7 Shrinking Guest List
print(guest_list[0] + "," + " " + "Unfortunately, I can now only accomodate two people at dinner.")
print(guest_list[1] + "," + " " + "Unfortunately, I can now only accomodate two people at dinner.")
print(guest_list[2] + "," + " " + "Unfortunately, I can now only accomodate two people at dinner.")
print(guest_list[3] + "," + " " + "Unfortunately, I can now only accomodate two people at dinner.")
print(guest_list[4] + "," + " " + "Unfortunately, I can now only accomodate two people at dinner.")
popped_guest_list = guest_list.pop()
print(guest_list)
print(popped_guest_list + "," + " " + "I'm sorry, we can no longer accomodate you at dinner.")
popped_guest_list = guest_list.pop()
print(guest_list)
print(popped_guest_list + "," + " " + "I'm sorry, we can no longer accomodate you at dinner.")
popped_guest_list = guest_list.pop()
print(guest_list)
print(popped_guest_list + "," + " " + "I'm sorry, we can no longer accomodate you at dinner.")
print(guest_list[0] + "," + " " + "You are one of the lucky guests that can still come to dinner!")
print(guest_list[1] + "," + " " + "You are one of the lucky guests that can still come to dinner!")
del guest_list[1]
del guest_list[0]
print(guest_list)
# Organizing a List
#.sort() sorts alphabetically and is a permanent sort
#cars.py
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
#.sort(reverse=True) sorts in reverse alphabetical order
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)
#sorted() is a temporary change to the list
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)
# Printing in reverse order, will change original list
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()
print(cars)
# Finding the length of a list
cars = ['bmw', 'audi', 'toyota', 'subaru']
len(cars)
print(len(cars))
# 3-8 Seeing the World
travel_list = ['Lake Tahoe', 'Acadia National Park', 'Colorado', 'Italy', 'Iceland']
print(travel_list)
print(sorted(travel_list))
print(travel_list)
print(sorted(travel_list))
print(travel_list)
travel_list.reverse()
travel_list.reverse()
travel_list.sort()
print(travel_list)
travel_list.sort()
travel_list.sort(reverse=True)
print(travel_list)
# 3-9 Dinner Guests
print(len(guest_list))
# 3-10 Every Function
breakfast_foods = ['bacon', 'cereal', 'eggs', 'sausage', ]
print(breakfast_foods)
print(breakfast_foods[0])
print(breakfast_foods[0].title())
print(breakfast_foods[1])
print(breakfast_foods[3])
print(breakfast_foods[-1])
message = "My favorite thing to eat in the morning are " + breakfast_foods[2] + "."
print(message)
breakfast_foods[1] = 'oatmeal'
print(breakfast_foods)
breakfast_foods.append('pancakes')
print(breakfast_foods)
breakfast_beverages = []
print(breakfast_beverages)
breakfast_beverages.append('coffee')
breakfast_beverages.append('tea')
breakfast_beverages.append('juice')
print(breakfast_beverages)
breakfast_foods.insert(1, 'waffles')
print(breakfast_foods)
del breakfast_foods[1]
print(breakfast_foods)
popped_breakfast_foods = breakfast_foods.pop()
print(breakfast_foods)
print(popped_breakfast_foods)
last_eaten = popped_breakfast_foods
print(last_eaten)
print("The last thing I ate were some " + last_eaten + ".")
first_eaten = breakfast_foods.pop(0)
print('The first thing I ate today was ' + first_eaten + ".")
print(breakfast_foods)
already_eaten = 'sausage'
breakfast_foods.remove(already_eaten)
print(breakfast_foods)
print("\n" + already_eaten.title() + " is off the menu.")
print(breakfast_foods)
breakfast_foods = ['bacon', 'cereal', 'eggs', 'sausage', 'pancakes', 'waffles']
breakfast_foods.sort()
print(breakfast_foods)
breakfast_foods.sort(reverse=True)
print(breakfast_foods)
breakfast_foods = ['bacon', 'cereal','waffles', 'eggs', 'sausage', 'pancakes']
print("Here is the original list:")
print(breakfast_foods)
print("\nHere is the sorted list:")
print(sorted(breakfast_foods))
print("\nHere is the original list again:")
print(breakfast_foods)
breakfast_foods = ['bacon', 'cereal','waffles', 'eggs', 'sausage', 'pancakes']
print(breakfast_foods)
breakfast_foods.reverse()
print(breakfast_foods)
print(len(breakfast_foods))
breakfast_foods = ['bacon', 'cereal','waffles', 'eggs', 'sausage', 'pancakes']
print(breakfast_foods[3])
print(breakfast_foods[-1])
# Chapter 4 - Working with Lists
# magigians.py
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
for magician in magicians:
        print("I can't wait ot osee your next trick, " + magician.title() + ".\n")
for magician in magicians:
     print(magician.title() + ", that was a great trick!")
     print("I can't wait to see your next trick, " + magician.title() + ".\n")
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick," + magician.title() + ".\n")
# 4-1 Pizzas
print("Thank you, everyone. That was a great magic show!")
pizzas = ['buffalo', 'cheese', 'mushroom']
for pizza in pizzas:
    print("I love " + pizza + " " + "pizza" + "!")
print("\n I love all kinds of pizza!")
# 4-2 Animals
animals = ['cat', 'dog', 'rabbit' 'lizzard', 'goat']
for animal in animals:
     print("I would like to have a " + animal + " as a pet.")
print("These would all make great pets!")
# numbers.py
for value in range(1,5):
    print(value)
for value in range(1,6):
     print(value)
# even_numbers.py
even_numbers = list(range(2,11,2))
print(even_numbers)
# squres.py (** = exponents)
squares = []
for value in range(1,11):
     square = value**2
     squares.append(square)
print(squares)
squares = []
for value in range(1,11):
        squares.append(value**2)
print(squares)
# Simple Statistics with a List of Numbers
digits = [1,2,3,4,5,6,7,8,9,0]
print(min(digits))
print(max(digits))
print(sum(digits))
# Using a list comprehension
# squares.py
squares = [value**2 for value in range(1,11)]
print(squares)
# 4-3 Counting to Twenty
for value in range(1,21):
    print(value)
# 4-4 One Million
# for value in range(1, 1000001):
#    print(value)
# 4-5 Summing a Million
digits = [1,1000000]
print(min(digits))
print(max(digits))
print(sum(digits))
# 4-6 Odd Numbers
for i in range(1,21,2):
     print(i)
# 4-7 Threes
multiples = []
print("every 3rd number")
for value in range(3,31,3):
    print(value)
# 4-8 Cubes
cubes = []
for value in range(1,11):
     cube = value**3
     cubes.append(cube)
print(cubes)
# 4-9 Cube Comprehension
cubes = []
for value in range(1,11):
     cubes.append(value**3)
print(cubes)
# Slicing a list
#players.py
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
# Looping Through a Slice
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team:")
for player in players[:3]:
     print(player.title())
# Copying a list
# foods.py
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)
# 4-10 Slices
animals = ['cat', 'dog', 'rabbit', 'lizzard', 'goat']
print("The first three items in this list are as follows:")
for animal in animals[:3]:
     print(animal.title())
print("Three animals in the middle of the list are:")
for animal in animals[1:4]:
    print(animal)
print("The last three animals are:")
for animal in animals[-3:]:
    print(animal)
# 4-11 My Pizzas, Your Pizzas:
pizzas = ['buffalo', 'cheese', 'mushroom']
friends_pizzas = pizzas[:]
print(friends_pizzas)
pizzas.append('sausage')
print(pizzas)
friends_pizzas.append('cheese')
print(friends_pizzas)
print(pizzas)
print("The best pizzas are:")
print(pizzas)
print("My friend's favorite toppings are:")
print(friends_pizzas)
my_foods = ['pizza', 'falafel', 'carrot cake']
my_friend_foods = my_foods[:]
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)
for food in my_foods[1:4]:
    print(food)
for food in my_friend_foods[-3:]:
    print(food)
# dimensions.py
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
dimensions = (200, 50)
for dimension in dimensions:
        print(dimension)
# Writing over a Tuple
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
     print(dimension)
dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
     print(dimensions)
# 4-13 Buffet NEED HELP

#Chapter_5.py
#cars.py
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
car = 'bmw'
car == 'bmw'
print(car=='bmw')
car = 'audi'
print(car=='bnw')
# A double equal sign asks the question "Is the value of car equal to 'bmw'?"
# Upper and Lower Case Matters
car = 'Audi'
car.lower() == 'audi'
print(car.lower() == 'audi')
# An exclaimation point means "not"
#toppings.py
requested_topping = 'mushroom'
if requested_topping != 'anchovies':
    print("Hold the anchovies!")
# magic.number.py
answer = 17
if answer != 42:
    print("That is not the correct answer. Please try again!")
age_0 = 22
age_1 = 18
print(age_0 >=21 and age_1 >=21)
# To find out whether a particular value is already in a list, use the key-word "in."
requested_toppings = ['mushrooms', 'onions' 'pineapple']
'mushrooms' in requested_toppings
print('mushrooms' in requested_toppings)
print('pepperoni' in requested_toppings)
# Use keyword "not" it know if a value does not appear in a list
#banned_users.py
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print(user.title() + ", you can post a response if you wish.")
# Boolean values track the state of a condition
# game_active = True
# can _edit = False
# 5-1 Conditional Tests
vacation = 'Virgin Islands'
print("Is vacation == 'Virgin Islands'? I predict True.")
print(vacation == 'Virgin Islands')
print("\nIs vacation == 'Puerto Rico'? I predict False.")
print(vacation == 'Puerto Rico')
# 5-2 More Conditional Tests
vacation = 'Virgin Islands'
print("Is vacation == 'Virgin_Islands'? I predict True.")
print(vacation == 'Virgin_Islands')
print("\nIs vacation == 'Puerto_Rico'? I predict False.")
print(vacation == 'Puerto_Rico')
#voting.py
age = 19
if age >= 18:
    print("You are old enough to vote!")
age = 17
if age >= 18:
    print("You hare old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")
# amusement_park.py
age = 12
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $5.")
else:
    print("Your admission ost is $10.")
#if-elif-else block
age = 12
if age < 4:
    price = 0
elif age <18:
    price = 5
else:
    price = 10
print("Your admission cost is $" + str(price) + ".")
#toppings.py
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    print("Adding " + requested_topping + ".")
print("\nFinished making your pizza!")
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print("Adding " + requested_topping + ".")
print("\nFinished amking your pizza!")
requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".")
else:
    print("Are you sure you want a plain pizza?")
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")
print("\nFinished making your pizza!")
# 5-3 Alien Colors #1
alien_colors = ['green', 'yellow', 'red']
if 'green' in alien_colors:
    print("You have won five points!")
if 'yellow' in alien_colors:
    print("Better luck next time!")
if 'red' in alien_colors:
    print("Better luck next time!")
# 5-4 Alien Colors #2
alien_colors = ['green', 'yellow', 'red']
if 'green' in alien_colors:
    print("You have won 5 points!")
if 'yellow' in alien_colors:
    print("You have earned 10 points!")
if 'red' in alien_colors:
    print("You have earned 10 points!")
# 5-5 Alien Colors #3
alien_colors = 'green'
if alien_colors == 'green':
    print("You have won 5 points!")
alien_colors = 'yellow'
if alien_colors == 'green':
    print("You have won 5 points!")
alien_colors = 'yellow'
if alien_colors == 'green':
    print("You have won 5 points!")
else:
    print("You have won 10 points")
alien_colors = 'green'
if alien_colors == 'green':
    print("\nYou have won 5 points!")
else:
    print("You have won 10 points")
# 5-5 Alien Colors #3
alien_colors = 'red'
if alien_colors == 'green':
    print("You have won 5 points!")
elif alien_colors == 'yellow':
    print("You have won 10 points")
else:
    print("You have won 15 points!")