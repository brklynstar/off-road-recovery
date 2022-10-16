#Main Menu Functions
def border_line(): 
    print("-" * 40)

def welcome_msg():
    print()
    border_line()
    print("Welcome to the Off-Road_Recovery App!")
    border_line()

def menu():
    print("Choose an Option:\n")
    print("[1] I Need Assistance")
    print("[2] I Want to Help Recover Someone")
    print("[3] Exit Program\n")

def get_post_details(): 
    print()
    border_line()
    print("Enter Your Post Details")
    border_line()
    print()


#Functions that get user input
def user_input(prompt):
    user_input = input = input(prompt).lower().upper()
    return user_input

def need_assist_intake():
    print()
    get_post_details()
    name = input("Name: ""\n")
    location = input("Location: ""\n")
    vehicle_make = input("Vehicle Make: ""\n")
    vehicle_model = input("Vehicle Model: ""\n")
    recovery_desc = input("Description of Recovery Needs: ""\n")
    border_line()
    print("Your post submission details:")
    border_line()
    print( "\n",
    "Name:","\n", name,"\n",
    "\n","Location:","\n",location,"\n",
    "\n","Vehicle Make:","\n","\n", vehicle_make,"\n",
     "\n","Vehicle Model:","\n",vehicle_model,"\n",
     "\n","Recovery Details:", "\n",recovery_desc,"\n","\n")
   
def offer_assist_intake():
    get_post_details()
    name = input("Name:  " "\n")
    location = input("Location:  ""\n")
    vehicle_make = input("Vehicle Make:  ""\n")
    vehicle_model = input("Vehicle Model: ""\n")
    recovery_gear = input("List of Recovery Gear:  ""\n")
    border_line()
    print("Your post submission details:")
    border_line()
    print( "\n",
    "Name:","\n", name,"\n",
    "\n","Location:","\n",location,"\n",
    "\n","Vehicle Make:","\n", vehicle_make,"\n",
     "\n","Vehicle Model:","\n",vehicle_model,"\n",
     "\n","List of Recovery Gear:", "\n",recovery_gear,"\n","\n")

def request_successful():
    print("Thank you! Your submission has posted!\n")
    print("We're searching for available recovery assistance near you... \nHang tight...")
  
#Functions to append answers
def update_input():
    

    

yes = ("y,yes, Y, YES")
no = ("n, no, N, No")
def post_detail_confirm():
    border_line()
    input("Are these details correct? y/n: ")
    print()
    if no == no:
     return 
    if yes == yes:
        return request_successful()
    else: 
        print("Invalid Entry, Try Again")

#Main Menu 
#--------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------- 
#--------------------------------------------------------------------------------------------


welcome_msg()
print()
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
    option= int(input("Enter Option:  "))


        



