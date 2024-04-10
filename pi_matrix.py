import sys
import random
import re

def bounds():
    try:
        max_digit = int(input("Enter upper bound for testing. "))
        return max_digit
    except ValueError:
        print("Please enter a valid input.")
        bounds()


max_group = bounds()//5

def __init__():
    global pi

    pi_file = open('digits_of_pi.txt','r')
    pi = pi_file.read().replace("\n", "")
    pi_file.close()
    pi = re.findall('.....',pi)
    
    main()
 

def main():
    index = random.randint(1,max_group-1)
    target_group = pi[index]
    group_above = pi[index+1]
    group_below = pi[index-1]
    print(target_group)
    while True:
        answer_above = input("Group above: ")
        if answer_above == "quit":
            print("SHUTTING DOWN ...")
            sys.exit()
        elif len(answer_above) != 5:
            print("Not a valid input.")
            continue
        break
    if answer_above == group_above:
        print("Correct.")
    else:
        print(f"WRONG. The correct answer is: {group_above}")
    main()
    
__init__()