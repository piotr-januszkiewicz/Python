from random import randint

if __name__ == '__main__':
    counter = 1
    n = 0
    x = randint(1, 100)

    print("Welcome to the \"guess the number game\"")

    while int(n) != x:
        print("guess the number: ")
        n = input()
        if int(n) == x:
            print(f"Congratulations! the number is {x} and you guessed it after {counter} times!")
            break
        else:
            counter += 1
            if int(n) > x:
                print("Lower\n")
            else:
                print("Greater\n")
