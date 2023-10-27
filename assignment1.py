
# Question 1
expressions =[
  10*(90+2)-5,
  10*90+2-5,
  10*90+(2-5),
  10.0*(90+2)-5,
  120/(20+40)-(6-2)/4,
  5.0/2,
  5/2,
  5.0/2.0,
  5/2.0,
  678%3*(8-(9/4))
]

for x in expressions:
  print(x) # O(1)

# Question 2

id = eval(input("Enter your ID: "))
format_id = "[" + "0" + str(id).strip() + "]"
print("Your profile-ID: ", format_id)

name = str(input("Enter your name: "))
format_name = "[" +  name.strip().upper() + "]"
print("your profile-name: " + format_name) #o(1)


while True:
  date_of_birth = input("Enter your date of birth DD/MM/YY: ")
  if "/" in date_of_birth and len(date_of_birth ) >=8:
    print("Your date of birth is :"+ "[" + date_of_birth.strip() + "]")
    break
  else:
   print("invaild format please try again :") #O(1)
  

address = str(input("Enter your address: "))
format_address = "["  + address.strip().lower() + "]"
print("Your address is :" + format_address) #0(1)


# Question 3

number = eval(input("Enter a number : "))

if number:
  length = len(str(number))
  print(str(number) + " " + "has" + " " + str(length) + " " + "digits") #O(1)


# Question 4

numeric_grade = eval(input("Enter your Numeric grade : "))
letter_grade = ""
if numeric_grade>=97:
  letter_grade = "A+"
elif numeric_grade>=93 and numeric_grade <97:
  letter_grade = "A"
elif numeric_grade>=90 and numeric_grade <93:
  letter_grade = "A-"
elif numeric_grade>=87 and numeric_grade <90:
  letter_grade = "B+"
elif numeric_grade>=83 and numeric_grade <87:
  letter_grade = "B"
elif numeric_grade>=80 and numeric_grade <83:
  letter_grade = "B-"
elif numeric_grade>=77 and numeric_grade <80:
  letter_grade = "C+"
elif numeric_grade>=73 and numeric_grade <77:
  letter_grade = "C"
elif numeric_grade>=70 and numeric_grade <73:
  letter_grade = "C-"
elif numeric_grade>=67 and numeric_grade <70:
  letter_grade = "D+"
elif numeric_grade>=63 and numeric_grade <67:
  letter_grade = "D"
elif numeric_grade>=60 and numeric_grade <63:
  letter_grade = "D-"
elif numeric_grade <60:
  letter_grade = "F"
if letter_grade:
  print(str(numeric_grade)+ " " + "is equivalent to a " + letter_grade) #O(1)


# Question 5 

user_number = eval(input("Enter a number: "))

for x in range(1,user_number+1):
  print("*" * x)
for x in range(user_number -1 ,0,-1):
  print("*" * x) #O(N)

# Question 6

number1 = eval(input("Enter the first number: "))
number2 = eval(input("Enter the second: "))
  
while number2 <= number1:
  print("second number that is less than the first number please try again:")
  number2 =eval(input("Enter the second: "))
print("")
for x in range(number1 +1 ,number2):
  if x % 2 == 0:
   print(x) # O(N)