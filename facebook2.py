first_name= input("Enter your first name: ")
last_name= input("Enter your last name: ")
email=input("Enter your email address: ")
remail=input("Re-enter your email addresss: ")
password=input("Enter a password: ")
if not (first_name and last_name and email and remail and password):
    print("all fields are mandatory")
elif not first_name.isalpha():
    print("must type letters only")
elif '@' not in email or '.' not in email or '@' not in remail and '.' not in remail:
    print("invalid email address")
elif email!=remail:
    print("Email does not match")
elif len(password)<6:
    print("password length must be greater than 6")
else:
    print("registration is successful")


