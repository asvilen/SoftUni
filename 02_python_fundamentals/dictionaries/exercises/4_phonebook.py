phone_book = {}
while True:
    contact = input()
    if contact.isnumeric():
        break
    name, phone_number = contact.split("-")
    phone_book[name] = phone_number
number_of_contacts_to_search = int(contact)
for search in range(number_of_contacts_to_search):
    name_to_search = input()
    if name_to_search in phone_book:
        print(f"{name_to_search} -> {phone_book[name_to_search]}")
    else:
        print(f"Contact {name_to_search} does not exist.")