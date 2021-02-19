import re


def passwordRules():
    rules = "Minimum length is 5; \nMaximum length is 10; \nShould contain at least one number; \nShould contain at least one special character (such as &, +, @, etc); \nShould not contain spaces.\n\n"
    print(rules)

passwordRules()

def messageOutput(message_str):
    user_password = input(message_str)
    return user_password


valid_message_str = "\nPlease enter a valid password... "
user_password = input("Please enter a password to login...  ")
failed = True
while failed:

    if len(user_password) < 5:
        message = "\nPassword is too short!!!" + valid_message_str
        user_password = messageOutput(message)
        # continue

    elif len(user_password) > 10:
        message = "\nPassword is too long!!!" + valid_message_str
        user_password = messageOutput(message)

    elif not re.match(r"(?=.*[0-9]+)[\w+\W+\S+]", user_password):
        message = "\nA password must contain at least one number!!!" +  valid_message_str
        user_password = messageOutput(message)

    elif not re.match(r"(?=.*[a-zA-Z]+)[\w+\W+\S+]", user_password):
        message = "\nA password must contain at least one letter!!!" + valid_message_str
        user_password = messageOutput(message)

    elif not re.match(r"(?=.*[^a-zA-Z0-9]+)[\w+\W+\S+]", user_password):
        message = "\nInclude at least one special character (such as !, @, #, $, %, etc)!!!"
        message += valid_message_str
        user_password = messageOutput(message)
        

    elif re.match(r"(?=.*\s+)[\w+\W+\S+]", user_password): # Return object if theres space.
        message = "A password must not contain any spaces!!!" + valid_message_str
        user_password = messageOutput(message)

    else: 
        print("\nTHANK YOU!!!")
        print("Welcome, you are now logged in.")
        failed = False

        

