#Define Functions

def welcome_message():
    print("Welcome to the Off-Road_Recovery App!")
    print("Choose an option: " "\n""1. I need recovery assistance" "\n""2. I want to assist in recovery""\n")
    border_line()
    
    
def border_line():
    print("-" * 40)

need_assist = ("1. I need assistance")
offer_assist = ("2. I want to offer assistance")

def choices(need_assist, offer_assist):
    if need_assist == 1:
        print(need_assist_intake)
    elif offer_assist == 2:
        return offer_assist_intake
    else: 
        print("Please enter option 1 or 2")

def need_assist_intake():
    print(name = input("Name: "))
    print(location = input("Location: "))
    print(vehicle_make = input("Vehicle Make: "))
    print(vehicle_model = input("Vehicle Model: "))
    print(recovery_desc = input("Description of Recovery Needs: "))  

def offer_assist_intake():
    print(name = input("Name: "))
    print(location = input("Location: "))
    print(vehicle_make = input("Vehicle Make: "))
    print(vehicle_model = input("Vehicle Model: "))
    print(recovery_gear = input("List of Recovery Gear:  "))

welcome_message()
#Test Code
