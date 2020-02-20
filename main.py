class Book:
    def __init__(self, id, score):
        self.id = id
        self.score = score


class Lib:
    def __init__(self, id, books, signup_time, score):
        self.id = id
        self.books = books
        self.signup_time = signup_time
        self.score = score


class Problem:
    def __init__(self, days, libs):
        self.days = days
        self.libs = libs


def solver(problem):
    pass


def read_input(filepath,
               n_lines=None):
    with open(filepath) as fp:
        lines = fp.readlines()
    lines = [x.strip() for x in lines]
    if n_lines:
        return lines[:n_lines]
    else:
        return lines


def write_output(data, filepath):
    with open(filepath, 'w') as fp:
        for line in data:
            for number in line:
                fp.write(str(number))
                fp.write(' ')
            fp.write('\n')


if __name__ == "__main__":
    data = read_input('b_example.txt')
