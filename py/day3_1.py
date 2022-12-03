import string

def main():

    with open("../../inputs/day3/input1.txt") as f:

        raw_data = f.read().split('\n')
        # Break down the string into halves and then: [[string, string], [string, string], ...]
        data_P1 = [[x[:len(x)//2], x[len(x)//2:]] for x in raw_data]
        # List of strings in groups of 3: [[string, string, string], [string, string, string], ...]
        data_P2 = [[raw_data[i], raw_data[i+1], raw_data[i+2]] for i in range(0, len(raw_data), 3)]

    # Dictionary where key = letter a-zA-Z and value = index in list
    priorities = {letter: (i + 1) for i, letter in enumerate(string.ascii_lowercase + string.ascii_uppercase)}

    P1_answer = 0
    P2_answer = 0

    # P1
    for d in data_P1:
        comp1 = d[0]
        comp2 = d[1]
        # Return a list of letters that appears in both string halves. As per specifications, only one such letter exists between both halves so only first index is needed
        common = [x for x in comp1 if x in comp2][0]
        
        P1_answer += priorities[common]

    # P2
    for d in data_P2:
        # Similar logic as in P1, but shuffle source data around and compare letters in groups of 3
        badge = [x for x in d[0] if x in d[1] and x in d[2]][0]
        
        P2_answer += priorities[badge]

    print(f"P1 answer: {P1_answer}")
    print(f"P2 answer: {P2_answer}")

if __name__ == "__main__":
    main()