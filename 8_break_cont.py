

def run():

#############    
##Continue#
#############
#     for cont in range(100):
#         if cont % 2 != 0:
#            continue    ##Here if conditions is true the following continue does not execute
#         print(cont)

#########
#break##
#########

    # for i in range(100):
    #     print(i)  
    #     if i == 50:
    #         break


    # text = input("Write a text: ")
    # for letter in text:
    #     print(letter, end ="")
    #     if letter == "o":
    #         break      

###################################
##break and continue with while
####################################
    num = int(input("Write a number you are interested to know the" \
                    " multiplication from 0-10 but for an odd numbers: "))
    i = 0
    pr = 0
    while i <= 10:
        pr = num * i
        i += 1 
        if num % 2 == 0:
            print("Write an odd number")
            break
        print(f" {num} times {i-1} equals: {pr}")


if __name__ == '__main__':
    run()