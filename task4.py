#Question 1
items=[3,5,7,9,11,13]
a=items.pop(4)
items.insert(2,a)
items.append(a)
print(items)

#Question2
first_set={23,42,65,57,78,83,29}
second_set={57,83,29,67,73,43,48}
a=first_set.intersection(second_set)
print(a)
if a :
    first_set.difference(second_set)
    print(f'common elements: {a}')
else:
    print("no")

#Question 3
first_set={27,43,34}
second_set={34,93,22,27,43,53,48}
a=first_set.issubset(second_set)
print(a)
if a:
    first_set.clear()
    print(first_set)
else:
    print("It is not subset")

#Question 4
month={'jan':47,'feb':52,'march':47,'april':44,'may':52,'june':53,'july':54,'aug':44,'sept':54}
a=list(set(month.values()))
print(a)

#Question 5
sample_list=[87,45,41,65,94,41,99,94]
temp=set(sample_list)
late=tuple(temp)
print(late)
print(min(late))
print(max(late))

#Question 6
club_A={"ram","hari","shyam"}
club_B={"ram","gita","hari"}
a=club_A.intersection(club_B)
b=club_A.isdisjoint(club_B)
print(b)
if a:
    print(a)
else:
    print("No overlapping members found between groups")

#Question 7
required_tasks={"Email","Report","Meeting"}
completed_tasks={"Email","Report"}
check=required_tasks.issubset(completed_tasks)
if check:
    print("Print all tasks done")
else:
    print("Some tasks pending")

#Question 8
email={"Ram":"ram23@gmail.com", "Hari":"hari25@yahoo.com", "shyam":"shyam65@icloud.com"}
name=input("Enter student name: ")
if name in email:
    print("Email address is", email[name])
else:
    print("Contact not found")

#Question 9
shopping_list={"Milk","Bread","Egg"}
bought={"Bread","Egg"}
unbought=shopping_list.difference(bought)
if unbought:
    print(unbought)
else:
    print("Shopping is complete")

#Question 10
class_list=["ram","sita","laxman"]
student=input("Enter student name: ")
if not student in class_list:
    class_list.append(student)
    print(class_list)
else:
    print("Already present")

#Question 11
votes=["Blue","Red","Blue","Green","Blue"]
blue=votes.count("Blue")
if blue>=3:
    print("Blue wins")
else:
    print("Blue did not win")

#Question 12
grades={"Ram":92,"Sita":88}
student_name=input("Enter student name: ")
if student_name in grades:
    print(student_name, "grade is",grades[student_name])
else:
    print("Grade is not available")

#Question 13
applicant={"name": "Priya", "skills": ["Java","SQL"], "experience_years": 1}
required_skills={"Python","Java"}
if ("Python" in applicant["skills"] or "Java" in applicant["skills"]) and applicant["experience_years"]>=2:
    print("Priya qualifies")
else:
    print("Priya does not qualify")

#Question 14
banned_items={"scissors","knife","ligter"}
weight=int(input("Enter baggage weight: "))
item=input("Enter items in your baggage: ").lower()

if weight<=7 and item not in banned_items:
    print("Bag allowed")
else:
    print("Bag not allowed")

#Question 15
sample_dict={
    "emp1":{'name':'Jhon','salary':7500},
    "emp2":{'name':'Emma','salary':8000},
    "emp3":{'name':'Shyam','salary':500},
}
sample_dict["emp3"]['salary']=8500
print(sample_dict)

#Question 16
Ram={"Pen","Notebook","Calculator"}
Laxman={"Pencil","Diary","Pen"}
common=Ram.intersection(Laxman)
if common:
    print(f'They have some common items {common}')
else:
    print("They picked completely different items")