#!/usr/bin/python3
"""RZFeeser | Alta3 Research
   Printing dictionary data stored as lists to the screen"""


def main():
    """On this farm there was a..."""

    #this is the data we want to loop
    #is is a list contain 3 dictionaries
    farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

    for farm in farms:
        #print(farm)  #good first step after devloping the loop
        print(farm.get("name", "Unknown Farm"), end=":\n")

        for argi in farm.get("agriculture"):
            print(" -", argi)

if __name__ == "__main__":
    main()
