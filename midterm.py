# add menu 
def displayMenu():
    print("The Menu:\n", "\t1. Open Tab\n","\t2. Close Tab\n","\t3. Switch Tab\n","\t4. Display All Tabs\n","\t5. Open Nested Tab\n","\t6. Clear All Tabs\n","\t7. Save Tabs\n","\t8. Import Tabs\n","\t9. Exit\n")

def openTab():
    dict_for_tabs = {}
    lst_for_tap = []
    num_of_tabs = int(input("Enter the number of tabs: "))
    for x in range(1,num_of_tabs+1):
        new_dict ={}
        for y in range(1):
            title = input("Enter the website title: ")
            url = input("Enter the website url:  ")
            new_dict = lst_for_tap.append(title)
            new_dict = num_of_tabs.append(url)
        id = "ID" + str(x)
        dict_for_tabs[id] = new_dict
        print(dict_for_tabs)
        

def main():
    displayMenu()

    choice = 0 
    while choice != 9:
        choice = int(input("Enter Your Choice: "))
        if choice == 1:
            return openTab()
        elif choice == 2:
            print("close Tab")
        elif choice  == 3:
            print("Switch Tab")
        elif choice  == 4:
            print("Display All Tabs")
        elif choice == 5:
            print("Open Nested Tab")
        elif choice == 6:
            print("Clear All Tabs")
        elif choice == 7:
            print("Save Tabs")
        elif choice == 8:
            print("Import Tabs")
        elif choice != 9:
            print("Invalid Input Please try again")
    print("You left")
main()