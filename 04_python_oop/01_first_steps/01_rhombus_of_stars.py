def print_row(n):
    print("* " * n)


def print_top_half(n):
    for row in range(1, n + 1):
        print_row(row)


def print_bottom_half(n):
    for row in range(n - 1, 0, -1):
        print_row(row)


def print_triangle(n):
    print_top_half(n)
    print_bottom_half(n)


triangle_height = 5
print_triangle(triangle_height)
