import re


def passwordRules():
    rules = "Minimum length is 5; \nMaximum length is 10; \nShould contain at least one number; \nShould contain at least one special character (such as &, +, @, etc); \nShould not contain spaces."

    print(rules)

passwordRules()

def messageOutput(message_str):
    print(message_str);

user_password = input("Please enter a password to login...  ")
if len(user_password) < 5:
    user_password = ("Please enter a valid password with minimum of 5 characters")