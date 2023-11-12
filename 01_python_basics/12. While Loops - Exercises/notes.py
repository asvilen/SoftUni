favorite_book = input()
book_name = input()

searched = 0
failed = False

while book_name != favorite_book:
    searched += 1
    book_name = input()
    if book_name == "No More Books":
        failed = True
        break

if not failed:
    print(f"You checked {searched} books and found it.")
else:
    print(f"The book you search is not here!")
    print(f"You checked {searched} books.")