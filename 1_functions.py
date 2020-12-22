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
x = 0

def conversation_choice(choice):
    print('Hola')
    print('How are you?')
    print('You chose the option:', choice)
    print('Bye')

option = int(input("Choose one function (1,2,3): "))
if option == 1:
    x = option
    choice(x)
elif option == 2:
    x = option
    choice(x)
elif option == 3:
    x = option
    choice(x)
else:
    print("Write a correct option!!")    
