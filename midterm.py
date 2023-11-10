class BrowserTabsSimulation:
    def __init__(self):
        self.dict_for_tabs = {}

    def displayMenu(self):
        print("The Menu:\n", "\t1. Open Tab\n","\t2. Close Tab\n","\t3. Switch Tab\n","\t4. Display All Tabs\n","\t5. Open Nested Tab\n","\t6. Clear All Tabs\n","\t7. Save Tabs\n","\t8. Import Tabs\n","\t9. Exit\n")

    def openTab(self):
        
        
        for x in range(1):
            lst_content =[]
            for y in range(1):
                title = input("Enter the website title: ")
                url = input("Enter the website url:  ")
                lst_content.append(title)
                lst_content.append(url)
            id = "ID" + str(len(self.dict_for_tabs)+1)
            self.dict_for_tabs[id] = lst_content
            print(self.dict_for_tabs)

    def closeTab(self):
        index = input("Enter index of the tab you want to close: ").upper()
        if index in self.dict_for_tabs:
            del self.dict_for_tabs[index]
        else:
            print("Not Found")
    
    def displayAll(self):
        print("The tabs: ")
        print(self.dict_for_tabs)
    
    
    def switchTab(self):
        index = input("Enter the index you want to switch: ").upper()  
        if index in self.dict_for_tabs:
            print()
        else:
            print("Not Found")

def main():
    browser = BrowserTabsSimulation()

    choice = 0 
    while choice != 9:
        browser.displayMenu()
        choice = int(input("Enter Your Choice: "))
        if choice == 1:
            browser.openTab()
        elif choice == 2:
            browser.closeTab()
        elif choice  == 3:
            print("Switch Tab")
        elif choice  == 4:
            browser.displayAll()
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