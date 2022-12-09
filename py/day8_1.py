from functools import reduce


def main():


    with open("../inputs/day8/input1.txt") as f:
        forest_grid = [[int(x) for x in y] for y in f.read().split('\n')]

    P1_answer = 0
    P2_answer = 0

    P1_answer = P1_check_visibility(forest_grid)
    P2_answer = P2_check_scenery(forest_grid)

    print(f"P1 answer: {P1_answer}")
    print(f"P2 answer: {P2_answer}")


# Check if a tree is visible from any direction
def P1_check_visibility(grid):


    perimeter = len(grid) * 2 + (len(grid[0]) - 2) * 2
    directions = ['N', 'E', 'S', 'W']
    dimensions = (len(grid[0]), len(grid))
    count = perimeter

    for y, row in enumerate(grid):
        if y == 0 or y == len(grid)-1:
            continue
        
        for x, tree in enumerate(row):
            if x == 0 or x == len(grid)-1:
                continue

            visible = False
            # Check each direction. If any return true, increment count and break loop
            for direction in directions:
                if direction == 'N':
                    visible = not tuple(i[x] for i in grid[:y] if i[x] >= tree)
                elif direction == 'S':
                    visible = not tuple(i[x] for i in grid[y+1:] if i[x] >= tree)
                elif direction == 'E':
                    visible = not tuple(i for i in row[x+1:] if i >= tree)
                elif direction == 'W':
                    visible = not tuple(i for i in row[:x] if i >= tree)

                if visible:
                    count += 1
                    break
            
    return count


# Check how far can be seen from a given tree
def P2_check_scenery(grid):


    directions = ['N', 'E', 'S', 'W']
    scenery_values = []

    for y, row in enumerate(grid):
        if y == 0 or y == len(grid)-1:
            continue
        
        for x, tree in enumerate(row):
            if x == 0 or x == len(grid)-1:
                continue
            
            # Begin counting from current tree, and break loop when a taller tree is found. Repeat for each direction
            view_distance = {d:0 for d in directions}
            for direction in directions:
                if direction == 'N':
                    for i in reversed(grid[:y]):
                        view_distance[direction] += 1
                        if i[x] >= tree: break

                elif direction == 'S':
                    for i in grid[y+1:]:
                        view_distance[direction] += 1
                        if i[x] >= tree: break

                elif direction == 'E':
                    for i in row[x+1:]:
                        view_distance[direction] += 1
                        if i >= tree: break

                elif direction == 'W':
                    for i in reversed(row[:x]):
                        view_distance[direction] += 1
                        if i >= tree: break

            # print(f"({x},{y}) [{tree}] {view_distance}")
            scenery_values.append(reduce(lambda x, y: x*y, view_distance.values()))
            
    return max(scenery_values)


    
if __name__ == '__main__':
    main()