import re
import copy

def main():

    # Process input
    with open("../inputs/day5/input1.txt") as f:
        # Split input into crates and moves
        raw_data = f.read().split('\n\n')

        # All of the crates are length 3 (+space). Make a list of lists of strings by skipping through the input 4 indices at a time
        crates_raw = [[row[i+1] for i in range(0, len(row), 4)] for row in raw_data[0].split('\n')]
        crates = {}

        # Make a dictionary with key = crate column index+1 and value = list of crates with top crate at index 0
        for row in crates_raw[:-1]:
            for i, col in enumerate(row):
                j = i+1
                if j not in crates.keys():
                    crates[j] = []
                if col != ' ':
                    crates[j].append(col)

        # Split the other half of input string by newline, then split those strings by regex matching away the words around the commands
        moves = [[int(y) for y in list(filter(None, re.split("move | from | to ", x)))] for x in raw_data[1].split('\n')]

    P1_answer = 0
    P2_answer = 0

    P1_crates = P1_operate_crane(copy.deepcopy(crates), moves)
    P2_crates = P2_operate_crane(copy.deepcopy(crates), moves)

    P1_answer = ''.join([x[0] for x in P1_crates.values()])
    P2_answer = ''.join([x[0] for x in P2_crates.values()])

    print(f"P1 answer: {P1_answer}")
    print(f"P2 answer: {P2_answer}")
    

def P1_operate_crane(crates, rules):

    for rule in rules:
        amount = rule[0]
        start = rule[1]
        end = rule[2]

        for i in range(amount):
            crate = crates[start].pop(0)
            crates[end].insert(0, crate)

    return crates

def P2_operate_crane(crates, rules):

    crates = crates.copy()

    for rule in rules:
        amount = rule[0]
        start = rule[1]
        end = rule[2]

        stack = []

        for i in range(amount):
            stack.append(crates[start].pop(0))
        
        crates[end] = stack + crates[end]

    return crates

if __name__ == "__main__":
    main()