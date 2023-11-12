class MustContainAtSymbolError(Exception):
    pass


class NameTooShort(Exception):
    pass


class InvalidDomainError(Exception):
    pass


EMAIL_MIN_LENGTH = 5
VALID_DOMAINS = ["com", "bg", "net", "org"]

while True:
    new_email = input()
    if new_email == "End":
        break

    if "@" not in new_email:
        raise MustContainAtSymbolError("Email must contain @")

    handle = new_email[:new_email.index("@")]
    domain = new_email.split(".")[-1]

    if len(handle) < EMAIL_MIN_LENGTH:
        raise NameTooShort("Name must be more than 4 characters")

    if domain not in VALID_DOMAINS:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    print("Email is valid")
