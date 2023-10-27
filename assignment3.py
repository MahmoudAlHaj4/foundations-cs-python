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
       matrix1.append([])
       for col in range(num_col):
           value = input("Enter row values of the first matrix: ") # add values to matrix 1
           matrix1[row].append(value)


   for row in range(num_row): # creating a loop to add rows and cols for matrix 2 
       matrix2.append([])
       for col in range(num_col):
           value = input("Enter row values of the second matrix: ") # add values to matrix 2
           matrix2[row].append(value)
    
