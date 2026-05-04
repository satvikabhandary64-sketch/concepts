#Question number 1
'''balance=5000
amount=int(input("Withdraw amount: "))

if amount<=0:
    print("Input valid amount")
elif amount>balance:
    print("Insufficient funds")
else:
    balance-=amount
    print(f"New balance: {balance}")'''

#Question number 2
correct_password= "gurkhas123"
entered= "pass123"

#print("Login successful!")
#print("Welcome!!!")


'''username= "adminram"
password ="gurkhas123"

entered_user ="admin"
entered_passsword = "123"

if entered_user==username and entered_passsword==password:
    print("Login succefull, welcome")
elif entered_user!=username:
    print("Username not valid")
else:
    print("Wrong password")'''


marks=45

'''print("Grade: A+")
print("Grade: A")
print("Grade: B")
print("Grade: F")'''

'''if marks>=90:
    print("Grade: A+")
elif marks>=80:
    print("Grade: A")
elif marks>=70:
    print("Grade: B")
elif marks>=60:
    print("Grade: C")
elif marks>=50:
    print("Grade: D")
else:
    print("Grade: F, You have failed")'''


month=int(input("Enter a number between 1 to 12: "))
if month>=1 and month<=12:
    if month in (12,1,2):
        print("Winter")
    elif month in (3,4,5):
        print("Spring")
    elif month in (6,7,8):
        print("Summer")
    elif month in (9,10,11):
        print("Autumn")
else:
    print("Number is invalid")