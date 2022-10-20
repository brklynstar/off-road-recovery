#Main Menu Functions
def border_line(): 
    print("-" * 40)

def welcome_msg():
    print()
    border_line()
    print("Welcome to ORRA!""\n""Off-Road Recovery App")
    border_line()

def enter_option():
    option= int(input("Enter Option:  "))
    while option != 0:
        if option == 1:
            need_assist_intake() # Handles user needing assistance input and submission review
            post_detail_confirm() #Handles if user inputs are correct and invalid answers
            print()
            break
        elif option == 2:
            offer_assist_intake()#Handles user offering assistance input and submission review
            post_detail_confirm()
            print() 
            break 
        elif option == 3:
            print("\nThank you for using the Off-Road Recovery app!")
            break
        else:
            print("Invalid entry, Try again.")
        print()
        menu()
        enter_option()

    
def menu():
    print("Select an Option:\n")
    print("[1] I Need Assistance")
    print("[2] I Want to Help Recover Someone")
    print("[3] Exit Program\n")
    enter_option()
    

def get_post_details(): 
    print()
    border_line()
    print("Enter Your Post Details")
    border_line()
    print()

def need_assist_intake():
    print()
    get_post_details()
    name = input("\n""Name: ""\n")
    location = input("\n""Location: ""\n")
    coordinates = input("\n""Coordinates: ""\n")
    vehicle_make = input("\n""Vehicle Make: ""\n")
    vehicle_model = input("\n""Vehicle Model: ""\n")
    vehicle_year =input("\n""Vehicle Year: ""\n")
    recovery_desc = input("\n""Description of Recovery Needs: ""\n")
    border_line()
    print("Your post submission details:")
    border_line()
    print( "\n",
    "Name:","\n", name,"\n",
    "\n","Location:","\n",location,"\n",
    "\n","Coordinates: ""\n", coordinates,"\n",
    "\n","Vehicle Make:","\n","\n", vehicle_make,"\n",
    "\n","Vehicle Model:","\n",vehicle_model,"\n",
    "\n","Vehicle Year: ","\n", vehicle_year, "\n",
     "\n","Recovery Details:", "\n",recovery_desc,"\n")
     
   
def offer_assist_intake():
    get_post_details()
    name = input("\n""Full Name:  ""\n")
    location = input("\n""Location:  ""\n")
    vehicle_make = input("\n""Vehicle Make:  ""\n")
    vehicle_model = input("\n""Vehicle Model: ""\n")
    vehicle_year = input("\n"" Vehicle Year: ""\n")
    recovery_gear = input("\n""List of Recovery Gear:  ""\n")
    border_line()
    print("Your submission details:")
    border_line()
    print( "\n",
    "Full Name:","\n", name,"\n",
    "\n","Location:","\n",location,"\n",
    "\n","Vehicle Make:","\n", vehicle_make,"\n",
    "\n","Vehicle Model:","\n",vehicle_model,"\n",
    "\n","Vehicle Year:", "\n", vehicle_year, "\n",
    "\n","List of Recovery Gear: ", "\n",recovery_gear,"\n")
    

def request_successful():
    print("Thank you! Your submission has posted!\n")
    print("Thank you for using the Off-Road Recovery app!")
   

yes = str("y,yes").lower().upper()
no = str("n, no").lower().upper()


def post_detail_confirm():
    border_line()
    user_answer = input("Are these details correct? y/n: ")
    border_line()
    print()
    if user_answer == "y":
        request_successful()
    elif  user_answer == "n":
            print("No, worries! Let's try again!")
            revisit_main_menu()
            int(input("Enter Option:  "))
    else: 
       print("Invalid Entry, Try Again")
       return post_detail_confirm

def main_menu():    
    welcome_msg()
    print()
    menu()

    
def revisit_main_menu():
    menu()
    option= int(input("Enter Option:  "))
    while option != 0:
        if option == 1:
            need_assist_intake() # Handles user needing assistance input and submission review
            post_detail_confirm() #Handles if user inputs are correct and invalid answers
            print()
            break
        elif option == 2:
            offer_assist_intake()#Handles user offering assistance input and submission review
            post_detail_confirm()
            print() 
            break 
        elif option == 3:
            print("\nThank you for using the Off-Road Recovery app!")
            break
        else:
            print("Invalid entry, Try again.")
        print()
        menu()
        enter_option()
        # option= int(input("Enter Option:  "))


#Main Menu Loop
#--------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------- 
#--------------------------------------------------------------------------------------------

main_menu()   

# option= int(input("Enter Option:  "))

