################################
#  Advent of Code 2017         #
#  Day 15: Dueling Generators  #
#  April Jackson               #
################################


# Get the data
with open('day15.in') as f:
    data = f.read()


# Helper: Parse the data for each generator's initial value
def get_gen_values(data):
    generators = []
    for line in data.splitlines():
        line = [word for word in line.split()]
        generators.append(line[-1])
    return int(generators[0]), int(generators[1])


# Helper: Get next value for Generator A
def get_next_a(gen_a):
    mult_a = 16807
    div_by = 2147483647

    gen_a *= mult_a
    gen_a %= div_by

    return gen_a


# Helper: Get next value for Generator B
def get_next_b(gen_b):
    mult_b = 48271
    div_by = 2147483647

    gen_b *= mult_b
    gen_b %= div_by

    return gen_b


# Part 1
def part1(gen_a, gen_b):
    print('gen a: {}; gen b: {}'.format(gen_a, gen_b))

    total_rounds = 40000000

    judge = 0

    for round in range(total_rounds):
        gen_a = get_next_a(gen_a)
        gen_b = get_next_b(gen_b)
        bin_a = "{0:b}".format(gen_a)
        bin_b = "{0:b}".format(gen_b)
        if bin_a[-16:] == bin_b[-16:]:
            judge += 1

    print('Part 1: Judge\'s final count: {}'.format(judge))


# Part 2
def part2(gen_a, gen_b):
    pass


# Do the stuff
gen_a, gen_b = get_gen_values(data)
part1(gen_a, gen_b)
part2(gen_a, gen_b)