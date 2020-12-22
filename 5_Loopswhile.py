##############
#while loop
##############


def run():
    LIM = 10000   #LIM constante with upper case

    cont = 0
    pow_2 = 2**cont
    while pow_2 < LIM:
        print(f"2 power {str(cont)} is equals to: {pow_2}")
        cont = cont + 1
        pow_2 = 2**cont

if __name__ == "__main__":
    run()