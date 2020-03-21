#Ethan Kramer
#An integration of everything I have learned so far


def calculate_area_square():
    print("Calculate The Area of a Square")
    side = int(input("Enter the length of the side of a square to get the area:  "))  #PUT "INT" BEFORE SO IT ACTUALLY ADDS THE NUMBERS TOGETHER
    area_square = side ** 2
    print("The area of the square is", area_square)
    print("Exiting...")
    
def calculate_area_rectangle():
    print("Calculate The Area of a Rectangle")
    base = int(input("Enter the value of the base: "))
    height = int(input("Enter the value of the height: "))
    area_rectangle = base * height
    print("The area of this rectangle is", area_rectangle)
    print("Exiting...")
    
def calculate_area_triangle():
    print("Calculate The Area of a Triangle")
    base = float(input("Enter the value of the base: "))
    height = float(input("Enter the value of the height: "))
    area_triangle = (base * height) * 0.5
    print("The area of the triangle is", area_triangle)
    print("Exiting...")

def calculate_area_rhombus():
    print("Calculate The Area of a Rhombus")
    base = float(input("Enter the height of the rhombus: "))
    length = float(input("Enter the length of the rhombus: "))
    area_rhombus = (base * length) / 2
    print("The area of the rhombus is", area_rhombus)
    print("Exiting...")
    
#Main Menu
print("Hello!")
print("My name is Shmugman Jimmy, and I am your new virtual assistant.")
name = input("What's your name? ") # defines variable "name"
print("Sounds good!  It's a pleasure to meet you", name + ".")
do_again = True
while do_again:
    print("Welcome to the Shmugman Jimmy Abilities Menu.  My abilities include: ")
    print("1. Play Digital Ad Libs") #already made
    print("2. Area Calculator ") #as many shapes as possible...how much paint idea
    print("3. Basic Calculator ") 
    print("4. Blackjack") #can add functions
    print("How my I assist you today?")
    print("Enter 'quit' to exit the program.")
    user_input = (input("Enter the number that corresponds with the feature you would like to use here: "))
    if user_input == "quit":
        do_again = False

    #Digital Ad Libs
    elif user_input == "1":
        input("Hello, and welcome to digital ad libs!  Let's start by getting to know eachother a little better.  Type 'ok' to continue: ")
        food2 = input("What is your favorite category of food (Chinese, BBQ, Indian, etc.)?    ")
        animal = input("Name an animal you wish would go extinct.    ")
        print("Yeah,", animal + "s are pretty annoying.")
        dessert = input("What's your favorite type of dessert?    ")
        print("Somebody's got good taste!")
        part = input("Name a body part.    ")
        adj = input("Name an adjective.    ")
        smell = input("What smell makes you want to vomit?   ")
        sorority = input("Name a sorority.   ")
        music = input("Name a style of music.   ")
        bev = input("Name your go-to beverage.   ")
        print("One time, I came home from school in 4th grade and there was a", food2, animal, "eating a huge", dessert,
              "in my living room.  It started chasin' me around my house trying to bite my", part + ".  I think the ",
              dessert, "started bothering its stomach because it then let out a very", adj, "fart.  It smelled just like",
              smell + ".  I looked over my shoulder and saw the ", animal, "dancing to", music,
              "while drenching itself in the last of my", bev + ".")
        print("Thanks for playing!")
        print("Exiting back to the abilities menu...")


    #Area Calculator
    if user_input == "2":
        area_calculator = True
        while area_calculator:
            print("This program finds the area of any square, rectangle, triangle, or rhombus.")
            shape = input("Please specify 'square', 'rectangle', 'triangle', or 'rhombus'. To quit, type 'done':   ")
            if shape.lower() == "done":
                area_calculator = False
            if shape.lower() == "square":
                calculate_area_square()
            elif shape.lower() == "rectangle":
                calculate_area_rectangle()
            elif shape.lower() == "triangle":
                calculate_area_triangle()
            elif shape.lower() == "rhombus":
                calculate_area_rhombus()


#Basic Calculator
    if user_input == "3":
        basic_calculator = True
        while basic_calculator:
            print("Welcome to the Basic Calculator!")
            print("1. Addion")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")
            print("5. Square Root")
            print("6. Exponent")
            print("To exit the program, type 'quit'.")
            operation = input("Enter the number that corresponds to the operation you'd like to use here: ")
            if operation.lower() == "quit":
                calculator = False
            elif operation.lower() == "1":
                print("~Addition~")
                integers = int(input("Enter the number of integers you will be adding: "))
                total = 0
                for x in range(integers):
                    num = float(input("Enter a number to add: "))
                    total += num
                print("The total is", total, end = ".\n")
                print("Exiting...")
            if operation.lower() == "2":
                print("~Subtraction~")
                num1 = float(input("Enter the number you will be subracting from here: "))
                num2 = float(input("Enter the number you will be subtracting from the previous number here: "))
                difference = num1 - num2
                print("The difference of", num1, "and", num2, "is", difference)
            if operation.lower() == "3":
                print("~Multiplication~")
                num1 = float(input("Enter the first number you'd like to multiply: "))
                num2 = float(input("Enter the next number you'd like to multiply: "))
                product = num1 * num2
                print("The product is", product)
            if operation.lower() == "4":
                print("~Division~")
                num1 = float(input("Enter the dividend: "))
                num2 = float(input("Enter the divisor: "))
                quotient = num1 / num2
                print("The quotient is", quotient, end = ".\n")
            if operation.lower() == "5":
                print("~Square Root~")
                num = float(input("Enter the number you would like the square root of: "))
                root = pow(num, .5)
                print("The square root of", num, "is", root, end = ".\n")
            if operation.lower() == "6":
                print("~Exponent~")
                base = float(input("Enter the base: "))
                power = float(input("Enter the power: "))
                answer = pow(base, power)
                print("The value of", base, "to the power of", power, " is: ", answer, end = ".\n")


#Blackjack
    elif user_input == "4":
        print("Hello, and welcome to blackjack!  Get as high of a total as possible without going over 21!")
        import random
        total = 0
        input("To be dealt your first two cards, type 'go' : ")
        first_card = random.randint(1, 11)
        second_card = random.randint(1, 11)
        print("Your cards are: ", first_card, "and", second_card, end = ".\n")
        total = first_card + second_card
        print("Your current total is", total, end = ".\n")
        decision = input("Enter 'hit' or 'stand': ")
        while decision == "hit":
            card = random.randint(1, 11)
            print("Your next card is:", card, end = ",  ")
            total += card
            print("your new total is", total, end = ".  Don't go over 21!\n")
            decision = input("Enter 'hit' or 'stand': ")
        if decision == "stand":
            if total > 21:
                print("Your total is too high, you lose!")
            elif total <= 21:
                print("Your total is:", total, end = ".\n")
                print("You win!")