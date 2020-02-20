class Book:
    def __init__(self, id, score):
        self.id = id
        self.score = score

class Lib:
    def __init__(self, id, books, signup_time, books_per_day = 0, score=0, used_books=[]):
        self.id = id
        self.books = books
        self.signup_time = signup_time
        self.score = score
        self.used_books = used_books
        self.books_per_day = books_per_day

class Problem:
    def __init__(self, days, libs):
        self.days = days
        self.inited_libs = []
        self.pending = None
        self.uninited_libs = libs


def solver(problem):
    day = 0
    
    # sort libs by signup_day (equal not yet done, do later)
    problem.uninited_libs = {k: v for k, v in sorted(problem.uninited_libs.items(), key = lambda item: item[1].signup_time)}

    while(day < problem.days):

        # start init of one lib
        if problem.pending == None:
            if len(problem.uninited_libs) > 0:
                problem.pending = problem.uninited_libs[(list(problem.uninited_libs.keys()))[0]]
                init_day = problem.pending.signup_time + day
                del problem.uninited_libs[problem.pending.id]

        # do book reading here
        for lib in problem.inited_libs:
            # fix this check with extra list, saves comp time
            # ^ don't do this, makes output parsing harder
            if len(lib.books) > 0: 
                # note: assumes books in the lib are sorted by score, highest first!!
                read_books = list(lib.books)[:min(lib.books_per_day, len(lib.books))]
                # remove read_books from books
                lib.books = list(lib.books)[min(3, len(lib.books)):]
                lib.used_books = lib.used_books + read_books

        # all read books must be removed from all libs, and recalc)
        # skip for now
            
        # if init day is reached, move lib from pending to inited_libs
        if day == init_day:
            problem.inited_libs.append(problem.pending)
            problem.pending = None
        
        # increment day
        day += 1

def convert_to_objects(data):
    all_books = {}
    libs = {}
    for i, score in enumerate(data[1]):
        all_books[i] = Book(id=i, score=score)
    for i in range(2, len(data), 2):
        libs[(i - 2) / 2] = Lib(id=(i - 2) / 2, books={}, signup_time=data[i][1], books_per_day=data[i][2])
        for j in range(0, len(data[i + 1])):
            libs[(i - 2) / 2].books[data[i + 1][j]] = all_books[data[i + 1][j]]
    problem = Problem(data[0][2], libs)
    return problem


def read_input(filepath,
               n_lines=None):
    with open(filepath) as fp:
        lines = fp.readlines()
    lines = [x.split() for x in lines]
    for line in lines:
        for i in range(0, len(line)):
            line[i] = int(line[i])
    if n_lines:
        return lines[:n_lines]
    else:
        return lines


def write_output(problem, filepath):
    with open(filepath, 'w') as fp:
        fp.write("{}\n".format(str(len(problem.inited_libs))))
        for library in problem.inited_libs:
            fp.write("{} {}\n".format(library.id, len(library.books)))
            for book in sorted(library.books.keys()):
                fp.write("{} ".format(book))
            fp.write("\n")


if __name__ == "__main__":
    filepath = 'a_example.txt'
    data = read_input('a_example.txt')
    swag = convert_to_objects(data)
    solver(swag)
    write_output(swag, "{}_solved".format(filepath[0]))

