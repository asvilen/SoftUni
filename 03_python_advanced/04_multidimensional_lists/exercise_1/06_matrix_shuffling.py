rows, columns = [int(x) for x in input().split()]

matrix = [[x for x in input().split()] for rows in range(rows)]

while True:
    received_input = input()
    if received_input == "END":
        break
    command = received_input.split()
    if command[0] != "swap" or len(command) != 5:
        print("Invalid input!")
    else:
        first_element = [int(command[1]), int(command[2])]
        second_element = [int(command[3]), int(command[4])]
        try:
            matrix[first_element[0]][first_element[1]], matrix[second_element[0]][second_element[1]] \
                = matrix[second_element[0]][second_element[1]], matrix[first_element[0]][first_element[1]]
            [print(*row, sep=" ") for row in matrix]
        except IndexError:
            print("Invalid input!")
