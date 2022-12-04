def main():

    with open("../inputs/day4/input1.txt") as f:
        data = [[tuple(int(z) for z in y.split('-')) for y in x.split(',')] for x in f.read().split('\n')]

    P1_answer = 0
    P2_answer = 0

    for d in data:
        if is_encased(d[0], d[1]) or is_encased(d[1], d[0]):
            P1_answer += 1
        if is_overlapping(d[0], d[1]) or is_overlapping(d[1], d[0]):
            P2_answer += 1
        
    print(f"P1 answer: {P1_answer}")
    print(f"P2 answer: {P2_answer}")


def is_encased(range_1, range_2):
    return range_1[0] >= range_2[0] and range_1[1] <= range_2[1]

def is_overlapping(range_1, range_2):
    return range_1[0] >= range_2[0] and range_1[0] <= range_2[1]

if __name__ == '__main__':
    main()