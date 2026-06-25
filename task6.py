#Question 1
items=['sql','123','pythyon']
temp=filter(lambda x: x.isalpha(),items)
print(list(temp))

#Question 2
products=[{'id':1,'name':'laptop','category':'electronics','price':1200, 'instock':True}, {'id':2,'name':'smartphone','category':'electronics','price':800,'instock': False}]

temp=filter(lambda x: x['instock']==True,products)

for i in temp:
    print(i['name'])

#Question 3
def add(num1,num2):
    return num1+num2

def subtract(num1,num2):
    return num1-num2

def multiply(num1,num2):
    return num1*num2

def divide(num1,num2):
    return num1/num2

def calculator():
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    while True:
        user_choice=int(input("Choose 1,2,3 4: "))
        if user_choice==5:
            print("Exit")
            break

        num1=int(input("Enter first number: "))
        num2=int(input("Enter second number: "))

        if user_choice==1:
            a=add(num1,num2)
            print(a)
        elif user_choice==2:
            b=subtract(num1,num2)
            print(b)
        elif user_choice==3:
            c=multiply(num1,num2)
            print(c)
        elif user_choice==4:
            if num2==0:
                print("Cannot divide by zero")
            else:
                d=divide(num1,num2)
                print(d)
        else:
            print("Invalid choice")
        
calculator()

#Question 4
def remove_at_idx(lst,index):
    new_list=[]
    
    i=0
    while i<len(lst):
        if i!=index:
            new_list.append(i)
        i=i+1

    return new_list

print(remove_at_idx([1,2,3,4],2))

# Question 5
def square():
    new_list=[]
    for i in range(1,21):
        a=i**2
        new_list.append(a)
    print(new_list[:5])

square()

#Question 6
course = [ {'title': 'Ancient Civilizations', 'genre': 'history'}, {'title': 'Corporate Finance', 'genre': 'commerce'}, {'title':'Modern World History', 'genre': 'history'} ]

temp=filter(lambda x:x['genre']=='history',course)
for i in temp:
    print(i)

#Question 7
emails = ['ram.sharma@gmail.com', 'spam@hooya.com', 'virus@malware.net','shyam.kumar@workcorp.com']
blacklist = ('@hooya.com', '@malware.net')

mail=filter(lambda x: x.endswith(blacklist),emails)
print(list(mail))
          
#Question 8
price = [100, 50, 200, 75]
dis=0.8
cart=map(lambda x: x*dis,price)
print(list(cart))