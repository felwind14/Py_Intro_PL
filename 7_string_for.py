def run():
    # name = input("Write your name: ")
    # for letter in name:
    #     print(letter)
    list =[]
    i = 0
    sentence = input("Write a sentence: ")
    for caracter in sentence:
        print(caracter.upper())
        list.append(caracter.upper())

    list="".join(list) #join list element as a string
    print(list)
    print(type(list))  
     


if __name__ == '__main__':
    run()
