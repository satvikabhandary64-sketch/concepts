#Question 1

num=int(input("Enter a number: "))
if num>1 and num<100:
    print("The number is between 1 and 100")
else:
    print("Number is not valid")

#Question 2

num=int(input("Enter a number: "))
if num%2==0:
    print("Number is even")
    print(num)
else:
    print("Number is oddd")
    print(num)

#Question 3

num=int(input("Enter a valid number: "))
if num>=1 and num<=12:
    if num==1:
        print("January")
    elif num==2:
        print("February")
    elif num==3:
        print("March")
    elif num==4:
        print("April")
    elif num==5:
        print("May")
    elif num==6:
        print("June")
    elif num==7:
        print("July")
    elif num==8:
        print("August")
    elif num==9:
        print("September")
    elif num==10:
        print("October")
    elif num==11:
        print("November")
    elif num==12:
        print("December")
else:
    print("The number entered is not valid")


#Question 4

marks=int(input("Enter marks: "))

if marks>80:
    print("Grade: A")
elif marks>60:
    print("Grade: B")
elif marks>50 and marks<=60:
    print("Grade: C")
elif marks>45 and marks<=50:
    print("Grade: D")
elif marks>25 and marks<=45:
    print("Grade: E")
else:
    print("Grade: F")

#Question 5
num=int(input("Enter a number: "))
if num%7==0:
    print("Number is divisible by 7")
else:
    print("Number is not divisible by 7")

#Question 6

num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
operator=input("Enter appropriate mathematical operator: ")
if operator=="+":
    print("Your answer is: ", num1 + num2)
elif operator=="-":
    print("Your answer is: ", num1 - num2)
elif operator=="*":
    print("Your answer is: ", num1 * num2)
elif operator=="/":
    print("Your answer is: ", num1/num2)
elif operator=="//":
    print("Your answer is: ", num1// num2)
elif operator=="%":
    print("Your answer is: ", num1% num2)
elif operator=="**":
    print("Your answer is: ", num1**num2)
else:
    print("The operator is invalid")


#Question 7

salary=int(input("Enter salary amount: "))
credit_score=int(input("Enter credit score: "))
if salary>=50000 and credit_score>=700:
    print("Eligible for car loan")
else:
    print("Not eligible for car loan")

#Question 8
n=int(input("Enter a number: "))
if n%3==0 and n%5==0:
    print("FizzBuzz")
elif n%5==0:
    print("Buzz")
elif n%3==0:
    print("Fizz")
else: 
    print(n)

#Question 9
char=input("Enter a character: ").lower()
if not char.isalpa():
    print("Invalid character")
elif char in "aeiou":
    print("Vowel")
else:
    print("Consonant")

#Question 10
marks=int(input("Enter marks: "))
if marks>=90 and marks<=100:
    print("Grade: A")
elif marks>=80 and marks<=89:
    print("Grade: B")
elif marks>=70 and marks<=79:
    print("Grade: C")
else:
    print("Grade: Fail")

#Question 11
age=int(input("Enter your age: "))
if age<13:
    print("Child")
elif age>=13 and age<=19:
    print("Teenager")
else:
    print("Adult")

#Question 12
char=input("Enter a character: ")
if char.isupper():
    print("Character is uppercase ")
elif char.islower():
    print("Character is lowercase")
elif char.isdigit():
    print("Character is a digit")
else:
    print("Invalid input")

#Question 13
colour=input("enter red, green or yellow: ").lower()
if colour=="red":
    print("Stop")
elif colour=="yellow":
    print("Get Ready")
elif colour=="green":
    print("Go")
else:
    print("Invalid colour input")

#Question 14
age=int(input("Enter your age: "))
experience=int(input("Enter years of work experience: "))
if age>18 and experience>=2:
    print("Eligible for job")
else:
    print("Not eligible for job")

#Question 15
temperature=int(input("Enter current temperature: "))
if temperature>30:
    print("It is hot, stay hydrated")
elif temperature>=15 and temperature<=30:
    print("Enjoy the weather")
else:
    print("It is cold, wear warm clothes")

#Question 16
menu=input("Choose pizza, burger or pasta: ").lower()
if menu=="pizza":
    print("Pizza: $10")
elif menu=="burger":
    print("burger: $7")
elif menu=="pasta":
    print("pasta: $8")

#Question 17
height=int(input("Enter player's height: "))
if height>=6:
    print("Player is selected")
else:
    print("Player is not selected")

#Question 18
age=int(input("Enter your age: "))
if age>=18:
    print("Eligible to watch movie")
else:
    print("Not eligible to watch movie")

#Question 19
Username= "admin"
password= "password123"

entered_user=input("Enter username: ")
entered_pass=input("Enter password: ")
if entered_user==Username and entered_pass==password:
    print("Acess Granted")
else:
    print("Access denied")

#Question 20
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