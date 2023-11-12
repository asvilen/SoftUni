def add_piece(pieces, piece_info):
    piece, composer, key = piece_info
    if piece not in pieces:
        pieces[piece] = {"composer": composer, "key": key}
        print(f"{piece} by {composer} in {key} added to the collection!")
    else:
        print(f"{piece} is already in the collection!")


def remove_piece(pieces, piece):
    if piece in pieces:
        del pieces[piece]
        print(f"Successfully removed {piece}!")
    else:
        print(f"Invalid operation! {piece} does not exist in the collection.")


def change_key(pieces, piece, new_key):
    if piece in pieces:
        pieces[piece]["key"] = new_key
        print(f"Changed the key of {piece} to {new_key}!")
    else:
        print(f"Invalid operation! {piece} does not exist in the collection.")


def print_collection(pieces):
    for piece, info in pieces.items():
        composer = info["composer"]
        key = info["key"]
        print(f"{piece} -> Composer: {composer}, Key: {key}")


def main():
    n = int(input())
    pieces = {}

    for _ in range(n):
        piece_info = input().split("|")
        piece, composer, key = piece_info
        if piece not in pieces:
            pieces[piece] = {"composer": composer, "key": key}

    while True:
        command = input()
        if command == "Stop":
            break

        command_args = command.split("|")
        action = command_args[0]
        piece = command_args[1]

        if action == "Add":
            composer = command_args[2]
            key = command_args[3]
            add_piece(pieces, (piece, composer, key))
        elif action == "Remove":
            remove_piece(pieces, piece)
        elif action == "ChangeKey":
            new_key = command_args[2]
            change_key(pieces, piece, new_key)

    print_collection(pieces)


if __name__ == "__main__":
    main()
