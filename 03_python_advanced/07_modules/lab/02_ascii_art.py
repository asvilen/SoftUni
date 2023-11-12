from pyfiglet import figlet_format

input_text = input()
def print_art(message):
    return figlet_format(message)

print(print_art(input_text))