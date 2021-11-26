##########################
##Creation of a function##
##########################

#1- Function:

# def printing_message():
#     print("Special message:")
#     print("I'm learning to use functions")

# # #Instead of writing 3 times the "print" statement 
# # #We call the function three times
# printing_message()
# printing_message()
# printing_message()

# print("\n")

#2-Parameters

#Here we are repeating the same code block but how to create a function
#to change the option  --> use parameter

# option = int(input("Choose one function (1, 2, 3):")  
# if option == 1:
#     print('Hola')
#     print('How are you?')
#     print('You chose the option 1')
#     print('Bye')
# elif option == 2:
#     print('Hola')
#     print('How are you?')
#     print('You chose the option 2')
#     print('Bye')
# elif option == 3:
#     print('Hola')
#     print('How are you?')
#     print('You chose the option 3')
#     print('Bye')


######################    
##Using parameters####
######################


# def conversation(message):
#     print('Hola')
#     print('How are you?')
#     print(message)
#     print('Bye')


# option = int(input("Choose one function (1,2,3): "))
# if option == 1:
#     conversation('You chose the option 1')
# elif option == 2:
#     conversation('You chose the option 2')
# elif option == 3:
#     conversation('You chose the option 3')
# else:
#     print("Write a correct option!!")

# print("\n")
 
#Replacing The above code with two functions####
#######################################
# x = 0

# def conversation_choice(choice):
#     print('Hola')
#     print('How are you?')
#     print('You chose the option:', choice)
#     print('Bye')

# option = int(input("Choose one function (1,2,3): "))
# if option == 1:
#     x = option
#     choice(x)
# elif option == 2:
#     x = option
#     choice(x)
# elif option == 3:
#     x = option
#     choice(x)
# else:
#     print("Write a correct option!!")    

##More advanced by FF

# def conversacion_choice(choice):
#     print("Hola, Como estás?")
#     print("Seleccionaste la opcion:", choice)
#     print("Gracias por participar ahora cerraremos el programa.")

# loop=1
# choice = 0

# choice = int(input("Please type a choice 1 to 3 select 4 to quit. "))
# while loop == 1:
#     if choice == 1:
#         conversacion_choice(choice)
#         loop = 0
#     elif choice == 2:
#         conversacion_choice(choice)
#         loop = 0
#     elif choice == 3:
#         conversacion_choice(choice)
#         loop = 0
#     elif choice == 4:
#         print("Sad you don't want to play.")
#         loop = 0
#     else:
#         print("Please try again!!")
    
 ##A bit more advanced

##Creating the Menu

def menu():
    print("\nWelcome to our first programme\nOptions available:\n")
    print("1.Write Hola")
    print("2.Write Chao")
    print("3.Write Love")
    print("4.To exit")
    
    return eval(input("\nChoose your option: "))

def hol(a):
    a = "Hola"
    print(f"Writing...{a}!")

def ch(b):
    b = "Chao"
    print(f"Writing...{b}!")

def lo(c):
    c= "Love"
    print(f"Writing...{c}")

loop = 1
choice = 0

while loop == 1:
    choice = menu()
    if choice == 1:
        hol(choice)
        print("####")
    elif choice == 2:
        ch(choice)
        print("####")
    elif choice == 3:
        lo(choice)
        print("####")
    elif choice == 4:
        loop = 0
        print("####")
    else:
        print("\nPlease!!!!!...Insert a valid option")
        menu()

print("Thank you for testing")
    
