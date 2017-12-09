#######################################
#  Advent of Code 2017                #
#  Day 8: I Heard You Like Registers  #
#  April Jackson                      #
#######################################

# Imports
import pprint

# Get the data
with open('day8.in') as f:
    data = f.read()


# Part 1
def part1(instructions):
    registers = {}

    for instruct in instructions.splitlines():
        instruct_split = [item for item in instruct.split()]
        instruct_split[1] = "+" if instruct_split[1] == "inc" else "-"
        if_check = 'if registers[instruct_split[4]] ' + ' '.join(instruct_split[5:])
        action = 'registers[instruct_split[0]] = registers[instruct_split[0]] ' + ' '.join(instruct_split[1:3])
        exec_string = if_check + ': ' + action
        # print(exec_string)
        if instruct_split[0] not in registers:
            registers[instruct_split[0]] = 0
        if instruct_split[4] not in registers:
            registers[instruct_split[4]] = 0
        exec(exec_string)

    # pprint.pprint(registers)
    largest_val = max(registers.values())

    print('Part 1: Largest value in any register: {}'.format(largest_val))


# Part 2
def part2(instructions):
    pass


# Do the stuff
part1(data)
part2(data)