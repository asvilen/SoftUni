initial_input = input()
# Numbers lists
numbers_list = [int(number) for number in initial_input if number.isdigit()]
take_numbers = [number for index, number in enumerate(numbers_list) if index % 2 == 0]
skip_numbers = [number for index, number in enumerate(numbers_list) if index % 2 != 0]
# Non numbers lists
non_numbers_list = [non_number for non_number in initial_input if not non_number.isdigit()]

resulting_string = ""

for turn in range(len(take_numbers)):
    char_to_keep = int(take_numbers[turn])
    resulting_string += "".join(non_numbers_list[:char_to_keep])
    non_numbers_list = non_numbers_list[char_to_keep:]
    char_to_skip = int(skip_numbers[turn])
    non_numbers_list = non_numbers_list[char_to_skip:]

print(resulting_string)
