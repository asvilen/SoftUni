def decode_message(message, instructions):
    for instruction in instructions:
        command, *args = instruction.split('|')
        if command == 'Move':
            number_of_letters = int(args[0])
            message = message[number_of_letters:] + message[:number_of_letters]
        elif command == 'Insert':
            index, value = int(args[0]), args[1]
            message = message[:index] + value + message[index:]
        elif command == 'ChangeAll':
            substring, replacement = args[0], args[1]
            message = message.replace(substring, replacement)

    return message


def main():
    encrypted_message = input().strip()
    instructions = []
    while True:
        command = input()
        if command == 'Decode':
            break
        instructions.append(command)

    decrypted_message = decode_message(encrypted_message, instructions)
    print(f"The decrypted message is: {decrypted_message}")


if __name__ == "__main__":
    main()
