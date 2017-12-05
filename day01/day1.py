#####################################
#  Advent of Code 2017              #
#  Day 1: Inverse Captcha           #
#  April Jackson                    #
#####################################

def part1(captcha):
    solution = 0
    for i in range(0, len(captcha)):
        # print('for: {}'.format(i))
        if i == len(captcha) - 1:
            # print('if: {}'.format(i))
            if captcha[i] == captcha[0]:
                # print('if/if: {}'.format(i))
                solution += int(captcha[i])
        elif captcha[i] == captcha[i+1]:
            # print('elif: {}'.format(i))
            solution += int(captcha[i])

    print('Part 1: Captcha solution: {}'.format(solution))

def part2(captcha):
    solution = 0
    steps = int(len(captcha)/2)

    for i in range(0, len(captcha)):
        # print('for: {}'.format(i))
        match = i + steps
        if match >= len(captcha):
            # print('if; match: {}'.format(match))
            match -= len(captcha)
        # print('match: {}'.format(match))

        if captcha[i] == captcha[match]:
            # print('i: {}; match: {}'.format(i, match))
            solution += int(captcha[i])

    print('Part 2: Captcha solution: {}'.format(solution))


captcha = input('Captcha: ')
part1(captcha)
part2(captcha)