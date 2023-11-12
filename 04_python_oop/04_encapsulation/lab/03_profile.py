class Profile:
    min_username_length = 5
    max_username_length = 15

    min_password_length = 8
    min_password_digits = 1
    min_password_upper = 1

    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, new_username):
        self.username_is_valid(new_username)
        self.__username = new_username

    def username_is_valid(self, new_username):
        if len(new_username) < self.min_username_length \
                or len(new_username) > self.max_username_length:
            raise ValueError("The username must be between 5 and 15 characters.")

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, new_password):
        self.password_is_valid(new_password)
        self.__password = new_password

    def password_is_valid(self, new_password):
        error_message = (f"The password must be {self.min_password_length} or more characters "
                         f"with at least {self.min_password_digits} digit "
                         f"and {self.min_password_upper} uppercase letter.")
        
        if len(new_password) < self.min_password_length:
            raise ValueError(error_message)

        if len([x for x in new_password if x.isupper()]) < self.min_password_upper:
            raise ValueError(error_message)

        if len([x for x in new_password if x.isdigit()]) < self.min_password_digits:
            raise ValueError(error_message)

    def __str__(self):
        return (f'You have a profile with username: "{self.username}" '
                f'and password: {"*" * len(self.password)}')


correct_profile = Profile("Username", "Passw0rd")
print(correct_profile)

