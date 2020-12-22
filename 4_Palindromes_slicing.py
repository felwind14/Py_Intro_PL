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
    word = input("Write a word: ")
    is_palindrome = palindrome(word)
    if is_palindrome == True:
        print("It is a palindrome")
    else:
        print("It is not a palindrome")


#2- Entry point --always used---once py finds it starts running
#everything is below
if __name__ == '__main__':
    run()




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