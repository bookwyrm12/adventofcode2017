###############################
#  Advent of Code 2017        #
#  Day 20: Particle Swarm     #
#  April Jackson              #
###############################


# Imports
import re
from collections import defaultdict


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


# Helper: Update particles one tick, with destructive collisions
def tick_update_collision(position, velocity, accel):
    velocity = [[v + a for v, a in zip(vel, acc)] for vel, acc in zip(velocity, accel)]
    position = [[p + v for p, v in zip(pos, vel)] for pos, vel in zip(position, velocity)]

    tally = defaultdict(list)
    for i, pos in enumerate(position):
        pos = ','.join([str(x) for x in pos])
        tally[pos].append(i)
    dupes = [(key, locs) for key, locs in tally.items() if len(locs) > 1]

    if dupes:
        has_collision = True
        dupes = [i for sublist in dupes for i in sublist[1]] # flatten list of duplicate indeces
        dupes.sort(reverse=True) # reverse sort indeces
        for dupe in dupes:
            del position[dupe]
            del velocity[dupe]
            del accel[dupe]
    else:
        has_collision = False

    return position, velocity, accel, has_collision


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
def part2(position, velocity, accel):
    counter = 0

    while counter < 1000:
        print('counter: {}'.format(counter))
        position, velocity, accel, has_collision = tick_update_collision(position, velocity, accel)
        if has_collision:
            counter = 0
        else:
            counter += 1

    particles_left = len(position)
    print('Part 2: Particles left after collisions: {}'.format(particles_left))


# Do the stuff
position, velocity, accel = get_particle_data(data)
part1(position, velocity, accel)
part2(position, velocity, accel)