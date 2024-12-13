# Program that reads a csv with a list of emails
# uses re to separate the usernames and the domains
# write to a json file with separate lists for each domain, and the usernames included in that domains

import json
import re
from domains import Domain, SpecialDomain

# Basic email pattern, words and numbers of any length @ words and numbers of any length, then one or more repetiton of words or numbers of 2 or more in length
email_pattern = re.compile(r"\w+@\w+(\.\w{2,})+")


def main():
    # Fill the special domains dictionary from the json file
    special_domains = fill_special_domains("special_domains.json")
    # print(special_domains)

    # Go through the csv file, add valid and unique emails
    email_list = create_email_list("emails.csv")

    # Go through the list of emails, create domain objects for each unique domain
    domain_list = create_domains(email_list, special_domains)

    # Go through each domain, write the dictonary format to json file
    write_to_file("domains_users.json", domain_list)


def fill_special_domains(file_name):
    # Read from a json file that contains domains to match to the emails
    with open(file_name, 'r') as json_file:
        return json.load(json_file)

    

def create_email_list(file_name):
    email_list = []
    # Open the file with a list of emails
    with open(file_name, 'r') as emails:
        # Run for each line of the file
        for line in emails:
            # Remove the newline symbol from each email
            email = line.strip()
            # Verify that the email is valid, if not, skip
            if re.match(email_pattern, email):
                # Email is valid
                # print(email)

                # Add the clean email to the email list, protect against adding the same email again
                if email not in email_list:
                    email_list.append(email)
        
        return email_list
    

def create_domains(emails, special_domains={}):
    domain_list = []
    
    for email in emails:
        # For each email, split between the @
        username, domain_name = email.split('@')
        # For each email's second half, split between each .
        domain_levels = domain_name.split('.')

        # Start domain set to None so that if there are no domains yet, the first one can be added
        domain_object = None
        # If the chosen domain name matches one already in the list of domains, skip
        for domain in domain_list:
            if domain.domain_name == domain_name:
                domain_object = domain
                break

        # If there are no matching domains, 
        if domain_object == None:
            # for each category
            for category, keywords in special_domains.items():
                # for each level in the domain
                for level in domain_levels:
                    # if the current level matches the category's keywords
                    if level in keywords:
                        # create this domain as a special domain, with the addition of a category attribute
                        domain_object = SpecialDomain(domain_name, category)
                        # break so the most specific category is chosen; domains get more general as they go up layers
                        break

            # if no keywords are found, add the domain without a category
            if domain_object is None:
                domain_object = Domain(domain_name)

            # add the domain to the list
            domain_list.append(domain_object)
        
        # Add the username to the domain
        domain_object.add_username(username)

    # return the completed list of domain objects
    return domain_list

                
def write_to_file(file_name, domain_list):
    with open(file_name, 'w') as json_file:
        # Create a list that holds data of all the domains
        domains_data = []

        # For each domain in the list
        for domain in domain_list:
            domains_data.append(domain.to_dictionary())

        # Get the domains userlist as a dictionary and write it to file
        json.dump(domains_data, json_file, indent=4)


if __name__ == "__main__":
    main()