name = str(input("Enter your name: "))
print("welcome", name)
# print welcome mssg

def displayMenu():
    print("The menu:\n","\t1.Add Matrices\n","\t2. Check Rotation\n","\t3. Invert Dictionary\n","\t4. Convert Matrix to Dictionary\n","\t5. Check Palindrome\n","\t6. Search for an Element & Merge Sort\n","\t7. Exit\n")


def addMatrices():
   num_row = int(input("Enter the number of row: ")) 
   num_col = int(input("Enter the number of col: "))
   # inputs to get the number of rows and cols for the Matrix

   
   matrix1 = []
   matrix2 = []

   
   for row in range(num_row): # creating a loop to add rows and cols for matrix 1 
       matrix1_row = [] # creating an empty [] to store row values in matrix 1
       for col in range(num_col):
           value = int(input("Enter row values of the first matrix: ")) # add values to matrix 1
           matrix1_row.append(value)
       matrix1.append(matrix1_row)


   for row in range(num_row): # creating a loop to add rows and cols for matrix 2 
       matrix2_row =[] # creating an empty [] to store row values in matrix 2
       for col in range(num_col):
           value = int(input("Enter row values of the second matrix: ")) # add values to matrix 2
           matrix2_row.append(value)
       matrix2.append(matrix2_row)
    
   result = []

   for row in range(num_row):
       sum_of_row = [] # creating a new list to save the sum value in it
       for col in range(num_col):
           sum_of_row.append(matrix1[row][col]+ matrix2[row][col])
       result.append(sum_of_row)

   for row in result:
       print(row)

addMatrices()

