#Question 1
for i in range(1,6):
    if i%2==0:
        print(f'Number {i} is even')
    else:
        print(f'Number {i} is odd')

#Question 2
list=[10,20,30,40]
total=0

for i in list:
    total+=i
    print(f'Added {i}. Running total is {total}')
print(f'Total sum is {total}')

#Question 3
Heading="Email Greetings Generated"
print(Heading.center(31,"-"))

student_names = ["Ram", "Hari", "Sita"]
for i in student_names:
    print(f'Hi {i}, your course approval is ready!')

#Question 4
Header="Book Chapter Summary"
print(Header.center(26,"-"))
count=1
page=[45, 30, 50, 40] 

for i in page:
    print(f'Chapter {count} has {i} pages.')
    count+=1

#Question 5
total=1
mult=4
list=[4,5,3,2]
for i in list:
    total=total*i
print(total)


#Question 6
num=11
for i in range(1,11):
    print(f'{num} * {i} = {num*i}')

#Question 7
list = [3,2,1,4,5]
r_list=[]

for i in list:
    r_list.insert(0,i)
print(r_list)

#Question 8
list_1=[1,2,3,4,5] 
list_2=[3,4,5,6,7] 
common_elements=[]

for i in list_1:
    if i in list_2:
        common_elements.append(i)
print(common_elements)

#Question 9
lst=[1,2,3,4]
for i in lst:
    if i==1 or i==4:
        print(i)

#Question 10
box=input("Enter a string: ").lower()
vowels=['a','e','i','o','u']
result=""

for i in box:
    if i in vowels:
        result+=i
print(result)



#Question 11
word='Loops are Fun'.lower()
vowels=['a','e','i','o','u']
vow=""
cons=""

for i in word:
    if i in vowels:
        vow+=i
    elif i.isalpha():
        cons+=i 


print(len(vow))
print(len(cons)) #There are only 6 consonants in the string so the output could not give 7

#Question 12
list=[1,2,3,4,5]
odd=[]
even=[]

for i in list:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)

print(odd)
print(even)

#Question 13
number=int(input("Enter a number: "))
if number==0 or number==1:
    print("Not a prime number")

elif number>1:
    for i in range(2,number):
            if number%i==0:
                print(f"{number} is not a prime number")
                break
    else:
        print(f"{number} is a prime number")
else:
    print("Invalid number")

#Question 14
list= [1,2,3,4,"a","b"] 
num_list=[]
str_list=[]

for i in list:
    if i==1 or i==2 or i==3 or i==4:
        num_list.append(i)
    elif i.isalpha():
        str_list.append(i)
    else:
        print("Not in list")

print(num_list)
print(str_list)

#Question 15
user_input=(input("Enter your word: "))
dig_list=[]
letter_list=[]

for i in user_input:
    if i.isdigit():
        dig_list.append(i)
    elif i.isalpha():
        letter_list.append(i)
    else:
        print("Not given in input")
  

print(f'The number of digit are {len(dig_list)}, {dig_list}')
print(f'The number of letters are {len(letter_list)}, {letter_list}')

#Question 16
username = input("Enter username: ")
password = input("Enter password: ")

valid = True
has_number = False

for i in username:
    if not i.isalnum():
        valid = False

if len(password) < 8:
    valid = False

for i in password:
    if i.isdigit():
        has_number = True

if valid and has_number:
    print("Valid username and password")
else:
    print("Invalid username or password")

#Question 17
num=int(input("Enter a number: "))
for i in range(num, num+1):
    if i%2==0:
        print("It is even")
    else:
        print("It is odd")

#Question 18
num=int(input("Enter a number: "))
factorial=1
if num<0:
    print("Factorial does not exist for negative")
elif num==0:
    print("The factorial is 1")
else:
    for i in range(1, num+1):
        factorial*=i

print(f'The factorial of this number is {factorial}')

#Question 19
list=[1,2,3,4,5,6,7,8]
for i in list:
    for j in range(1,11):
        print(f'{i} * {j} = {i*j}')
    print()

#Question 20
lst=[1,2,3,4] 
for i in lst:
    if i==1 or i==2:
        print(i)

#Question 21
total=0
for i in range(1,6):
    if i%2==0:
        pass
    else:
        total=total+i
print(f'The sum of odd numbers is {total}')

#Question 22
total=0
for i in range(1,6):
    if i%2==0:
        total+=i
    else:
        pass
print(f'The sum of even numbers is {total}')

#Question 23
user_input=(input("Enter a word: "))
count=0
for i in user_input:
    if i==" ":
        count+=1
print("space",count)

#Question 24
list=[1,2,3,4]
new_list=[]
for i in list:
    i=i**3
    new_list.append(i)
print(new_list)

#Question 25
a="programming"
for i in a[-1::-1]:
    print(i, end=" ")
print()

#Question 26
for i in range(50):
    if i==8:
        break
    else:
        print(i)

#Question 27
user_input=input("Enter a word: ")
for i in user_input:
    print(i) #See if this will go on one line

#Question 28
a=["ram","shyam",1,2] 
for i in a:
    if i=="ram" or i=="shyam":
        print(f'Hello!, {i}')

#Question 29
a=["ram","shyam",1,2]
b=[]
for i in a:
    b.append(f'Dr.{i}')
print(b)

#Question 30
a=int(input("Enter a range: "))
sq_list=[]
for i in range(1,a):
    sq_list.append(i**2)
print(sq_list)

#Question 31
lst1=[111, 32, -9, -45, -17, 9, 85, -10]
lst2=[]
for i in lst1:
    if i>0:
        lst2.append(i)
    else:
        pass

print(lst2)

#Question 32
list=[0,1,2,3,4,5,6]
empty=[]
for i in list:
    if i==3 or i==6:
        pass
    else:
        empty.append(i)
print(empty)

#Question 33
a = [1, "hello", 3.5, True]
b=[]
for i in a:
    b.append(type(i))
print(b)

#Question 34
for i in range(5):
    print(i)
else:
    print("Done")

#Question 35
num=7
for i in range(15,0,-1):
    a=i*num
    print(a)

#Question 36
bad_chars = [';', ':', '!', "*"]
stringy = "py;th* o:n ! ;py * t*h:o !n"
for i in stringy:
    if i in bad_chars or i== " ":
        pass
    else:
        print(i, end=" ")
print()

#Question 37
series=[55,78,123,43,67,80]
odd=0
even=0
for i in series:
    if i%2==0:
        even+=1
    else:
        odd+=1

print(f'Count of odd number is {odd}')
print(f'Count of even number is {even}')

#Question 38
total=0
num=int(input("Enter a number: "))
if num==3 or num==5:
    for i in range(3,99):
        i=num*i
        total=total+i
        # print(i)
    print(total)
else:
    print("Number is not valid")

#Question 39
odd_total=0
even_total=0
for i in range(1,100):
    if i%2==0:
        even_total=even_total+i
    else:
        odd_total=odd_total+i

print(f'The sum of all old numbers in the range is {odd_total}')
print(f'The sum of all even numbers in the range is {even_total}')

#Question 40
list1=[10,20,10,30,10,40,50]
count=0
for i in list1:
    if i==10:
        count+=1
print(f'The number 10 appears {count} times in the list')