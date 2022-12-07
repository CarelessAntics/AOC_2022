def main():


    with open("../inputs/day7/input1.txt") as f:
        commands = [x.split(' ') for x in f.read().split('\n')]

    P1_answer = 0
    P2_answer = 0

    # Build the Tree object from puzzle input
    file_system = build_tree(commands)

    size_buffer = {}
    file_system.get_dir_sizes(size_buffer)

    # file_system.print_tree()
    # print(size_buffer)
    
    P1_answer = P1_solver(size_buffer)
    P2_answer = P2_solver(size_buffer)
    
    print(f"P1_answer: {P1_answer}")
    print(f"P2_answer: {P2_answer}")


class Tree:


    def __init__(self):
        self.root = Node('/')
        self.current = self.root

    def change_dir(self, dir_name):

        if dir_name == '..':
            self.current = self.current.parent
            return

        elif dir_name == '/':
            self.current = self.root
            return

        elif dir_name not in self.current.dirs.keys():
            self.current.add_dir(dir_name)
        
        self.current = self.current.dirs[dir_name]

    def add_dir(self, name):
        self.current.add_dir(name)

    def add_file(self, file_data):
        self.current.add_file(file_data)

    # Takes in a buffer dictionary, and recursively calculates the size of each directory, including directories inside current directory
    def get_dir_sizes(self, sizes, start=None, path='/'):
        if start is None:
            start = self.root
        else:
            path += start.name + '/'

        total_size = 0
        # If current node has child directories, call this function on each of them and return their sizes.
        if start.dirs:
            for d in start.dirs.values():
                total_size += self.get_dir_sizes(sizes, d, path)
        
        # Regardless of child directories, add the size of current node to the total, and add it to the buffer. Then return the size
        total_size += start.get_dir_size()
        sizes[path] = total_size

        return total_size

    # Prints out a formatted version of the tree object
    def print_tree(self, start=None, depth=1):
        if start is None:
            start = self.root

        tab = ('  ' * depth)
        print('> ' + start.name)

        if start.files:
            for file, size in start.files.items():
                print(tab + f' file={file}, size={size}')

        if start.dirs:
            for d in start.dirs.values():
                print(tab, end='')
                self.print_tree(d, depth+1)
        else:
            return
            

class Node:


    def __init__(self, name, parent=None):
        self.parent = parent
        self.name = name
        self.dirs = {}
        self.files = {}

    def add_file(self, file_input):
        file = file_input[1]
        size = int(file_input[0])
        self.files[file] = size

    def add_dir(self, directory):
        if directory not in self.dirs.keys():
            self.dirs[directory] = Node(directory, self)

    def get_dir_size(self):
        size_total = 0
        for file, size in self.files.items():
            size_total += size

        return size_total


def build_tree(commands):


    file_system = Tree()

    for command in commands:
        if command[0] == '$' and command[1] == 'cd':
            file_system.change_dir(command[2])
            continue

        if command[0] == '$' and command[1] == 'ls':
            continue

        if command[0] == 'dir':
            file_system.add_dir(command[1])
            continue
        
        file_system.add_file(command)

    # file_system.print_tree(file_system.root)

    return file_system


def P1_solver(dir_sizes):


    count = 0

    for directory, size in dir_sizes.items():
        if size <= 100000:
            count += size

    return count


def P2_solver(dir_sizes):


    disk_space = 70000000
    used_space = dir_sizes['/']
    free_space = disk_space - used_space
    required_space = 30000000

    eligible_directories = {k:v for k, v in dir_sizes.items() if free_space + v >= required_space}

    return min(eligible_directories.values())



if __name__ == '__main__':
    main()