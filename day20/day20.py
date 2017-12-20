###############################
#  Advent of Code 2017        #
#  Day 20: Particle Swarm     #
#  April Jackson              #
###############################


# Imports
import re


# Get the data
with open('day20.in') as f:
    data = f.read()


# Helper: Get the position, velocity, and acceleration lists
def get_particle_data(data):
    valid_num_p = re.compile(r'p=<(-?\d+),(-?\d+),(-?\d+)>')
    valid_num_v = re.compile(r'v=<(-?\d+),(-?\d+),(-?\d+)>')
    valid_num_a = re.compile(r'a=<(-?\d+),(-?\d+),(-?\d+)>')

    position = []
    velocity = []
    accel = []

    for particle in data.splitlines():
        p = [int(x) for x in valid_num_p.search(particle).groups()]
        v = [int(x) for x in valid_num_v.search(particle).groups()]
        a = [int(x) for x in valid_num_a.search(particle).groups()]
        position.append(p)
        velocity.append(v)
        accel.append(a)
    return position, velocity, accel


# Helper: Update particles one tick
def tick_update(position, velocity, accel):
    velocity = [[v + a for v, a in zip(vel, acc)] for vel, acc in zip(velocity, accel)]
    position = [[p + v for p, v in zip(pos, vel)] for pos, vel in zip(position, velocity)]

    return position, velocity


# Helper: Get closest particle
def get_closest(position):
    closest, dist = 0, sum([abs(x) for x in position[0]])
    for i, pos in enumerate(position):
        pos = [abs(x) for x in pos]
        tmp_dist = sum(pos)
        if tmp_dist < dist:
            closest, dist = i, tmp_dist
    return closest


# Part 1
def part1(position, velocity, accel):
    closest_particle = None
    counter = 0

    while counter < 1000:
        print('counter: {}'.format(counter))
        position, velocity = tick_update(position, velocity, accel)
        new_close_particle = get_closest(position)
        if closest_particle == new_close_particle:
            counter += 1
        else:
            closest_particle = new_close_particle
            counter = 1

    print('Part 1: Particle closest to <0,0,0>: {}'.format(closest_particle))


# Part 2
def part2(data):
    pass


# Do the stuff
position, velocity, accel = get_particle_data(data)
part1(position, velocity, accel)
part2(data)