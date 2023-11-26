name = input("Enter your name: ").capitalize()
print("Welcome", name)

def displayMenu(): # function to display Menu for user
    print("The menu:\n","\t1. Singly Linked List\n","\t2. Check if Palindrome\n","\t3. Priority Queue\n","\t4. Evaluate an Infix Expression\n","\t5. Graph\n","\t6. Exit\n")

class Node: #Class Node 
    def __init__(self,info):
        self.head = None
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
                        
        
    

def main():
    ll = LinkedList()
    queue = Queue()
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
                    
            
    
    ll.displayNodes()
    print()
main()