#Question 1
numbers=[]
while True:
    num=int(input("Enter a number: "))
    if num in numbers:
        print("Repeated number found")
        break
    else:
        numbers.append(num)
        print(numbers)

#Question 2
num=int(input("Enter a positive integer: "))
factorial=1
while num>1:
    factorial=factorial*num
    num=num-1

print(f'factorial is {factorial}')

#Question 3
num=int(input("Enter a number: "))
i=0
total=0
while i <=num:
    total=total+i
    i=i+1
print(total)

#Question 4
lst=[1,3,40,10,22,67,89,10,54]
i=0
count=0
while i <len(lst):
    if lst[i]==10:
        count=count+1

    i=i+1

print(count)

#Question 5
tree="ne gation@"

vowels=['a','e','i','o','u']
special_char=['@','#','*','&']

vcount=0
ccount=0
i=0
while i <len(tree):
    if tree[i] in vowels:
        vcount=vcount+1
    elif tree[i] in special_char or tree[i]==' ':
        pass
    else:
        ccount=ccount+1

    i=i+1

print(vcount)
print(ccount)

#Question 6
given=1456
count=0
while given>0:
    count=count+1
    given=given//10
print(count)

#Question 7
n=6
while n!=1:
    print(n, end='')

    if n%2==0:
        n=n//2
    else:
        n=3*n+1
print(n)

#Question 8
i = 65

while i <= 90:
    print(chr(i), end=" ")
    i = i + 1

#Question 9
starting_int=int(input("Enter a number: "))
ending_int=int(input("Enter a number: "))
i=starting_int
while i>=starting_int and i<=ending_int:
    print(i)
    i=i+1

#Question 10
i=49
while i >= 1:
    if i%2!=0:
        print(i)
    i=i-1

#Question 11
i=1
while i<=100:
    if i%7==0:
        print(i)

    i=i+1

#Question 12
numbers=[]
total=0
while True:
    num=int(input("Enter a number: "))
    if num==0:
        break
    total=total+num

print(total)

#Question 13
while True:
    age=int(input("Enter your age: "))
    if age<0 or age>120:
        print("Invalid age")
    else:
        break

#Question 14
scores=[]
average=0
total=0
while True:
    score=int(input("Enter students score: "))
    if score==-1:
        break
    else:
        total=total+score
        scores.append(score)
        average=total/len(scores)

print(average)

#Question 15
i=0
while i<=3:
    pas=input("Enter your password: ")
    if pas=='secret123':
        print("Acces granted")
        break
    else:
        print("Try again")
        i=i+1

    if i==3:
        print("Access denied")

#Question 16 
enter=int(input("Enter a number: "))
reverse=0

while enter>0:
    digit=enter%10
    reverse=reverse*10+digit
    num=num//10

print(reverse)

#Question 17
n=int(input("Enter the number of number of terms: "))
a=0
b=1
count=0

while count<n:
    print(a,end=' ')
    c=a+b
    a=b
    b=c

    count=count+1

#Question 18
goal=input("Enter your word: ")

vowel="a,e,i,o,u"
new=""
i=0

while i <len(goal):
    if goal[i] not in vowel:
        new=new+goal[i]
    i=i+1
print(new)

#Question 19
text=input("Enter a string: ")
count=0
i=0
while i<=len(text)-1:
    if text[i]=='h' and text[i+1]=='i':
        count=count+1
    i=i+1

print(count)

#Question 20
numbers = [12, 25, 7, 30, 18, 40, 55, 9]
new_lst=[]
i=0
while i <len(numbers):
    if numbers[i]%5==0:
        new_lst.append(numbers[i])

    i=i+1
print(new_lst)

#Question 21
text=input("Enter a string: ")
new=""

i=0
while i<len(text):
    if text[i].islower():
        new=new+text[i].upper()
    elif text[i].isupper():
        new=new+text[i].lower()
    else:
        new=new+text[i]

    i=i+1

print(new)

#Question 22
i=1
while i<=2:
    j=1
    while j<=2:
        print(f'{i} and {j}', end='')
        j=j+1
    i=i+1
#Loop runs 2 times for each iteration of outer loop i

# Question 23
# j was initialized outside of the inner loop

#Question 24
#5 is the first ineteger whose squre is strictly grater tan 20
found=False
x=1
while not found:
    if x*x>20:
        found=True
    else:
        x=x+1
print(x)


# #Question 25
#-1 is not added and the final total is 11
total=0
user_input=0
while user_input!=-1:
    total=total+user_input
    user_input=int(input("Enter: "))
print(total)

# Question 26
# loop doesnt print because 10<5 doesnot work and the final value of x is still 10

# Question 27
# X evaluates to 0 when it reaches a non-zero integer

# Question 28
# When logic is updated this code turns into the fibonacci sequence

#Question 29
tet=input("Enter a string: ")
i=0
upcount=0
lowcount=0

while i<len(tet):
    if tet[i].isupper():
        upcount=upcount+1
    elif tet[i].islower():
        lowcount=lowcount+1
    else:
        tet[i]
    
    i=i+1
print(upcount)
print(lowcount)

#Question 30

num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
while True:
    choice=int(input("Choose 1,2,3,4: "))
    if choice==1:
        add=num1+num2
        print(add)
    elif choice==2:
        sub=num1-num2
        print(sub)
    elif choice==3:
        mul=num1*num2
        print(mul)
    elif choice==4:
        break
        

# Question 31

neg=0
pos=0

while True:
    entry=int(input("Enter a number: "))
    if entry==0:
        break
    elif entry<0:
        neg=neg+1
    elif entry>0:
        pos=pos+1

print(f'the number of negative input are {neg}')
print(f'the number of postive input are {pos}')

#Question 32
start=int(input("Enter a number: "))
end=int(input("Enter a number: "))
i=start
while i>=start and i<=end:
    if i<=1:
        print(i,"It is not a prime number")
    elif i>1:
        j=2
        
        while j<i:
            if i%j==0:
                print(i,"It is not a prime")
                break
            j=j+1
        else:
            print(i,"It is prime")
    i=i+1

# Question 33
num=[12, 40, 21, 31, 10, 7, 5]

i=0
while i<len(num):
    if num[i]<20:
        print(num[i])
    i=i+1 

#Question 34
numbers = [45, 60, 12, 75, 30, 55, 8, 90]
new=[]
i=0
while i<len(numbers):
    if numbers[i]>50:
        numbers[i]=0

    i=i+1
print(numbers)

#Question 35
numbers = [15, 25, 30, 45, 60, 12, 90, 7]
count=0
i=0
while i<len(numbers):
    if numbers[i]%3==0 or numbers[i]%5==0:
        count=count+1
    
    i=i+1
print(count)

#Question 36
numbers = [10, 15, 25, 30, 45]

i=0
while i <len(numbers)-1:
    if numbers[i]>numbers[i+1]:
        print("not sorted")
        break

    i=i+1
else:
    print("sorted")

# Question 37
i = 97

while i <= 122:
    print(chr(i), end=" ")
    i = i + 1

#Question 38
chapter=[45, 30, 50,40]

count=1
i=0
while i<len(chapter):
    print(f'Chapter {count} has {chapter[i]} pages')
    count=count+1
    i=i+1

# Question 39
num1=[1,2,3,4,5]
num2=[3,4,5,6,7]

i=0 
while i <len(num1):
    j=0

    while j<len(num2):
        if num1[i]==num2[j]:
            print(num1[i])
        j=j+1

    i=i+1

#Question 40
list=[2,4,6,7,8]

i=0

while i<len(list):
    j=1

    while j<=10:
        print(f'{list[i]}x{j}={list[i]*j}')
        j=j+1

    print()
    i=i+1

#Question 41
list=[2,3,6,8,8]
i=0
while i<len(list)-1:
    if list[i]==list[i+1]:
        print("Duplicate found")
    else:
        print("No duplicates found")

    i=i+1