import pandas as pd
import sys
import random

periodic_table = pd.read_csv("Periodic Table of Elements.csv")
periodic_table["AtomicMass"] = periodic_table["AtomicMass"].round()
modes = ["AtomicNumber","AtomicMass"]
mode_names = ["atomic number", "atomic mass"]

def main():
    x = random.randint(0,1)
    mode = modes[x]
    mode_name = mode_names[x]
    atomic_number = random.randint(1,50)
    element = periodic_table.loc[periodic_table["AtomicNumber"]==atomic_number,"Element"].values[0]
    prompt = periodic_table.loc[periodic_table["AtomicNumber"]==atomic_number,mode].values[0]
    response = input(f"What element has {mode_name} {prompt}?\n").strip().lower().capitalize()
    if response == "Quit":
        sys.exit()
    elif response == element:
        print("Correct!")
    else:
        print(f"Wrong! The element is {element}")
    main()

main()