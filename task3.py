#shopping
total_purchase_amount=int(input("Enter total purchase amount: "))
if total_purchase_amount>5000:
    membership=input("Are you a member? ").lower()
    if membership=="yes":
        card=input("Do you have a membership card? ")
        if card=="yes":
            discount_amount=total_purchase_amount*0.30
            final_price=total_purchase_amount-discount_amount
            print("Amount saved", discount_amount)
            print("Final price: ", final_price)
        else:
            print(total_purchase_amount)
else:
    print(total_purchase_amount)


#game
print("Welcome to the Magic Forest")
print("STAGE 1")
direction=input("Go NORTH or SOUTH? ").lower()
if direction=="south":
    print("STAGE 2")
    path=input("Cross the river or follow the path? ").lower()
    if path=="follow the path":
        print("STAGE 3")
        character=input("Choose FAIRY, OGRE or ELF? ").lower()
        if character=="elf":
            print("YOU WIN")
        else:
            print("GAME OVER")
    else:
        print("GAME OVER")
else:
    print("GAME OVER")

#Body mass index
weight=float(input("Enter your weight: "))
height=float(input("Enter your height in meters: "))
BMI=float(weight/height**2)

if BMI<18.5:
    print("Underweight")
elif BMI>=18.5 and BMI<25:
    print("Normal Weight")
elif BMI>=25 and BMI<=30:
    print("Overweight")
else:
    print("Obese")

print("Weight: ", weight)
print("Height: ", height)
print("BMI: ", BMI)

#Student portal
entered_username=input("Enter username: ")
entered_password=input("Enter password: ")
if entered_username=="admin":
      if entered_password=="ad123":
            print("Access Granted:Faculty Dashboard")
      else:
            print("Invalid login credentials, Please try again")
elif entered_username=="student":
    if entered_password=="st2026":
        print("Access Granted: Notes and Practice Questions")
    else:
        print("Invalid login credentials, Please try again")
else:
      print("Invalid login credentials, Please try again")

#Utility company
usage=int(input("Enter electricity usage in units: "))
if usage<100:
    cost=usage*5
    print("cost of unit is", cost)
elif usage>=100 and usage<=300:
    first_cost=100*5
    remaining=usage-100
    remaining_cost=remaining*8
    print(f'The cost of first 100 units is {first_cost} and cost of remaining units is {remaining_cost}')
elif usage>300:
    first_cost=100*5
    second_cost=200*8
    remaining=usage-300
    remaining_cost=remaining*10
    print(f'The cost of first 100 units is {first_cost}, the cost of next 200 units is {second_cost} and cost of remaining units is {remaining_cost}')
else:
    print("Invalid usage")

#positive
num=int(input("Enter a number: "))
if num>0:
    if num%2==0:
        print("The number is even")
    else:
        print("The number is odd")
else:
    print("Enter positive number")

#purchase
total_amount=int(input("Enter purchased amount: "))
if total_amount>1000:
    membership=input("Member: True or False: ").lower()
    if membership=="true":
        discount_amount=total_amount*0.20
        final_price=total_amount-discount_amount
        print(f"The final price is {final_price}")
    else:
        discount_amount=total_amount*0.10
        final_price=total_amount-discount_amount
        print(f"The final price is {final_price}")
else:
    print("No discount is given", total_amount)

#planet
weight=float(input("Enter your weight: "))
planet_number=int(input("Enter planet number: "))
if planet_number==1:
    destination_weight=weight*0.38
    print(f"Your weight on Mercury is {destination_weight}")
elif planet_number==2:
    destination_weight=weight*0.91
    print(f"Your weight on Venus is {destination_weight}")
elif planet_number==3:
    destination_weight=weight*0.38
    print(f"Your weight on Mars is {destination_weight}")
elif planet_number==4:
    destination_weight=weight*2.53
    print(f"Your weight on Jupiter is {destination_weight}")
elif planet_number==5:
    destination_weight=weight*1.07
    print(f"Your weight on Saturn is {destination_weight}")
elif planet_number==6:
    destination_weight=weight*0.89
    print(f"Your weight on Uranus is {destination_weight}")
elif planet_number==7:
    destination_weight=weight*1.14
    print(f"Your weight on Neptune is {destination_weight}")
else:
    print(f"Your weight on Earth is {weight}")


#results
math=int(input("Math: Enter your marks: "))
computer=int(input("Computer: Enter your marks: "))
social=int(input("Social: Enter your marks: "))
english=int(input("English: Enter your marks: "))
total_marks=math+computer+social+english
print(total_marks)
total_percentage=(total_marks/400)*100
print(total_percentage)
if math>70 and computer>70 and social>70 and english>70:
    print("Distinction")
elif math>60 and computer>60 and social>60 and english>60:
    print("First")
elif math>40 and computer>40 and social>40 and english>40:
    print("Passed")
else:
    print("Failed")

#lift
number=int(input("Enter floor number: "))
if number>=0 and number<=10:
    weight=int(input("Enter your weight: "))
    if not weight>500:
            door=input("Enter is door open or closed: ").lower()
            if door=="closed":
                 print("Elevator is activated")
            else:
                 print("Close door properly")
    else:
        print("Overweight, lift cannot move")
else:
    print("Invalid floor number")

#ATM
balance=5000
correct_pin=123
print("Welcome to the Global Bank Atm")
is_card_valid=True 
if is_card_valid:
    user_pin=int(input("Please enter your PIN: "))
    if user_pin==correct_pin:
        print("1. Check Balance")
        print("2. Withdraw Cash")
        print("3. Exit")
        choice= int(input("Select an option (1-3): "))
        if choice==1:
            print("Your current balance is Rs.5000")
        elif choice==2:
            amount=int(input("Enter the amount to withdraw: "))
            if amount<balance and amount>500:
                balance-=amount
                print(f"Please collect your cash: Rs. {amount}")
                print(f"Updated balance: Rs{balance}")
            else:
                print("Error: insufficient balance")
        elif choice==3:
            print("Thank you for visiting")
    else:
        print("Wrong Pin")
else:
    print("Invalid option")