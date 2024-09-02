import re

def check_user_password(passwd):
    if not re.search(r"^(?=.*\d).{5,10}$",passwd):
        return False
    return True

def check_user_gmail(email):
    if not re.search(r"^[a-zA-Z0-9._]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$", email):
        return False
    return True