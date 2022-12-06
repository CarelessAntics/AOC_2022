def main():

    with open("../inputs/day6/input1.txt") as f:
        signal = f.read()

    P1_answer = detect(signal, 4)
    P2_answer = detect(signal, 14)

    print(f"P1 answer: {P1_answer}")
    print(f"P1 answer: {P2_answer}")

def detect(signal, size):
    buffer = []
    for i, symbol in enumerate(signal):
        if symbol not in buffer:
            buffer.append(symbol)
        else:
            cutoff = buffer.index(symbol)
            buffer = buffer[cutoff+1:]
            buffer.append(symbol)

        if len(buffer) == size:
            return i + 1

    return None


if __name__ == '__main__':
    main()