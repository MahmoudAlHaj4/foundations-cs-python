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

    def displayNodes(self):
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
    def pickChoice(self):
        choice = 0 
        while choice != "4":
            print("The menu:\n", "\t1. Add Node\n","\t2. Display Nodes\n","\t3. Search and Delete Node\n","\t4. Return to main menu")
            choice = (input("Pick: "))
            if choice == "1":
                value = int(input("Enter a value of node: "))
                new_node = Node(value)
                if self.head is None:
                    self.head = new_node
                else:
                    current = self.head
                    while current.next is not None:
                        current = current.next
                    current.next = new_node
            elif choice == "2":
                print()
                self.displayNodes()
                print()
            elif choice == "3":
                print("serach and dele")
            elif choice != "4":
                print("Invalid Input")
        print("You Left")
            
                        
        
    

def main():
    print()
    displayMenu()
    print()
main()