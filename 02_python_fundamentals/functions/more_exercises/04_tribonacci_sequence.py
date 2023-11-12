integer_input = int(input()) + 1


def tribonacci(integer):
    sequence_list = [0, 0, 1]
    for number in range(2, integer):
        current_number = sequence_list[number] + sequence_list[number - 1] + sequence_list[number - 2]
        sequence_list.append(current_number)
    for number in sequence_list[2:]:
        print(number, end=" ")


tribonacci(integer_input)