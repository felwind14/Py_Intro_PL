import random    #Module python

def run():

    aleat_num = random.randint(1, 100)
    chosen_num = int(input("Choose a number between 1:100: "))

    while chosen_num != aleat_num:
        if chosen_num < aleat_num:
            print("Choose a higher number!")
        else:
            print("Choose a lower number!")
        chosen_num = int(input("\nInsert the new number:")) #if we put this inside else --> infinite loop
    print("You are right!")


if __name__=="__main__":
    run()