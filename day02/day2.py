#####################################
#  Advent of Code 2017              #
#  Day 2: Corruption Checksum       #
#  April Jackson                    #
#####################################

# Get data from an unknown number of lines of input
def get_data():
    data = []
    while True:
        row = input()
        if row == "":
            break
        data.append(row)

    return data

# Part 1
def part1(ss):
    checksum = 0
    for row in ss:
        list = [int(i) for i in row.split()]
        big = max(list)
        small = min(list)
        diff = big - small
        checksum += diff

    print('Part 1: Checksum: {}'.format(checksum))

# Part 2
def part2(ss):
    checksum = 0
    for row in ss:
        list = [int(i) for i in row.split()]
        quotient = part2_compare(list)
        checksum += quotient

    print('Part 2: Checksum: {}'.format(checksum))

def part2_compare(list):
    for i in range(0, len(list)):
        # print('list[i]: {}'.format(list[i]))
        for j in range(i + 1, len(list)):
            # print('list[j]: {}'.format(list[j]))
            if list[i] % list[j] == 0:
                # print('list[i] / list[j]: {}'.format(list[i] / list[j]))
                return (int(list[i] / list[j]))
            if list[j] % list[i] == 0:
                # print('list[j] / list[i]: {}'.format(list[j] / list[i]))
                return (int(list[j] / list[i]))

# Do the stuff
data = get_data()
part1(data)
part2(data)