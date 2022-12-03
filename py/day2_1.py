def main():
    
    with open("../inputs/day2/input1.txt") as f:
        data = [tuple(row.split(' ')) for row in f.read().split('\n')]

    P1_total_score = 0
    P2_total_score = 0

    for move in data:
        P1_total_score += p1_round(move)
        P2_total_score += p2_round(move)

    print(f"P1 answer: Total score is {P1_total_score}")
    print(f"P2 answer: Total score is {P2_total_score}")


# Count score for 1 round of RPS based on part 1 rules
def p1_round(move):
    round_score = 0
    opponent_moves = ['A', 'B', 'C'] 
    your_moves = ['X', 'Y', 'Z']
    # Rotate your moves 1 spot to the left and form pairs with opponent moves to get all winning combinations
    winning_moves = list(zip(opponent_moves, your_moves[1:] + your_moves[:1]))
    
    # Score for chosen move
    round_score += your_moves.index(move[1]) + 1

    # Check if the current move is a winning combination or draw. Otherwise counts as a loss
    if move in winning_moves:
        round_score += 6
    elif your_moves.index(move[1]) == opponent_moves.index(move[0]):
        round_score += 3

    return round_score


#Count round score with new set of rules. Select (the index of) your move depending on desired game outcome
def p2_round(game):
    round_score = 0
    moves = ['A', 'B', 'C'] 
    opponent_move = moves.index(game[0])
    game_result = game[1]
    
    # Loss
    if game_result == 'X':
        your_move = (opponent_move - 1) % 3

    # Draw
    elif game_result == 'Y':
        round_score += 3
        your_move = opponent_move

    # Win
    elif game_result == 'Z':
        round_score += 6
        your_move = (opponent_move + 1) % 3

    # Score for chosen move
    round_score += your_move + 1

    return round_score

if __name__ == '__main__':
    main()