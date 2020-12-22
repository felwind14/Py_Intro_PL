def is_prime(num):
    if num == 0 or num == 1:
        return False
    else:
        cont = 0

    for i in range (1, num + 1):
        if i == 1 or  i == num:
            continue
        if num % i == 0:
            cont += 1
    if cont == 0:
        return True
    else:
        return False



def run():
    num = int(input("Write a number:"))

    if is_prime(num): #if this is true we can obviate == True
        print("The number is prime.")
    else:
        print("The number is not prime.")

if __name__=="__main__":
    run()