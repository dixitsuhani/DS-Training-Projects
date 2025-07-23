# Write a pyhton function to check if a string is a valid email address.

import re
def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)
print(is_valid_email("dixitsuhani24@.com"))