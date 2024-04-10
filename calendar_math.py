from datetime import date
from faker import Faker
import sys

fake = Faker()

month_codes = [6,1,2,5,0,3,5,1,4,6,2,4]
weekDays = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")

queries = 0
successes = 0

def year_code(year):
    if year >= 2000:
        year -= 2000
        code = year + year//4
        code = code%7
        return code
    elif year <= 1999:
        year -= 1900
        code = year + year//4
        code = code%7
        return code+1

def quit():
    global queries
    queries -= 1
    print(f"You have successfully identified {successes} out of {queries} dates.")
    print(f"Success rate: {round(successes/queries,2)*100}%")
    sys.exit()

def main():
    global queries
    global successes

    queries += 1
    first_try = True

    new_date = fake.date_object()
    answer = weekDays[new_date.weekday()]
    print(new_date)
    while True:
        cmd = input().strip().lower().capitalize()
        if cmd == "Quit":
            quit()
        elif cmd == "Code":
            print(year_code(new_date.year))
            first_try = False
            continue
        elif cmd == answer:
            print("Correct")
            if first_try == True:
                successes += 1
        else:
            print("Try again.")
            first_try = False
            continue
        break
    main()

main()