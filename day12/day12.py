#############################
#  Advent of Code 2017      #
#  Day 12: Digital Plumber  #
#  April Jackson            #
#############################


# Get the data
with open('day12.in') as f:
    data = f.read()


# Helper method: Loop around circular list, from end to beginning
def data_to_dict(data):
    data_dict = {}
    for line in data.splitlines():
        line = line.split()
        id, programs = int(line[0]), line[2:]
        data_dict[id] = programs
    return data_dict


# Part 1
def part1(village):
    village = data_to_dict(village)
    seen = []

    num_programs = part1_recurse(village, 0, seen)
    print('Part 1: Number of programs: {}'.format(num_programs))


def part1_recurse(village, id, seen):
    # print('ID: {}; seen: {}; num_programs: {}'.format(id, seen, num_programs))
    if id in seen:
        return 0

    seen.append(id)

    for prog in village[id]:
        tmp = part1_recurse(village, int(prog), seen)

    return len(seen)


# Part 2
def part2(village):
    village = data_to_dict(village)
    seen = []
    num_groups = 0

    for key in village:
        group = part2_recurse(village, key, [])
        if group[0] not in seen:
            seen.extend(group)
            num_groups += 1

    print('Part 2: Number of groups: {}'.format(num_groups))


def part2_recurse(village, id, seen):
    # print('ID: {}; seen: {}; num_programs: {}'.format(id, seen, num_programs))
    if id in seen:
        return 0

    seen.append(id)

    for prog in village[id]:
        tmp = part2_recurse(village, int(prog), seen)

    return seen


# Do the stuff
part1(data)
part2(data)