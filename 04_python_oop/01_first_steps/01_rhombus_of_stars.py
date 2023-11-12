def print_row(n, row):
    print(" " * (n - row), end="")
    print("* " * row)


def make_triangle(n):
    for row in range(1, n + 1):
        print_row(n, row)


def make_reversed_triangle(n):
    for row in range(n - 1, 0, -1):
        print_row(n, row)


def make_rhombus(n):
    make_triangle(n)
    make_reversed_triangle(n)


n = int(input())

make_rhombus(n)
