#####################################
#  Advent of Code 2017              #
#  Day 7: Recursive Circus          #
#  April Jackson                    #
#####################################

# Get the data
with open('day7.in') as f:
    data = f.read()


# Part 1
def part1(info):
    info = [[splitline for splitline in line.split()] for line in info.splitlines()] # put input into array
    info_p = [] # init array to place cleaner program info into

    for p in info: # remove weights, arrows, and commas from program info
        tmp = [p.pop(0)]
        p.pop(0)
        while len(p) > 0:
            p_tmp = p.pop(0)
            if '(' not in p_tmp and '->' != p_tmp:
                tmp.append(p_tmp.strip(','))
        info_p.append(tmp)

    top_blocks = [x for x in info_p if len(x) == 1] # programs without any programs above them
    bottom_blocks = [x for x in info_p if x not in top_blocks] # programs holding other programs

    # failed attempts at using list comprehension to find the bottom program...
    # bottom = [[elem for sublist in bottom_blocks] for elem in sublist]
    # bottom = [x for x in bottom_blocks if x[0] not in [[elem for sublist in bottom_blocks] for elem in bottom_blocks]]
    
    bottom = None
    for p in bottom_blocks:
        possible = p[0]
        indeces = []
        for i in bottom_blocks:
            if possible in i:
                indeces.append(i.index(possible))
        if len(indeces) == 1:
            bottom = possible # the bottom program is the one with no other programs holding it

    print('Part 1: Bottom program: {}'.format(bottom))


# Part 2
def part2(info):
    pass


# Do the stuff
part1(data)
part2(data)