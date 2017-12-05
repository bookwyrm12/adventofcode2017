#####################################
#  Advent of Code 2017              #
#  Day 3: Spiral Memory             #
#  April Jackson                    #
#####################################

# Imports
import math
import numpy as np

# Global variables
coords = [(0,1), (-1,1), (-1,0), (-1,-1), (0,-1), (1,-1), (1,0), (1,1)] # idea borrowed from vesche (https://github.com/vesche/adventofcode-2017/blob/master/day03.py)

# Part 1
def part1(data):
    square_length = int(math.ceil(math.sqrt(data)) // 2 * 2 + 1) # round up to nearest odd integer
    # print('square len: {}'.format(square_length))
    # steps = square_length // 2 # steps from center of square to outer square
    # print('half square: {}'.format(steps))
    # bottom_right = square_length**2
    bottom_right_inner = (square_length - 2)**2
    # print('bot right: {}'.format(bottom_right))
    # print('bot right inner: {}'.format(bottom_right_inner))
    steps = (data - bottom_right_inner) % (square_length - 1)
    # print('position: {}'.format(position))

    print('Part 1: Steps: {}'.format(steps))

# Part 2
def part2(data):
    value = 0
    square_length = 3
    spiral = np.zeros((square_length, square_length)) # init 3x3 square of zeros
    spiral[1][1] = 1 # init the center of the spiral to 1

    # while value < data: # for each square (3, 5, 7,...) until we hit the end
    # for dist_from_center in range(1, data):
    while True:
        if value > data:
            break
        for i in range(4):
            for j in range(square_length - 1):
                print('i,j: {},{}'.format(i, j))
                for offset in coords: # add up all adjacent items
                    orow, ocol = offset
                # desired order:
                # 1,2
                # 0,2
                # 0,1
                # 0,0
                # 1,0
                # 2,0
                # 2,1
                # 2,2

        print(spiral)
        spiral = np.pad(spiral, [(1, 1), (1, 1)], mode='constant')
        print(spiral)
        square_length += 2
        break

    print('Part 2: Value: {}'.format(value))


# Do the stuff
data = int(input())
part1(data)
part2(data)