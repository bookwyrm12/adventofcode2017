###################################
#  Advent of Code 2017            #
#  Day 16: Permutation Promenade  #
#  April Jackson                  #
###################################


# Get the data
with open('day16.in') as f:
    data = f.read()


# Helper: Initialize programs
def get_intial_program_sequence():
    sequence = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']
    # sequence = ['a', 'b', 'c', 'd', 'e']
    return sequence


# Part 1
def part1(dance_moves):
    dance_moves = [move for move in dance_moves.split(',')]
    print(dance_moves)

    programs = get_intial_program_sequence()
    total_moves = len(dance_moves)

    for move in dance_moves:
        if move[0] == 's': # Spin
            num = int(move[1:])
            end = programs[-num:]
            the_rest = programs[:-num]
            programs = end + the_rest

        elif move[0] == 'x': # Exchange
            positions = move[1:].split('/')
            pos_a = int(positions[0])
            pos_b = int(positions[1])
            a = programs[pos_a]
            b = programs[pos_b]
            programs[pos_a] = b
            programs[pos_b] = a

        elif move[0] == 'p': # Partner
            progs = move[1:].split('/')
            a = progs[0]
            b = progs[1]
            pos_a = programs.index(a)
            pos_b = programs.index(b)
            programs[pos_a] = b
            programs[pos_b] = a

    final_order = ''.join(programs)
    print('Part 1: Final order: {}'.format(final_order))


# Part 2
def part2(dance_moves):
    pass


# Do the stuff
part1(data)
part2(data)