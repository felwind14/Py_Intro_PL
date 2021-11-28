######################
#Creating palindromes#
#####################

#3-Creating a funtion always above where it is called
def palindrome(word): 
    word = word.replace(' ', '')  #to remove spaces in order that the pc understands e.g Luz azul
    word = word.lower()            #to passs all letter into low
    inv_word = word[::-1]          #Inverting the word cap leter and lowcase are diff
    if word == inv_word:
        return True
    else:
        return False


#1- creating a main function which runs the program at the beggining
#to avoid just runing the program line by line commonly is used a
#function called def main() --> today we are going to use run
def run():
    word = input("Insert a word: ")
    word = word.strip()
    x = palindrome(word)
    if x == True:
        print("The word is a palindrome")
    else:
        print("The word is not a palindrome ")


#2- Entry point --always used---once py finds it starts running
#everything is below
if __name__ == '__main__':
    run()


##👨‍🏫Lesson
##################################################
#1.useful methods to work with cadenas characters
##################################################
#<var> = "str"  --> or cadena de caracteres
#<var>.capitalize()
#<var>.upper()
#<var>.strip() --> to eliminate garbage spaces at the beggining and the end
#<var>.lower() --->transform to minuscules
#<var>.replace() -->e.g <var>.replace("o","a")  --> replace 0 with a 
#<var>[#index] ---->to access to one part of the character
#Windowskey + . --> emojis
#len(<var>) ------->to know the lenghth of la cadena de caracteres

######
#2.Slicing
#######
#<var>[initial_value:end_value:steps]
#<var>[::-1]to invert
#<var>[#:] ---->from # till the end

##########
#Create a main function
###################

#Always we run python code line by line but it is good practice to tell the computer from where to start running the code
# def run():
#   pass
# if __name__ == "__main__":  --->entry point if python find this strats running here
#   run()




# # Other way 
# def es_palindromo(palabra):
#     palabra = palabra.replace(' ', '').lower()
#     if palabra[::] == palabra[::-1]:
#         return True
#     else:
#         return False


# def run():
#     palabra = input('Ingrese una palabra: ')
#     if es_palindromo(palabra):
#         print('Es palindromo')
#     else:
#         print('No es palindromo')


# if __name__ == "__main__":
#     run()