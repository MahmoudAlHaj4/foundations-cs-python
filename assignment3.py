


name = str(input("Enter your name: "))
print("welcome", name)
# print welcome mssg

def displayMenu():
    print("The menu:\n","\t1.Add Matrices\n","\t2. Check Rotation\n","\t3. Invert Dictionary\n","\t4. Convert Matrix to Dictionary\n","\t5. Check Palindrome\n","\t6. Search for an Element & Merge Sort\n","\t7. Exit\n")
    # printing the menu

def addMatrices(m1,m2):
   num_row = int(input("Enter the number of row: ")) 
   num_col = int(input("Enter the number of col: "))
   # inputs to get the number of rows and cols for the Matrix

   

   
   for row in range(num_row): # creating a loop to add rows and cols for matrix 1 
       matrix1_row = [] # creating an empty [] to store row values in matrix 1
       for col in range(num_col):
           value = int(input("Enter row values of the first matrix: ")) # add values to matrix 1
           matrix1_row.append(value) # The value will be saved in marix1_row
       m1.append(matrix1_row) 


   for row in range(num_row): # creating a loop to add rows and cols for matrix 2 
       matrix2_row =[] # creating an empty [] to store row values in matrix 2
       for col in range(num_col):
           value = int(input("Enter row values of the second matrix: ")) # add values to matrix 2
           matrix2_row.append(value) # The value will be saved in matri2_row
       m2.append(matrix2_row)
    
   result = [] # creating a empty list to print the last result 

   for row in range(num_row):
       sum_of_row = [] # creating a new list to save the sum value in it
       for col in range(num_col):
           sum_of_row.append(m1[row][col]+ m2[row][col])
       result.append(sum_of_row)

   for row in result:
       print(row)

matrix1 = []
matrix2 = []

def checkRotation(matrix1,matrix2):
  pass   


def invertDictionary():
    my_dict = {} 
    num_values = int(input("Enter the number of values: ")) 
    # creating an input to get the number of values in dict

    for x in range(num_values): # creating a loop to get from the user the key and the value 
        key = input("Enter your key: ")
        value = input("Enter a value: ")
        if value not in my_dict:
            my_dict[value] = key
            # if the value is not in dict the value,the value become the key and the key become the value
        else:
            my_dict[value].append(key)
            # the dict[value] will add the key

    print("Your dictionary is:")
    print(my_dict)


def convertMatrixToDictionary():
  final_dict = {} 
  num_emp = int(input("Enter the number of employees: "))
  # creating a dit to store the the final result 

  for row in range(1,num_emp+1): 
      result =[] 
      # creating a  nested loops to store the values to a matrix 
      for col in range(1):

          first_name = input("Enter your first name: ")
          last_name = input("Enter your last name: ")
          job_title = input("Enter your job title: ")
          company= input("Enter your company: ")
          result.append(first_name)
          result.append(last_name)
          result.append(job_title)
          result.append(company)
      id = "ID" + str(row) 
      # for creating a unique key I use str called ID and add to row by converting it to string
      final_dict[id] = result # the final dict will hold the unique keys

  print("your classroom is:",final_dict )

def checkPalindrome(s):
    if s == s[::-1]: 
        return True
        # the base case here is when the string is palindrome or reverse That's mean if string  = level and string[::-1] = level it will return true
    if s[0] == s[-1]:
        return checkPalindrome(s[1:-1])
        # If the first index of string  == the last index of string it will return the function it self and string[0],string[0] will be excluded
        # string[-1] will be at first and it's going to loop again to check
    return False # if the string is not palindrome will return false


def searchAndSort(lst, size):
  element = int(input("Enter the element to search for:")) # input for seraching
  new_lst = []

  while len(lst) > size: 
      parts = lst[:size] # taking elements from the beginning of the list at index size and put it in a new list called parts 
      new_lst.append(parts)
      lst = lst[size:] # this will update the new list 

  new_lst.append(lst)

  result = []
  for x in new_lst:
      result.extend(x) # search for it to add the parts and create a  1 list I

  sorted_lst = []

  while result: # using while loops for searching for the smaller number and sort it 
      small = result[0]
      for x in result:
          if x < small:
              small = x
      sorted_lst.append(small) # will add it to the sorted list
      result.remove(small) # remove the old small

  if element in sorted_lst: # for checking if the elemet is in the list or not
      index = sorted_lst.index(element)
      print(f"Element {element} is found at index {index} in the list.")
  else:
      print(f"Element {element} not found in the list.")

  print("Sorted list:", sorted_lst)

lsst = [2, 8, 3, 6, 5, 10, 7, 4, 9, 1]
size = 1


def main():
    displayMenu()
    choice = 0
    while choice !=7:
        choice = int(input("enter your choice: "))
        if choice == 1:
            addMatrices(matrix1,matrix2)
        elif choice == 2:
            checkRotation(matrix1,matrix2)
        elif choice == 3:
            invertDictionary()
        elif choice == 4:
            convertMatrixToDictionary()
        elif choice == 5:
        string = input("Enter a string: ")
            if checkPalindrome(string):
                print("The string is a palindrome.")
            else:
                print("The string is not a palindrome.")
        elif choice == 6:
            searchAndSort(lsst, size)
        elif choice != 7:
            print("Invalid Input")
    print("You left\n")
        
    

main()



