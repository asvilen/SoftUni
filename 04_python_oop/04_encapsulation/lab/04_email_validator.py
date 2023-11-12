class EmailValidator:
    def __init__(self, min_length: str, mails: list, domains: list):
        self.min_length = min_length
        self.mails = mails
        self.domains = domains

    def __is_name_valid(self, name):
        return len(name) >= self.min_length

    def __is_mail_valid(self, mail):
        return mail in set(self.mails)

    def __is_domain_valid(self, domain):
        return domain in set(self.domains)

    def validate(self, email):
        name, mailer = email.split("@")
        mail = mailer.split(".")[0]
        domain = mailer[mailer.index(".") + 1:]
        return self.__is_name_valid(name) \
            and self.__is_mail_valid(mail) \
            and self.__is_domain_valid(domain)


mails = ["gmail", "softuni"]
domains = ["com", "bg"]
email_validator = EmailValidator(6, mails, domains)
print(email_validator.validate("pe77er@gmail.com"))
print(email_validator.validate("georgios@gmail.net"))
print(email_validator.validate("stamatito@abv.net"))
print(email_validator.validate("abv@softuni.bg"))
