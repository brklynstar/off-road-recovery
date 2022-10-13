# def gear_choices():
#     f = open('gear_list.txt', 'r')
#     gear_list = f.readlines()
#     f.close()
#     gear_list = gear_list[0].split(' ')
#     return gear_list

#-----------------------------------------------------------------------
#Definig Functions

need_assistance = int(1)
offer_assistance =int(2)


def menu(option):
    if option == 1:
        return need_assistance
    elif option == 2:
        return offer_assistance

def need_valid_option(option):
    if option <2:
        print("Invalid option, try again")
    elif option >1:
        print("Invalid option, try again")
    else:
        return


def need_assistance():
    if need_assistance == 1:
        print(name = input("Name: "))
        print(location = input("Location: "))
        print(vehicle_make = input("Vehicle Make: "))
        print(vehicle_model = input("Vehicle Model: "))
        print(recovery_desc = input("Description of Recovery Needs: "))  
    else: 
        return need_valid_option

def offer_assistance():
    if offer_assistance == 2:
        print(name = input("Name: "))
        print(location = input("Location: "))
        print(vehicle_make = input("Vehicle Make: "))
        print(vehicle_model = input("Vehicle Model: "))
        print(recovery_desc = input("Description of Recovery Needs: "))
    else: 
        return need_valid_option



        







        


# def assist_or_be_assisted():
#     if need_assistance == 1:
        
#     else:
#         print()



#----------------------------------------------------
#Calling Functions
print("Welcome to the Off-Road Recovery App!" "\n")
print("Choose an option: " "\n" "1. I need recovery assistance" "\n"  "2. I want to assist in recovering someone" "\n")


