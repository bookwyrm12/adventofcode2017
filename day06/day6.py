#####################################
#  Advent of Code 2017              #
#  Day 6: Memory Reallocation       #
#  April Jackson                    #
#####################################

# Get the data
with open('day6.in') as f:
    data = f.read()


# Part 1
def part1(bank):
    bank = [int(x) for x in bank.split()] # put input into array
    steps = 0 # init step count
    history = [] # init state history array

    while True:
        max_block = max(bank) # highest number of blocks in any one bank
        pointer = bank.index(max_block) # index of the bank with the most blocks
        bank[pointer] = 0 # reset that bank before redistribution

        for i in range(max_block): # redistribute the blocks
            pointer += 1 # increment pointer to the next bank
            if pointer == len(bank): # loop around from end of array to beginning
                pointer = 0
            bank[pointer] += 1 # add block to the bank

        steps += 1 # increment step count

        if bank in history: # if the current state has been seen before, end loop
            break

        history.append(bank[:]) # add current state to history

    print('Part 1: Redistribution cycles: {}'.format(steps))


# Part 2
def part2(bank):
    bank = [int(x) for x in bank.split()] # put input into array
    history = [] # init state history array

    while True:
        max_block = max(bank) # highest number of blocks in any one bank
        pointer = bank.index(max_block) # index of the bank with the most blocks
        bank[pointer] = 0 # reset that bank before redistribution

        for i in range(max_block): # redistribute the blocks
            pointer += 1 # increment pointer to the next bank
            if pointer == len(bank): # loop around from end of array to beginning
                pointer = 0
            bank[pointer] += 1 # add block to the bank

        if bank in history: # if the current state has been seen before, end loop
            break

        history.append(bank[:]) # add current state to history

    history.append(bank[:]) # add the last (duplicate) state to history

    duplicates = []
    for i, j in enumerate(history): # get the indeces of the duplicate states
        if j == bank:
            duplicates.append(i)

    steps = duplicates[1] - duplicates[0] # number of cycles between the duplicate states

    print('Part 2: Cycles in infinite loop: {}'.format(steps))


# Do the stuff
part1(data)
part2(data)