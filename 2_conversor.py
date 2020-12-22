# Currency conversor
#######################################################
#2- Making the conversor in modules improving 1 below
########################################################


# #Take this example as a hint
# def sum(a, b):
#     print("Two numbers are added")
#     result = a + b   #If I don't add return python will not return directly so use return
#     return result  #the variable result will be returned

# addition = sum(1, 2)   #addition = result
# print(addition)

# print("\n")

##function
def conversor(currency_type, dollar_value):
    pesos = input("How many " + currency_type + " do you have?:  ")
    pesos = float(pesos)
 #   dollar_value = 3875  -deleted because is a parameter
    dollars = pesos / dollar_value
    dollars = round(dollars,2)
    dollars = str(dollars)
    print(f"You have ${dollars} in total")
    print("\n")    #Print is a function built-in

i = 1
while i == 1:
    #Creating a menu for user
    menu = """
    Welcome to the currency exchange Pesos to USD 😊🐕‍🦺  

    1- Colombian Pesos
    2- Argentinian Pesos 
    3- Mexican pesos

    Chose one option: """

    option = int(input(menu))


    if option == 1:
        conversor("COP", 3875)
        i = 0
    elif option == 2:
        conversor("ARG", 65)
        i = 0
    elif option == 3:
        conversor("MXN", 24)
    else:
        print("Enter a correct option. ")
        print("---------")
        i = 1

##############################################
#Special build-in functions --> x = variable
##############################################


# x.capitilize() --> capitilize the first word
# x.lower()  ------> small letters
# x.strip() ------> remove all remaining spaces before and after a word
# len (x)
# x[0-n]

###Slicing nombre = "Francisco"
#nombre[1::3] from position 1 till the end in steps of 3
#nombre[::-1] ocsicnarF


#################
#1 - Initial code
################


# Using menu

# menu = """
# Welcome to the currency exchange 😊🐕‍🦺

# 1- Colombian Pesos
# 2- Argentinian Pesos 
# 3- Mexican pesos

# Chose one option: """

# option = int(input(menu))
# #With int above we transform directly the input string to integer
# if option == 1:
#     #Code block
#     pesos = input("How many COP do you have?:  ")
#     pesos = float(pesos)
#     dollar_value = 3875
#     dollars = pesos / dollar_value
#     dollars = round(dollars,2)
#     dollars = str(dollars)
#     print("You have $" + dollars + " dollars")
#     print("\n")
# elif option == 2:
#     #Code block
#     pesos = input("How many ARG do you have?:  ")
#     pesos = float(pesos)
#     dollar_value = 65
#     dollars = pesos / dollar_value
#     dollars = round(dollars,2)
#     dollars = str(dollars)
#     print("You have $" + dollars + " dollars")
#     print("\n")
# elif option == 3:
#     #Code block
#     pesos = input("How many MXN do you have?:  ")
#     pesos = float(pesos)
#     dollar_value = 24
#     dollars = pesos / dollar_value
#     dollars = round(dollars,2)
#     dollars = str(dollars)
#     print("You have $" + dollars + " dollars")
#     print("\n")
# else:
#     print("Enter a correct option:")









