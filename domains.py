class Domain:
    def __init__(self, domain_name):
        self.domain_name = domain_name
        self.usernames = []

    def add_username(self, username):
        self.usernames.append(username)

    def to_dictionary(self):
        return {self.domain_name: self.usernames}