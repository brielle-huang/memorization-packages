import random
import sys

def main():
    num = random.randint(11,99)
    answer = num**2
    print(num)
    while True:
        try:
            response = int(input())
        except ValueError:
            print("Invalid input")
            continue
        if response == -1:
            sys.exit()
        elif response == answer:
            print("Correct.")
            break
        else:
            print("Try again.")
    main()

main()