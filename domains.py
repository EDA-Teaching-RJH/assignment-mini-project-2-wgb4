# This is a class that all emails fall under
class Domain:
    def __init__(self, domain_name):
        # Assign the objects variables
        self.domain_name = domain_name
        self.usernames = []

    def add_username(self, username):
        # Add the unique username to the list of usernames under this domain
        self.usernames.append(username)

    def to_dictionary(self):
        # Output the domains data in a dictionary format
        return {
            "domain_name" : self.domain_name,
            "usernames" : self.usernames
        }
    
# This class is for domains that match a 'special type' list
class SpecialDomain(Domain):
    def __init__(self, domain_name, domain_category):
        super().__init__(domain_name)
        self.domain_category = domain_category

    def to_dictionary(self):
        return {
            "domain_name" : self.domain_name,
            "category" : self.domain_category,
            "usernames" : self.usernames
        }