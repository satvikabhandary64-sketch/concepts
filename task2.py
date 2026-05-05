#Question 1
age=int(input("Enter your age: "))
height=int(input("Enter your height: "))
if age>=12 and height>=140:
    print("You can ride the roller coaster")
else:
    print("You cannot ride the roller coaster")

#Question 2
colour=input("Enter a colour (Red, Yellow, Green): ").lower()
if colour=="red":
    print("Stop")
elif colour=="yellow":
    print("Get Ready")
elif colour=="green":
    print("Go")
else:
    print("Invalid colour")

#Question 3
num=int(input("Enter a number between 1 and 4:" ))
if num==1:
        print("Spring")
elif num==2:
        print("Summer")
elif num==3:
        print("Autumn")
elif num==4:
        print("Winter")
else:
      print("Invalid number")


num=int(input("Enter a number between 1 and 4: "))
match num:
    case 1:
            print("spring")
    case 2:
            print("summer")
    case 3:
            print("autumn")
    case 4:
            print("winter")
    case _:
            print("Invalid input")

#Question 4
username= "admin"
password= "pass123"

entered_username=input("Enter username: ")
entered_password=input("Enter password: ")
if entered_username==username:
      if entered_password==password:
            print("valid login")
      else:
            print("wrong password")
else:
      print("wrong username")

#Question 5
age=int(input("Enter your age: "))
monthly_income=int(input("Enter your income: "))
credit_score=int(input("Enter your credit score: "))

if not (age>=21 and age<=60):
      print("Not approved: Age must be between 21 and 60")
elif not monthly_income>=30000:
      print("Not approved: Monthly income must be above 30000 ")
elif not credit_score>=700:
      print("Not approved: Credit score must be over 700")
else:
      print("You are eligible for loan")

#Question 6
age=int(input("Enter your age: "))


if age<12:
      print("The ticket is free")
elif age>=12 and age<=60:
      membership_card=(input("Do you have a membership card?")).lower()
      if membership_card=="yes":
            print("The cost of the ticket is 150")
      else:
            print("The cost of the ticket is 200")
else:
      print("The cost of the ticket is 100")

#Question 7
salary=int(input("Enter your salary: "))
service=int(input("Enter years of service: "))
bonus=0.05
if service>5:
      net_bonus=salary*bonus
      print("You have recieved bonus of: ", net_bonus)
else:
      print("You are not eligible for bonus")

#Question 8
radius=float(input("Enter radius of circle: "))
pi=3.141592
if radius>0:
      area=pi*radius**2
      print("Area of circle: ", area)
else:
      print("Radius must be positive")

#Question 9
age=int(input("Enter your age: "))
gender=input("Enter M or F: ").upper()
if age>=18 and age<30 and gender=="M":
      print("Daily wage is 700")
elif age>=18 and age<30 and gender=="F":
      print("Daily wage is 750")
elif age>=30 and age<=40 and gender=="M":
      print("Daily wage is 800")
elif age>=30 and age<=40 and gender=="F":
      print("Daily wage is 850")
else:
      print("Invalid age")

#Question 10
n=int(input("Enter a number: "))
if n%3==0 and n%5==0:
    print("FizzBuzz")
elif n%5==0:
    print("Buzz")
elif n%3==0:
    print("Fizz")
else: 
    print(n)