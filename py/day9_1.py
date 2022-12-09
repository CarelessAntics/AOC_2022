def main():


    with open("../inputs/day9/input1.txt") as f:
        rope_instructions = [[int(y) if y.isnumeric() else y for y in x.split(' ')] for x in f.read().split('\n')]

    P1_answer = 0
    P2_answer = 0

    P1_answer = P1_move_rope(rope_instructions)
    P2_answer = P2_move_rope(rope_instructions)

    print(f"P1 answer: {P1_answer}")
    print(f"P2 answer: {P2_answer}")


def P1_move_rope(instructions):


    tail_positions = {(0,0)}

    head = (0, 0)
    tail = (0, 0)

    for i in instructions:
        head = move_head(head, i)
        while not is_adjacent(head, tail):
            tail = move_tail(head, tail, tail_positions)

    return len(tail_positions)


# Luckily earlier functions can still be used for P2 with just changing the inputs to be other parts of the tail
def P2_move_rope(instructions):


    tail_positions = {(0,0)}

    head = (0, 0)
    tails = [(0, 0)] * 9
    tail_length = len(tails)

    for ins in instructions:
        head = move_head(head, ins)

        # Tail can't move directly to head like in P1. Must move one step at a time instead
        while not is_adjacent(tails[0], head):
            for i in range(tail_length):
                if i == tail_length -1:
                    tails[i] = move_tail(tails[i-1], tails[i], tail_positions)
                elif i == 0:
                    tails[i] = move_tail(head, tails[i])
                else:
                    tails[i] = move_tail(tails[i-1], tails[i])
        
        # print_snake(head, tails, tail_positions)

    return len(tail_positions)


# Teleport head to correct location. Works since head transform always has one component == 1
# P2 doesn't change the head transforms so still works
def move_head(start, ins):


    if ins[0] == 'R':
        target = (start[0] + ins[1], start[1])

    if ins[0] == 'L':
        target = (start[0] - ins[1], start[1])

    if ins[0] == 'U':
        target = (start[0], start[1] - ins[1])

    if ins[0] == 'D':
        target = (start[0], start[1] + ins[1])

    return target


def move_tail(head, tail, pos_buffer=set()):


    if not is_adjacent(head, tail):
        # Get the difference vector between current head and tail vectors
        # Get the length of longer component and use that to iterate
        difference = (head[0] - tail[0], head[1] - tail[1])

        # Generate one step of movement based on difference values
        movement = tuple(1 if x > 0 else -1 if x < 0 else 0 for x in difference)

        # Apply movement to tail. Update difference with movement vector
        tail = (tail[0] + movement[0], tail[1] + movement[1])
        difference = (difference[0] - movement[0], difference[1] - movement[1])

        pos_buffer.add(tail)

    return tail


def is_adjacent(a, b):


    difference = (abs(a[0] - b[0]), abs(a[1] - b[1]))
    return (difference[0] <= 1 and difference[1] <= 1)


# Print out the grid, rope, and path
def print_snake(head, tails, visited):


    max_x = max([head[0], max(x[0] for x in tails), max(x[0] for x in visited)])
    min_x = min([head[0], min(x[0] for x in tails), min(x[0] for x in visited)])

    max_y = max([head[1], max(y[1] for y in tails), max(y[1] for y in visited)])
    min_y = min([head[1], min(y[1] for y in tails), min(y[1] for y in visited)])
    offset = (12, 15)
    for y in range(min_y -1, max_y +2):
        for x in range(min_x -1, max_x +2):
            coord = (x, y)
            #coord = (x - offset[0], y - offset[1])

            if coord in tails:
                print("T", end='')
            elif coord == head:
                print("H", end='')
            elif coord == (0,0):
                print("S", end='')
            elif coord in visited:
                print("#", end='')
            else:
                print(".", end='')
        print()
    print('\n//////////\n')


if __name__ == '__main__':
    main()