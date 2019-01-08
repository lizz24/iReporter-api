class User:
    # user class
    def __init__(self, *args):
        self.id = args[0]
        self.firstname = args[1]
        self.lastname = args[2]
        self.othernames = args[3]
        self.email = args[4]
        self.phoneNumber = args[5]
        self.username = args[6]
        self.registered = args[7]
        self.isAdmin = args[8]
        self.password = args[9]
        self.password_confirm = args[10]

    def get_user_details(self):
        # getting one user
        return {
            "id": self.id,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "othernames": self.othernames,
            "email": self.email,
            "phoneNumber": self.phoneNumber,
            "username": self.username,
            "registered": self.registered,
            "isAdmin": self.isAdmin
        }
