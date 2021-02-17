import re


def passwordRules():
    rules = "Minimum length is 5; \nMaximum length is 10; \nShould contain at least one number; \nShould contain at least one special character (such as &, +, @, etc); \nShould not contain spaces."

    print(rules)

passwordRules()

def messageOutput(message_str):
    passwordRules()
    user_password = input(message_str)
    return user_password


user_password = input("Please enter a password to login...  ")
regexPass = r"(\w_+|\W+|\S+){1,10}"

failed = True
while failed:
    if (re.match(regexPass, user_password)):
        print("Password " + user_password + "\nTest: True")
        failed = False

    else:
        message_str = "Please enter a valid password... "
        user_password = messageOutput(message_str)
        

