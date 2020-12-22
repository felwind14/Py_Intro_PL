import random

def generate_password():
    cap = ["A", "B", "C", "D","E","F"]
    low = ["a","b","c","d","f","g"]
    symb = ["!", "#", "$", "+"]
    num = ["1","2","3","4","5"]
    characters = cap + low + symb + num

    password = []   #generating an empty list to store the new password

    for i in range (15+1):
        character_random = random.choice(characters)
        password.append(character_random)

    password =''.join(password)       #transforming a list on a string
    return password    


def run():
    password = generate_password()
    print('Your new password is: ' + password)


if __name__ =='__main__':
    run()
