first_line = input()
second_line = input()


def data_types(input, second_input):
    if input == "int":
        print(int(second_input) * 2)
    elif input == "real":
        second_input = float(second_input)
        print(f"{second_input * 1.5:.2f}")
    elif input == "string":
        print(f"${second_input}$")


data_types(first_line, second_line)
