import re

EMAIL_RGX = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'


def email_validator(email):
    check = re.fullmatch(EMAIL_RGX, email)
    return check