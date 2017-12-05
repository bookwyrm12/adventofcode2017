#####################################
#  Advent of Code 2017              #
#  Day 4: High-Entropy Passphrases  #
#  April Jackson                    #
#####################################

# Get the data
with open('day4.in') as f:
    data = f.read()


# Part 1
def part1(passphrases):
    valid = 0
    passphrases = passphrases.splitlines()
    # print(passphrases)
    for phrase in passphrases:
        words = phrase.split()
        # print(words)
        num_words = len(words)
        unique_words = list(set(words))
        num_unique_words = len(unique_words)
        if num_words == num_unique_words:
            valid += 1

    print('Part 1: Valid passphrases: {}'.format(valid))


# Part 2
def part2(passphrases):
    valid = 0
    passphrases = passphrases.splitlines()

    for phrase in passphrases:
        words = [''.join(sorted(w)) for w in phrase.split()]
        num_words = len(words)
        unique_words = list(set(words))
        num_unique_words = len(unique_words)
        if num_words == num_unique_words:
            valid += 1

    print('Part 2: Valid passphrases: {}'.format(valid))


# Do the stuff
part1(data)
part2(data)