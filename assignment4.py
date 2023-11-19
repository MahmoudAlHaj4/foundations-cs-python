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

def main():
    print()
    displayMenu()
    print()
main()