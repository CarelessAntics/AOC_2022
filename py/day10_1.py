def main():


    with open("../inputs/day10/input1.txt") as f:
        signal = [x if len(x) == 1 else [int(y) if y.lstrip('-').isnumeric() else y for y in x.split(' ')] for x in f.read().split('\n')]


    P1_answer = 0
    P2_answer = 0

    P1_answer = P1_process_signal(signal)
    P2_answer = P2_draw_CRT(signal)

    print(f"P1 answer: {P1_answer}")
    print(f"P2 answer: {P2_answer}")


def P1_process_signal(signal):


    cycle = 0
    index = 0
    addx_counter = 0
    signal_strengths = []
    register = 1

    # Loop through commands until you can't
    while True:
        cycle += 1

        try:
            current_command = signal[index]
        except IndexError:
            break

        # Signal strengths are received at the 20th cycle, and every 40 cycles after that. Same as if first cycle started from -20 and was always every 40th cycle
        if (cycle - 20) % 40 == 0:
            # print(f"{cycle}: {register} -> {register * cycle}")
            signal_strengths.append(register * cycle)

        if current_command[0] == 'noop':
            index += 1

        # Track how many cycles you have processed the addx-command. On the second run, reset counter and perform addition
        elif current_command[0] == 'addx':
            if addx_counter == 0:    
                addx_counter += 1  
            else:
                addx_counter = 0
                register += current_command[1]
                index += 1

    return sum(signal_strengths)


def P2_draw_CRT(signal):


    cycle = 0
    command_index = 0
    addx_counter = 0
    rows = [['.'] * 40 for i in range(6)]
    row_index = 0
    register = 1

    # Init CRT rows as dots. Draw a pixel when conditions are met. Otherwise perform the commands as in P1
    while True:
        row_index = int(cycle / 40)
        px_index = cycle % 40

        cycle += 1

        try:
            current_command = signal[command_index]
            current_row = rows[row_index]
        except IndexError:
            break

        if px_index <= register + 1 and px_index >= register - 1:
            current_row[px_index] = '#'

        if current_command[0] == 'noop':
            command_index += 1

        elif current_command[0] == 'addx':
            if addx_counter == 0:    
                addx_counter += 1  
            else:
                addx_counter = 0
                register += current_command[1]
                command_index += 1

    print_rows(rows)


def print_rows(rows):
    print('-' * 40)
    for row in rows:
        print(''.join(row))
    print('-' * 40)


if __name__ == '__main__':
    main()