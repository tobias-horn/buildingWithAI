import random

def main():

    favourite = ["bats", "dogs", "cats"]

    def randomWord(random_number):
        if random_number <= 0.8:
            return favourite[1]
        elif random_number <= 0.9:
            return favourite[0]
        else: 
            return favourite[2]

    print("I love " + randomWord(random.random()))




main()
