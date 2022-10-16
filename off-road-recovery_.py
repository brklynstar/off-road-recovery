#Define Functions




    
def border_line(): 
    print("-" * 40)
    


# user_input_1 = ("1")
# user_input_2 = ("2") 

# need_assist_opt = user_input_1
# offer_assist_opt = user_input_2
input_num = 1
user_input_y = ("y,yes,Y, YES")
user_input_n = ("n,no, N, NO")
main_menu_user_input = 0
raw_input = 0

def welcome_menu():
    print("Welcome to the Off-Road_Recovery App!")
    border_line()
   

# def main_menu_input(main_menu_user_input):
#     main_menu_user_input = int(input("Enter option: "))
#     if main_menu_user_input == input_num:
#        True
#     elif main_menu_user_input == input_num + 1:
#         False
#     else:
#         print("Please enter a valid option") #<- Not working, entering any number will continue to work
        


def request_success():
    print("\n""Thank you! Your assistance request has been posted!""\n")
   

def response():
    input("Are these details correct? y/n: ")
    if user_input_y == True:
       return request_success() 
    elif user_input_n == True: #<- Returns request
        return welcome_menu()

def need_assist_intake():
    name = input("Name: ")
    location = input("Location: ")
    vehicle_make = input("Vehicle Make: ")
    vehicle_model = input("Vehicle Model: ")
    recovery_desc = input("Description of Recovery Needs: ")
    print("\n","Your post submission details:""\n","\n","Name:","\n", name,"\n","\n","Location:","\n",location,"\n","\n","Vehicle Make:","\n", vehicle_make,"\n","\n","Vehicle Model:","\n", vehicle_model,"\n","\n","Recovery Need Details:","\n",recovery_desc,"\n", "\n")
    

def offer_assist_intake():
    name = input("Name: ")
    location = input("Location: ")
    vehicle_make = input("Vehicle Make: ")
    vehicle_model = input("Vehicle Model: ")
    recovery_gear = input("List of Recovery Gear:  ")
    print("Your post submission details:""\n","\n","Name: ",name,"\n","Location: ",location,"\n","Vehicle Make: ",vehicle_make,"Vehicle Model: ","\n",vehicle_model,"Recovery Gear: ","\n",recovery_gear,"\n")
    

#--------------------------------------------------------------------------------------------------------------------------------------------   
#--------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------
#Calling Functions
#welcome_menu() # currently a no response will return you to the main menu, but I would like the user to be able to append their list.
#have one user_input with 2 paramaeters y and n

#Runs Menu


user_inputs = ()
user_input = ()

welcome_menu()
for user_input in user_inputs:
    print("""
    1. I need assistance
    2. I want to help recover
    """)
    users_input= input("Enter option: ")
    
if user_input== input_num: 
    need_assist_intake()
elif users_input== input_num +1:
    offer_assist_intake
else:
    print("\n Invalid Choice, Try Again")









# while welcome_menu(): #"Choose an option: " "\n""1. I need recovery assistance" "\n""2. I want to assist in recovery""\n")
#     main_menu_input() #  #user_input_1 = "1"
#     print(need_assist_intake)
#     response() #"Are these details correct? y/n: ")
#     if response() == user_input_y:
#         request_success()
#     else:
#             welcome_menu()
#     if main_menu_input() == False:
#         offer_assist_intake
#         response()
#         if response() == user_input_y:
#             request_success()
#         welcome_menu()

#  response() == user_input_y:
#             request_success()


#     if user_input_2 == user_input_2: int("2") #user_input_2 = "2"
#     offer_assist_intake() # handles user intake and submission detail output
#     response()
#     request_success() #("\n""Thank you! Your assistance request has been posted!""\n")
            
       
#     elif offer_assist_opt == :
#         offer_assist_intake()
#         response()
#         if response == user_input_n:
#             welcome_menu #Want to make this to append the users input, not go back to main menu
#         if response == user_input_y:
#             request_success()
#     continue
            
        



#--------------------------------------------------------------------------------------------------------------------------------------------   
#--------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------


#Test Code
