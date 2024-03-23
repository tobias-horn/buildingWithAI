countries = ['Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden']
populations = [5615000, 5439000, 324000, 5080000, 9609000]
male_fishers = [1822, 2575, 3400, 11291, 1731]
female_fishers = [69, 77, 400, 320, 26]

def guess(winner_gender):
    if winner_gender == 'female':
        fishers = female_fishers
    else:
        fishers = male_fishers

    total_fishers = sum(fishers)
    biggest = 0
    guess = None

    for i in range(len(countries)):
        if fishers[i] > biggest:
            biggest = fishers[i]
            guess = countries[i]
    
    probability = (biggest / total_fishers) * 100

    return (guess, probability)

def main():
    country, fraction = guess("male")
    print("if the winner is male, my guess is he's from %s; probability %.2f%%" % (country, fraction))
    country, fraction = guess("female")
    print("if the winner is female, my guess is she's from %s; probability %.2f%%" % (country, fraction))

main()
