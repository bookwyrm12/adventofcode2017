###########################
#  Advent of Code 2017    #
#  Day 10: Knot Hash      #
#  April Jackson          #
###########################


# Get the data
with open('day10.in') as f:
    data = f.read()


# Helper method: Loop around circular list, from end to beginning
def wraparound(list_length, position):
    if position >= list_length:
        diff = position - list_length
        position = diff
    return position


# Part 1
def part1(knot_lengths):
    knot_lengths = [int(k) for k in knot_lengths.split(',')]

    # length = 5 # test list size
    length = 256 # actual list size
    string = list(range(length))

    skip = 0  # init skip size
    pointer = 0 # init pointer position

    # print('OG String: {}\n'.format(string))

    for k in knot_lengths:
        pointer = wraparound(length, pointer)

        # print('This length: {}'.format(k))
        # print('Pointer: {}'.format(pointer))
        # print('Skip: {}'.format(skip))

        substring = []
        for i in range(k):
            next = wraparound(length, pointer + i)
            substring.append(string[next])
        # print('Substring: {}'.format(substring))
        substring.reverse()

        for i in range(len(substring)):
            next = wraparound(length, pointer + i)
            string[next] = substring[i]
        # print('New String: {}\n'.format(string))

        pointer = pointer + k + skip
        pointer = wraparound(length, pointer)

        skip += 1

    # print('Final String: {}'.format(string))
    result = string[0] * string[1]
    print('Part 1: Final result: {}'.format(result))


# Part 2
def part2(knot_lengths):
    pass


# Do the stuff
part1(data)
part2(data)