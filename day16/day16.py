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
    sequence = list('abcdefghijklmnop')
    # sequence = ['a', 'b', 'c', 'd', 'e']
    return sequence


# Helper: Do the dance
def do_the_dance(programs, dance_moves):
    new_programs = programs[:]
    for move in dance_moves:
        if move[0] == 's': # Spin
            num = int(move[1:])
            end = new_programs[-num:]
            the_rest = new_programs[:-num]
            new_programs = end + the_rest

        elif move[0] == 'x': # Exchange
            positions = move[1:].split('/')
            pos_a = int(positions[0])
            pos_b = int(positions[1])
            a = new_programs[pos_a]
            b = new_programs[pos_b]
            new_programs[pos_a] = b
            new_programs[pos_b] = a

        elif move[0] == 'p': # Partner
            progs = move[1:].split('/')
            a = progs[0]
            b = progs[1]
            pos_a = new_programs.index(a)
            pos_b = new_programs.index(b)
            new_programs[pos_a] = b
            new_programs[pos_b] = a

    return new_programs


# Part 1
def part1(dance_moves):
    dance_moves = [move for move in dance_moves.split(',')]
    print(dance_moves)

    programs = get_intial_program_sequence()
    programs = do_the_dance(programs, dance_moves)

    final_order = ''.join(programs)
    print('Part 1: Final order: {}'.format(final_order))


# Part 2
def part2(dance_moves):
    pass


# Do the stuff
part1(data)
part2(data)