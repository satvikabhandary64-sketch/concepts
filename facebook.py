first_name= input("Enter your first name: ")
if first_name==' ':
    print("First name cannot be empty")
    is_first_name_valid=False

elif not first_name.isalpha():
    print("Use letters only")
    is_first_name_valid=False

else:
    is_first_name_valid=True
    print()

last_name= input("Enter your last name: ")
if last_name==' ':
    print("Last name cannot be empty")
    is_last_name_valid=False

elif not last_name.isalpha():
    print("Use letters only")
    is_last_name_valid=False

else:
    is_last_name_valid=True
    print()

email=input("Enter your email address: ")
if email==" ":
    print("Email cannot be empty")
    is_email_valid=False

elif "@" in email and "." in email:
    print("Email is valid")
    is_email_valid=True
else:
    is_email_valid=True
    print()

remail=input("Re-enter your email addresss: ")
if remail==" ":
    print("Re-email cannot be empty")
    is_remail_valid=False

elif not remail==email:
    print("Email address is invalid")
    is_remail_valid=True

else:
    is_remail_valid=True
    print("Email is valid")

password=input("Enter a password: ")
if password==" ":
    print("Password cannot be empty: ")
    is_password_valid=False

elif len(password)>=6:
    print("Password is valid")
    is_password_valid=True

else:
    is_password_valid=True
    print()

if is_first_name_valid==True and is_last_name_valid==True and is_email_valid==True and is_remail_valid==True and is_password_valid==True:
    print("Sign up is successful")
else:
    print("Sign up is unsuccessful")