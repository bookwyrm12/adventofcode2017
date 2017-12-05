#####################################
#  Advent of Code 2017              #
#  Day 5: A Maze of Twisty          #
#         Trampolines, All Alike    #
#  April Jackson                    #
#####################################

# Get the data
with open('day5.in') as f:
    data = f.read()


# Part 1
def part1(instructions):
    instructions = [int(x) for x in instructions.splitlines()]
    steps = 0
    pointer = 0

    while True:
        after_jump = pointer + instructions[pointer]
        instructions[pointer] += 1
        pointer = after_jump
        steps += 1

        if pointer < 0 or pointer >= len(instructions):
            break

    print('Part 1: Steps to reach the exit: {}'.format(steps))


# Part 2
def part2(instructions):
    instructions = [int(x) for x in instructions.splitlines()]
    steps = 0
    pointer = 0

    while True:
        after_jump = pointer + instructions[pointer]
        if instructions[pointer] >= 3:
            instructions[pointer] -= 1
        else:
            instructions[pointer] += 1
        pointer = after_jump
        steps += 1

        if pointer < 0 or pointer >= len(instructions):
            break

    print('Part 2: Steps to reach the exit: {}'.format(steps))


# Do the stuff
part1(data)
part2(data)