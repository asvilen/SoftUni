initial_list = [int(num) for num in input().split()]
result_list = initial_list
command = input()
while command != "end":
    command_list = command.split()
    clean_command = command_list[0]
    if clean_command == "exchange":
        index = int(command_list[1])
        if index >= len(result_list) or index < 0:
            print("Invalid index")
            continue
        result_list = result_list[index+1:] + result_list[:index+1]
    elif clean_command == "max":
        even_list = [num for num in result_list if num % 2 == 0]
        odd_list = [num for num in result_list if num % 2 != 0]
        even_odd = command_list[1]
        if even_odd == "even":
            if even_list:
                max_even_index = result_list[::-1].index(max(even_list))
                print(max_even_index)
            else:
                print("No matches")
        else:
            if odd_list:
                max_odd_index = result_list[::-1].index(max(odd_list))
                print(max_odd_index)
            else:
                print("No matches")
    elif clean_command == "min":
        even_list = [num for num in result_list if num % 2 == 0]
        odd_list = [num for num in result_list if num % 2 != 0]
        even_odd = command_list[1]
        if even_odd == "even":
            if even_list:
                min_even_index = result_list[::-1].index(min(even_list))
                print(min_even_index)
            else:
                print("No matches")
        else:
            if odd_list:
                min_odd_index = result_list[::-1].index(min(odd_list))
                print(min_odd_index)
            else:
                print("No matches")
    elif clean_command == "first":
        even_list = [num for num in result_list if num % 2 == 0]
        odd_list = [num for num in result_list if num % 2 != 0]
        count = int(command_list[1])
        even_odd = command_list[2]
        if even_odd == "even":
            if count > len(result_list):
                print("Invalid count")
            else:
                result_to_print = even_list[:count-1]
                print(result_to_print)
        else:
            if count > len(odd_list):
                print("Invalid count")
            else:
                result_to_print = odd_list[:count-1]
                print(result_to_print)

    elif clean_command == "last":
        even_list = [num for num in result_list if num % 2 == 0]
        odd_list = [num for num in result_list if num % 2 != 0]
        count = int(command_list[1])
        even_odd = command_list[2]
        if even_odd == "even":
            if count > len(result_list):
                print("Invalid count")
            else:
                result_to_print = even_list[:count-1:-1]
                print(result_to_print)
        else:
            if count > len(odd_list):
                print("Invalid count")
            else:
                result_to_print = odd_list[:count-1:-1]
                print(result_to_print)

    command = input()

print(result_list)

