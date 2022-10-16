#Define Functions
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
    print("[2] I Want to Help Recover")
    print("[3] Exit Program\n")

def get_post_details(): 
    border_line()
    print("Enter Your Post Details")
    border_line()
    print()

def post_detail_confirm():
    input("Are these details correct? y/n: ")
    if input == yes:
        return request_successful()
    elif input == no:
        return get_post_details()
    else: 
        print("Invalid Entry, Try Again")

def need_assist_intake():
    get_post_details()
    name = input("Name: ")
    location = input("Location: ")
    vehicle_make = input("Vehicle Make: ")
    vehicle_model = input("Vehicle Model: ")
    recovery_desc = input("Description of Recovery Needs: ")
    print("\n",
    "Your post submission details:","\n",
    "\n","Name:","\n", name,"\n","\n",
    "Location:","\n",location,"\n",
    "\n","Vehicle Make:","\n",
     vehicle_make,"\n",
     "\n","Vehicle Model:",
     "\n",vehicle_model,"\n",
     "\n","Recovery Details:",
     "\n",recovery_desc,"\n", "\n"
     )
    return post_detail_confirm()
    



def offer_assist_intake():
    get_post_details()
    name = input("Name: ")
    location = input("Location: ")
    vehicle_make = input("Vehicle Make: ")
    vehicle_model = input("Vehicle Model: ")
    recovery_gear = input("List of Recovery Gear:  ")
    print("Your post submission details:""\n","\n","Name: ",name,"\n","Location: ",location,"\n","Vehicle Make: ",vehicle_make,"Vehicle Model: ","\n",vehicle_model,"Recovery Gear: ","\n",recovery_gear,"\n")

def request_successful():
    print("Thank you! Your assistance request has been posted!")
    return request_successful()

yes = ("y,yes, Y, YES")
no = ("n, no, N, No")
main_menu_input=()



# def reenter_post_details(need_assist_intake, offer_assist_intake):
#     if input =="n":
#     reenter_post_details ==


  
welcome_msg()
print()
menu()
option= int(input("Enter Option:  "))





while option != 0:
    if option == 1:
        need_assist_intake()
        post_detail_confirm()
       
        pass
            
#     elif option == 2:
#         offer_assist_intake()
#         post_detail_confirm
#             # reenter_post_details()
#     else:
#         print("Invalid Entry, Try Again")

# menu()
    
# print("We're searching for a local off-road member near you...")
        



