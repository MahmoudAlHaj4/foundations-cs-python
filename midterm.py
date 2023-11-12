import requests
from bs4 import BeautifulSoup

class BrowserTabsSimulation: 
    def __init__(self):
        self.dict_for_tabs = {}

    def displayMenu(self):
        # function for display menu
        print("The Menu:\n", "\t1. Open Tab\n","\t2. Close Tab\n","\t3. Switch Tab\n","\t4. Display All Tabs\n","\t5. Open Nested Tab\n","\t6. Clear All Tabs\n","\t7. Save Tabs\n","\t8. Import Tabs\n","\t9. Exit\n")

    def openTab(self):
        # open tab function to create a tab
        # O(1) 
        for x in range(1):
            lst_content = {}
            for y in range(1):
                title = input("Enter the website title: ")
                url = input("Enter the website url:  ")
                lst_content['title'] = title
                lst_content['url'] = url
            id = "ID" + str(len(self.dict_for_tabs)+1)
            self.dict_for_tabs[id] = lst_content
            print(self.dict_for_tabs)

    def closeTab(self):
        index = input("Enter index of the tab you want to close: ").upper()
        if index in self.dict_for_tabs:
            del self.dict_for_tabs[index]
        elif index == "":
            last_id = "ID" + str(len(self.dict_for_tabs))
            del self.dict_for_tabs[last_id]
        else:
            print("Not Found")
    
    def displayAll(self):
        print("The tabs: ")
        print(self.dict_for_tabs)
    
    
    def switchTab(self):
        index = input("Enter the index you want to switch: ").upper()  
        if index in self.dict_for_tabs:
            page = requests.get(self.dict_for_tabs[index]['url']) # https://www.youtube.com/watch?v=taL3r_JpwBg # https://realpython.com/beautiful-soup-web-scraper-python/
            src = page.content
            soup = BeautifulSoup(src, 'html.parser')
            print(soup.prettify())
        
        else:
            print("Not Found")
    
    def openNestedTab(self):
        index = input("Enter the index where you want to insert additional tab:").upper()
        if index in self.dict_for_tabs:
            for x in range(1):
                for y in range(1):
                    nested_dict = {}
                    nested_title = input("Enter a tittle: ")
                    nested_url = input("Enter a url: ")
                    nested_dict['title'] = nested_title
                    nested_dict['url'] = nested_url
                    
                id = str(index) + "0"+ str(len(self.dict_for_tabs)+1)
                self.dict_for_tabs.setdefault(index, {}).setdefault("The Nested Tab" ,nested_dict) #1) https://stackoverflow.com/questions/3483520/use-cases-for-the-setdefault-dict-method  2)https://stackoverflow.com/questions/30881453/dict-setdefaultkey-append-get-rid-of-additional-list 3)https://codereview.stackexchange.com/questions/253195/nested-dictionary-creation-with-setdefault
                print(self.dict_for_tabs)
        else:
            print("Not found")
        
    def clearTabs(self):
        self.dict_for_tabs.clear()
        print(self.dict_for_tabs)
        

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
            browser.switchTab()
        elif choice  == 4:
            browser.displayAll()
        elif choice == 5:
            browser.openNestedTab()
        elif choice == 6:
            browser.clearTabs()
        elif choice == 7:
            print("Save Tabs")
        elif choice == 8:
            print("Import Tabs")
        elif choice != 9:
            print("Invalid Input Please try again")
    print("You left")
main()