name = input("Enter your name: ").capitalize()
print("Welcome", name)

def displayMenu(): # function to display Menu for user
    print("The menu:\n","\t1. Singly Linked List\n","\t2. Check if Palindrome\n","\t3. Priority Queue\n","\t4. Evaluate an Infix Expression\n","\t5. Graph\n","\t6. Exit\n")

class Node: #Class Node 
    def __init__(self,info):
        self.info = info
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
    
    def getSize(self):
        current = self.head
        size = 0 
        while current != None:
            current = current.next
            size+=1
        return size
    
    def displayNodes(self):
        current = self.head
        while current :
            print(current.info,end=" ")
            current = current.next

    def delNode(self):
        del_node = int(input("Enter a node to del: "))

        if self.head != None and self.head.info == del_node:
            self.head = self.head.next
        
        current = self.head
        prev = None

        while current != None:
            if current.info == del_node:
                prev.next = current.next
                return
            prev = current
            current = current.next
        

    def pickChoice(self):
        choice = 0 
        while choice != "4":
            print("The menu:\n", "\t1. Add Node\n","\t2. Display Nodes\n","\t3. Search and Delete Node\n","\t4. Return to main menu")
            choice = (input("Pick: "))
            if choice == "1":
                value = int(input("Enter a value of node: "))
                new_node = Node(value)
                if self.head == None:
                    self.head = new_node
                else:
                    current = self.head
                    while current.next != None:
                        current = current.next
                    current.next = new_node
            elif choice == "2":
                print("\nThe Nodes : ", end=" ")
                self.displayNodes()
                print()
            elif choice == "3":
                self.delNode()
            elif choice != "4":
                print("Invalid Input")
        print("You Left")

class Queue:
  def __init__(self):
    self.lst_queue = []
    self.head = None
    self.tail = None
    self.size = 0   

  def enqueue(self, value):
        self.lst_queue.append(value)
        self.size += 1
        if self.size == 1:
            self.head = value
        self.tail = value 

  def dequeue(self):
        if self.size == 0:
            print("Empty")
            return None
        elif self.size == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.lst_queue[1]
        self.size -= 1
        return self.lst_queue.pop(0)    
        
  def CheckPalindrome(self, s):
        string = s.lower().replace(" ", "") 
        for char in s:  
            self.enqueue(char)
        
        index = len(string) - 1  
        while self.size > 1:  
            char = self.dequeue()  
            if char != string[index]:
                return False
            index -= 1

        return True         

class Student:
    def __init__(self,name,midterm_grade,final_grade, good_personality):
        self.name = name
        self.midterm_grade = midterm_grade
        self.final_grade = final_grade
        self.good_personality = good_personality

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class PriorityQueue:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def dispalyNodes(self):
        current= self.head
        while current!= None:
            print(current.data)
            current = current.next

    def enqueue(self,student):
        node = Node(student)

        if self.size == 0:
            self.head = node
            self.size +=1
        else:
            if node.data < self.head.data:
                node.next = self.head
                self.head = node
                self.size +=1
            else:
                current = self.head
                prev = current

                while current != None and current.data <=node.data:
                    prev =current
                    current = current.next
                prev.next = node
                node.next = current
                self.size +=1

    def dequeue(self):
        if self.size == 0:
            print("Your Queue is Empty Enqueue First")
        if self.size == 1:
            self.head = None
            self.size -=1
        else:
            print("we are removing ", self.head.data)
            current = self.head
            self.head = self.head.next
            current.next = None
            self.size-=1


    def addStudent(self):
        name = input("Enter  name:")
        midterm = int(input("Enter  midterm grade: "))
        final = int(input("Enter  final grade: "))
        good_personality = (input("enter true if the student has a good_pers: "))

        if good_personality == "true":
            good_personality ==True
        else:
            good_personality ==False
        
        student = Student(name, midterm, final, good_personality)

        self.enqueue(student)

    def interviewAStudent(self):
        if self.size == 0:
            print("No student to Interview")
            return

        current = self.head
        prev = None
        while current:
            if current.data.good_personality:
                break
            prev = current
            current = current.next


        if current:

            highest_final = current
            while current:
                if current.data.good_personality:
                    if current.data.final_grade > highest_final.data.final_grade:
                        highest_final = current
                    elif current.data.final_grade == highest_final.data.final_grade:
                        if current.data.midterm_grade > highest_final.data.midterm_grade:
                            highest_final = current
                current = current.next
            

            student = highest_final.data
            print("Interviewing:", student.name)

            if highest_final == self.head:
                self.head = self.head.next
            else:
                prev.next = highest_final.next
            self.size -= 1

            return student 
        else:
            print("No student with a good personality found")


    def displayMenu(self):
        choice = 0
        while choice != '3':
            print("\nThe menu:")
            print("1. Add a student")
            print("2. Interview a student")
            print("3. Back to main menu")

            choice = input("Enter your choice: ")
            if choice == '1':
                self.addStudent()
            elif choice == '2':
                self.interviewAStudent()
            elif choice != '3':
                print("Invalid input. Please try again.")

class Graph1:

    def __init__(self):
        self.num_vertices = 0
        self.adj_matrix = []
            
    

def main():
    ll = LinkedList()
    queue = Queue()
    PQ= PriorityQueue()
    print()
    displayMenu()
    choice = 0
    while choice !=6:
        choice = int(input("Enter your choice: "))
        if choice ==1:
            ll.pickChoice()
            displayMenu()
        elif choice == 2:
            user = input("Enter a string:")
    
            if queue.CheckPalindrome(user):
                print("The string is a palindrome!")
            else:
                print("The string is not a palindrome.")
        
        elif choice == 3:
            PQ.displayMenu()
            displayMenu()
            
    
    ll.displayNodes()
    print()
main()