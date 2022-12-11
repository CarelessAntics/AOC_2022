from functools import reduce
from copy import deepcopy


def main():

    with open("../inputs/day11/input1.txt") as f:
        monkeys_raw = f.read().split('\n\n')
        monkeys = {}

        for i, monkey in enumerate(monkeys_raw):
            operations = monkey.split('\n')

            op = {}
            op['items'] = [int(x) for x in operations[1].split(': ')[1].split(', ')]
            op['operation'] = [int(x) if x.lstrip('-').isnumeric() else x for x in operations[2].split(': ')[1].replace('new = old ', '').split(' ')]
            op['test'] = int(operations[3].split(': ')[1].replace('divisible by ', ''))
            op['true'] = int(operations[4].split(': ')[1].replace('throw to monkey ', ''))
            op['false'] = int(operations[5].split(': ')[1].replace('throw to monkey ', ''))
            op['inspections'] = 0

            monkeys[i] = op

    P1_answer = 0
    P2_answer = 0

    P1_monkeys = deepcopy(monkeys)
    P2_monkeys = deepcopy(monkeys)

    simulate_simians(P1_monkeys, 20, 'P1')
    simulate_simians(P2_monkeys, 10000, 'P2')

    P1_answer = get_monkey_business(P1_monkeys)
    P2_answer = get_monkey_business(P2_monkeys)

    print(f"P1 answer: {P1_answer}")
    print(f"P2 answer: {P2_answer}")


def simulate_simians(monkeys, rounds, problem):


    # P2: Had to look this one up unfortunately. Wasn't aware of modular arithmetic before this
    # Multiply all divisors together. Taking 'worry % M' ensures that the checks validate but the worry amount won't get out of hand
    M = reduce(lambda x,y: x*y, tuple(x['test'] for x in monkeys.values()))

    for a_round in range(rounds):
        for n, monkey in monkeys.items():

            item_count = len(monkey['items'])
            monkey['inspections'] += item_count
            
            # item is each item's worry level
            for i in range(item_count):

                item = monkey['items'].pop(0)
                op = monkey['operation'][0]
                value = monkey['operation'][1] if not monkey['operation'][1] == 'old' else item
                worry = item

                # Only additions and multiplications in input
                if op == '+':
                    worry += value
                elif op == '*':
                    worry *= value

                if problem == 'P1':
                    worry = int(worry / 3)
                else:
                    worry = worry % M

                if worry % monkey['test'] == 0:
                    target = monkey['true']
                else:
                    target = monkey['false']

                monkeys[target]['items'].append(worry)

        # debug prints
        """
        print(f"Round {a_round+1}:")
        for n, monkey in monkeys.items():
            print(f"Monkey {n}: {monkey['items']}")
        print('-' * 10)

    for n, monkey in monkeys.items():
        print(f"Monkey {n} inspected items {monkey['inspections']} times.")
    print('-' * 10)
    """


def get_monkey_business(monkeys):

    # Take the first 2 elements of a reverse (desc) sorted list of the inspection counts of all monkeys, and multiply the elements together
    return reduce(lambda x, y: x*y, sorted([x['inspections'] for x in monkeys.values()], reverse=True)[:2])

    
if __name__ == '__main__':
    main()