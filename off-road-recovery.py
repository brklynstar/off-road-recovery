#Define Functions

def welcome_menu():
    print("Welcome to the Off-Road_Recovery App!")
    border_line()
    print("Choose an option: " "\n""1. I need recovery assistance" "\n""2. I want to assist in recovery""\n")
    main_menu_input(need_assist,offer_assist)
    
    
def border_line(): 
    print("-" * 40)

need_assist = True
offer_assist = True

def main_menu_input(option_1, option_2):
    
    print(input("Enter option: "))
    if option_1 == need_assist:
       return need_assist_intake()
    elif option_2 == (offer_assist_intake):
        return offer_assist_intake()
    else:
        print("Please enter a valid option")
        return welcome_menu


def need_assist_intake():
    name = input("Name: ")
    location = input("Location: ")
    vehicle_make = input("Vehicle Make: ")
    vehicle_model = input("Vehicle Model: ")
    recovery_desc = input("Description of Recovery Needs: ")
    print("\n","Your post submission details:""\n","\n","Name:","\n", name,"\n","\n","Location:","\n",location,"\n","\n","Vehicle Make:","\n", vehicle_make,"\n","\n","Vehicle Model:","\n", vehicle_model,"\n","\n","Recovery Details:","\n",recovery_desc,"\n", "\n")
    response()

def response():
    input("Are these details correct? y/n: ")
    if response.lower() == "y" or response.lower() == "yes":
        print("Thank you! Your assistance request has been posted!")
    elif response.lower() == "n" or response.lower() == "no":
        return main_menu_input
        

def offer_assist_intake():
    name = input("Name: ")
    location = input("Location: ")
    vehicle_make = input("Vehicle Make: ")
    vehicle_model = input("Vehicle Model: ")
    recovery_gear = input("List of Recovery Gear:  ")
    print("Are these details correct? y/n")
    print("Your post submission details:""\n","\n","Name: ", name,"\n","Location: ",location,"\n","Vehicle Make: ", vehicle_make,"Vehicle Model: ","\n",vehicle_model,"Recovery Gear: ","\n",recovery_gear,"\n")
    print("Thank you! Your assistance offer has been posted! ")

welcome_menu()


#Test Code
