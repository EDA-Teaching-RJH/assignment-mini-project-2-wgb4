

# Program that reads a csv with a list of emails
# uses re to separate the usernames and the domains
# write to a json file with separate lists for each domain, and the usernames included in that domains

import json
import re
import io
from domains import Domain

email_pattern = re.compile(r"\w+@\w+(\.\w{2,})+")

def main():
    # Go through the csv file, add unique domains to the list, add email usernames to the domains
    populate_domains(populate_email_list("emails.csv"))
    print(email_list)
    print(domain_list)
    # Go through all the domain objects, take the usernames list and make a json format out of them
    write_to_file("domains_users.json")
    
def populate_email_list(file_name):
    email_list = []
    # Open the file with a list of emails
    with open(file_name, 'r') as emails:
        # Run for each line of the file
        for email in emails:
            # Remove the newline symbol from each email
            email = email.strip()
            # Verify that the email is valid, if not, skip
            if re.match(email_pattern, email):
                # Email is valid
                # print(email)

                # Add the clean email to the email list, protect against adding the same email again
                if email not in email_list:
                    email_list.append(email)
        
        return email_list

def populate_domains(emails):
    domain_list = []

    for email in emails:
        # Split the email between the @ to get the username and domain seperately
        email_split = email.split('@')
        # print(email_split[-1])
        
        # For each domain in the list
        for domain in domain_list:
            # Add domain to the list of domains if it is new
            if email_split[-1] != domain.domain_name:
                domain_list.append(Domain(email_split[-1]))
            
            # If the email's domain is the same as the current domain iteration
            if email_split[-1] == domain.domain_name:
                # If the email is not in the domains username list already
                if email_split[0] not in domain.usernames:
                    # Add the username to the domain
                    domain.add_username(email_split[0])
                
def write_to_file(file_name):
    with open(file_name, 'w') as json_file:
        # For each domain in the list
        for domain in domain_list:
            # Get the domains userlist as a dictionary and write it to file
            json.dump(domain.to_dictionary(), json_file, indent=4)


if __name__ == "__main__":
    main()