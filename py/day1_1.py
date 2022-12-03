def main():
    with open('../inputs/day1/input_1.txt') as f:
        data = f.read().split('\n\n')

    elves = [[int(y) for y in x.split('\n')] for x in data]

    # Problem 1
    P1_most_calories = 0
    P1_most_elf = 0

    for i, elf in enumerate(elves):
        calories = sum(elf)
        if calories > P1_most_calories:
            P1_most_calories = calories
            P1_most_elf = i

    # Problem 2
    P2_top3_calories = sum(sorted([sum(x) for x in elves], reverse=True)[:3])

    # Answers
    print(f'Answer1: The elf with most calories is index {P1_most_elf}, with {P1_most_calories} calories')
    print(f'Answer2: Combined TOP 3 calories is {P2_top3_calories} calories')

if __name__ == '__main__':
    main()