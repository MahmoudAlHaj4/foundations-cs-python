import requests
from bs4 import BeautifulSoup
import json 
import os
class BrowserTabsSimulation: 
    def __init__(self):
        self.dict_for_tabs = {}

    def displayMenu(self):
        # function for display menu
        print("The Menu:\n", "\t1. Open Tab\n","\t2. Close Tab\n","\t3. Switch Tab\n","\t4. Display All Tabs\n","\t5. Open Nested Tab\n","\t6. Clear All Tabs\n","\t7. Save Tabs\n","\t8. Import Tabs\n","\t9. Exit\n")

    def openTab(self):
        # open tab function to create a tab
        # O(N)  N being the length of the dict
        for x in range(1):
            lst_content = {}
            for y in range(1): # function to create a tab
                title = input("Enter the website title: ")
                url = input("Enter the website url:  ")
                lst_content['title'] = title
                lst_content['url'] = url
            id = "ID" + str(len(self.dict_for_tabs)+1) # Id for the tab
            self.dict_for_tabs[id] = lst_content
            print(self.dict_for_tabs)
            

    def closeTab(self):
        # O(1) its a function that delete a fixed tab
        index = input("Enter index of the tab you want to close: ").upper()
        if index in self.dict_for_tabs:
            del self.dict_for_tabs[index]
        elif index == "":
            last_id = "ID" + str(len(self.dict_for_tabs)) # to get the last ID and delete it 
            del self.dict_for_tabs[last_id]
        else:
            print("Not Found")
    
    def displayAll(self):
        print("The tabs: ")
        for key,value in self.dict_for_tabs.items():
            print("The titles :", value['title'])
            if "The Nested Tab" in value:
                print("\t The nested Tab:", self.dict_for_tabs[key]["The Nested Tab"]['title']) #1) https://stackoverflow.com/questions/10399614/accessing-value-inside-nested-dictionaries 2)https://www.programiz.com/python-programming/nested-dictionary
    
    
    def switchTab(self):
        # O(N) N being the length of the nested tab
        index = input("Enter the index you want to switch: ").upper()  
        if index in self.dict_for_tabs:
            page = requests.get(self.dict_for_tabs[index]['url']) # https://www.youtube.com/watch?v=taL3r_JpwBg # https://realpython.com/beautiful-soup-web-scraper-python/
            src = page.content
            soup = BeautifulSoup(src, 'html.parser')
            print(soup.prettify())
        # to display the tab in HTML content 
            for key,value in self.dict_for_tabs.items():
                if "The Nested Tab" in value:
                    page2 = requests.get(self.dict_for_tabs[key]['The Nested Tab']['url'])
                    src2 = page2.content
                    soup2 = BeautifulSoup(src2,'html.parser')
                    print("The Nested is:\n",soup2.prettify())
        # to display the nested tab in HTML content
        
        else:
            print("Not Found")
    
    def openNestedTab(self):
        # O(N) N being the length of the nested tab
        index = input("Enter the index where you want to insert additional tab:").upper()
        if index in self.dict_for_tabs:
            for x in range(1):
                for y in range(1):
                    nested_dict = {}
                    nested_title = input("Enter a tittle: ")
                    nested_url = input("Enter a url: ")
                    nested_dict['title'] = nested_title
                    nested_dict['url'] = nested_url
                    

                self.dict_for_tabs.setdefault(index, {}).setdefault("The Nested Tab" ,nested_dict) #1) https://stackoverflow.com/questions/3483520/use-cases-for-the-setdefault-dict-method  2)https://stackoverflow.com/questions/30881453/dict-setdefaultkey-append-get-rid-of-additional-list 3)https://codereview.stackexchange.com/questions/253195/nested-dictionary-creation-with-setdefault
                print(self.dict_for_tabs)
                # This function is created for craeting nested dict and pass it to a tab
        else:
            print("Not found")
        
    def clearTabs(self):
        # O(1) we are cleaing a fix Tabs
        self.dict_for_tabs.clear() # research about it and find it clear all elemnt in the tab
        print(self.dict_for_tabs)
    
    def saveTab(self):
        # O(N)  N being the length of the N
        file = input("Enter the file path you want to save in it: ") # 1)https://www.youtube.com/watch?v=K48S3Sv1jwY 2)https://www.youtube.com/watch?v=WeetKVh31Eo 3)https://www.geeksforgeeks.org/reading-and-writing-json-to-a-file-in-python/amp/

        if os.path.exists(file): # .exists to check if the file path is valid or not
            with open(file,"w") as file:
                json.dump(self.dict_for_tabs,file)
                print("You saved the tab")
        else:
            print("Invalid path")
    
    def importTab(self):
        # O(N) N being the length of N of the dict
        
        file  = input("Enter the file you want to load: ")

        if os.path.exists(file):
            with open(file,"r") as file:
                self.dict_for_tabs = json.load(file) # 1)https://www.youtube.com/watch?v=FABwNhZA9pk 2)https://www.geeksforgeeks.org/reading-and-writing-json-to-a-file-in-python/amp/
                print("You Import a tab:")
        else:
            print("Invalid path")

        

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
            browser.saveTab()
        elif choice == 8:
            browser.importTab()
        elif choice != 9:
            print("Invalid Input Please try again")
    print("You left")
main()