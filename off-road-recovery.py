#Define Functions

def welcome_message():
    print("Welcome to the Off-Road_Recovery App!")
    border_line()
    print("Choose an option: " "\n""1. I need recovery assistance" "\n""2. I want to assist in recovery""\n")
    menu_input(need_assist,offer_assist)
    
    
def border_line():
    print("-" * 40)

need_assist = True
offer_assist = True

def menu_input(need_assist, offer_assist):
    print(input("Enter option: "))
    if need_assist == True:
        need_assist_intake()
    elif offer_assist == True:
        offer_assist_intake()
    else:
        print("Please enter a valid option")

def need_assist_intake():
    name = input("Name: ")
    location = input("Location: ")
    vehicle_make = input("Vehicle Make: ")
    vehicle_model = input("Vehicle Model: ")
    recovery_desc = input("Description of Recovery Needs: ")
    print(name,"\n",location,"\n",vehicle_make,"\n",vehicle_model,"\n",recovery_desc, "\n")

def offer_assist_intake():
    name = input("Name: ")
    location = input("Location: ")
    vehicle_make = input("Vehicle Make: ")
    vehicle_model = input("Vehicle Model: ")
    recovery_gear = input("List of Recovery Gear:  ")
    print(name,"\n",location,"\n",vehicle_make,"\n",vehicle_model,"\n",recovery_gear, "\n")

welcome_message()
#Test Code
