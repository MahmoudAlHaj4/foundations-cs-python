# # Question 1

print("------------------")

def reversedString(s,i):
  lst =[]
  for _x in range(i):
      lst.append(s)
  return "".join(lst)[::-1]


str = "hello"
num = 3 
print(reversedString(str,num))
print("------------------") #O(N)

# # Question 2


def reArrangeStrings(s):
  upper_case = []
  lower_case = []

  for letter in s:
    if letter.isupper():
      upper_case.append(letter)
    else:
      lower_case.append(letter)
  result = "".join(upper_case) + "".join(lower_case)
  return result

new_string = "HelLLo WorLD"
print(reArrangeStrings(new_string))
print("------------------")#O(N)


# Question 3

def isReordering(s1, s2):

  if s1[::-1] == s2:
    return True
  
  return False    

print(isReordering("abcde","edcb"))
print("------------------")#O(1)

####### Another Way to solve it 
def checkReordering(s1, s2):

  if sorted(s1) == sorted(s2):
    return True
  
  return False    

print(checkReordering("abcde","edcba"))#O(NlgN)
print("------------------")

# # Question 4
def findTheLargest(l):
  largest_number = l[0]
  largest_number_index = 0
  for x in range(len(l)):
    if l[x] > largest_number:
      largest_number = l[x]
      largest_number_index = x
      
  print("The largest number in the list is: ",largest_number, "at index", largest_number_index)
lst = [1,5,7,11,5,8,10,6,1]
findTheLargest(lst)#O(N)


# # Question 5 

def getsum(n):
  if n == 0:
      return 0

  return n %10 + getsum(n//10) 

num = int(input("enter a number: "))
print("The total sum is:", getsum(num))#O(N)



# # Question  6


def fixString(s):

  if len(s) <= 1:
      return s

  if s[0] == s[1]:
      return (fixString(s[1:]) )

  return s[0] + fixString(s[1:])

string = "hellloooo wwwworrrrld"
print(fixString(string))#O(N)

# # Question 7

