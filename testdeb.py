# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
def conversor(currency_type, dollar_value):
    pesos = input("How many " + currency_type + " do you have?:  ")
    pesos = float(pesos)
 #   dollar_value = 3875  -deleted because is a parameter
    dollars = pesos / dollar_value
    dollars = round(dollars,2)
    dollars = str(dollars)
    print("You have $" + dollars + " dollars")
    print("\n")    #Print is a function built-in

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
elif option == 2:
    conversor("ARG", 65)
elif option == 3:
    conversor("MXN", 24)
else:
    print("Enter a correct option:")



# %%
