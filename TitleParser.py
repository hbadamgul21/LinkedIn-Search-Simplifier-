from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException 
from selenium.webdriver.chrome.options import Options
from time import sleep
from tqdm import tqdm 
import bs4
import re
import tkinter as tk
from tkinter import ttk   


class LinkedInSearchSimplifier:
    def __init__(self,window, url, t, d, c):
        self.options = Options()
        self.options.headless = True
        self.options.add_argument("--log-level=3")
        self.driver = webdriver.Chrome(executable_path=r'chromedriver.exe', chrome_options=self.options)
        
        self.progress = ttk.Progressbar(window,orient ="horizontal",length = 200, mode='determinate')
        #self.url = "https://www.linkedin.com/jobs/search?keywords=Software%20Engineer&location=Katy%2C%20Texas%2C%20United%20States&trk=guest_job_search_jobs-search-bar_search-submit&redirect=false&position=1&pageNum=0&f_TP=1&f_E=2"
        #url = "https://www.linkedin.com/jobs/search?keywords=Software%20Engineer&location=Texas%2C%20United%20States&trk=guest_job_search_jobs-search-bar_search-submit&redirect=false&position=2&pageNum=0&f_TP=1&f_E=2&currentJobId=1477858929"
        self.url = url
        self.html = self.driver.page_source.encode('utf-8')
        self.driver.get(self.url)
        sleep(1)
        self.Get_All_The_Pages_Loaded()
        sleep(1.5)
        self.soup = bs4.BeautifulSoup(self.driver.page_source, 'html.parser')
        self.Get_All_The_Data(t, d, c)
        self.PrintEndNumResults()
        self.QuitDriver()
        

    #To make sure we gather all the data, we keep clicking the "load more" button.
    #Once we reach the end, we exit. We have the data to use with BeautifulSoup now.
    def Get_All_The_Pages_Loaded(self):
        page_num = 0
        while(1):
            window.update()
            try:
                self.driver.find_element_by_xpath("//*[text()='See more jobs']").click()
                page_num += 1
                page = tk.Label(window, text="Number of pages we are getting: " + str(page_num))
                page.grid(row = 6, column = 0)
                print("Page number: "+str(page_num))
                sleep(1)
            except NoSuchElementException:
                break
            
            
    #Grab the data we need, and perform certain actions to get the title, company name, and their descriptions. 
    #Then we manipulate the title, company name, and description to omit keywords and store the results in a .txt file.
    def Get_All_The_Data(self, t, d, c):
        global links 
        links = []
        global original 
        original = []
        for l in tqdm(self.soup.findAll(class_='result-card__full-card-link')):
            subURL = l['href']
            #print(subURL)
            self.driver.get(subURL)
            sleep(1)
            subSOUP = bs4.BeautifulSoup(self.driver.page_source, 'html.parser')
            #window.update()
            self.Bar()
            window.update()
            for items in subSOUP.findAll(class_='core-rail'):
                title = items.find(class_="topcard__title").get_text(strip=True)
                company = items.find(class_="topcard__flavor").get_text(strip=True)
                desc = items.find(class_="description__text description__text--rich").get_text(strip=True)
                #s1 = re.findall("Lead|Senior|Mid-Level|Sr.|Sr|SR|SR.|Angular|React|Contract", title)
                s1 = re.findall(t, title)
                #s2 = re.findall("1-2|7\+ years|2\+ years|4\+ years|5 years|8\+|5\+|5 plus|Sr.|Senior|Contract|12\+|12 months|2-4 years|3\+ years|\+ year's|2 years|contract|", desc)
                s2 = re.findall(d, desc)
                #s3 = re.findall("The Job Network|Revature|Kelly Services", company)
                s3 = re.findall(c, company)
                original.append(items.string)
                
                if(not(s1) and not(s2) and not(s3) and len(desc) > 600):
                    links.append(items.string)
                    with open("Results.txt", "a") as f:
                        print("_________________________________________________________________________________\n", file=f)
                        print(title, file=f)
                        print(company, file=f)
                    #print(desc)

    def Bar(self): 
        self.progress['value'] += 0.35
        if(len(original) == len(self.soup.findAll(class_='result-card__full-card-link'))-1):
            self.progress['value'] = 100
            w = tk.Label(window, text="Finished...you may close the window now.")
            w.grid(row = 6, column = 1)
        self.progress.grid(row = 5, column = 1)
    
    def PrintEndNumResults(self):         
        with open("Results.txt", "a") as f:
            print("_________________________________________________________________________________\n", file=f)
            print("Original number of results: "+ str(len(original)), file=f)
            print("The total results gathered with the given keywords are: " + (str)(len(links)), file=f)

    def QuitDriver(self):    
        sleep(0.5)
        self.driver.quit()

        

#GUI#
#This is where we perform GUI operations; however, I need to clean this up and make it into one class.         
window = tk.Tk()

window.geometry('1050x200')
window.title("LinkedIn Search Simplifier")

def Get_URL():
    id = my_entry.get()
    id2 = my_entry2.get()
    id3 = my_entry3.get()
    id4 = my_entry4.get()
    url = str(id)
    title = str(id2)
    desc = str(id3)
    company = str(id4)
    if url == "":
        window.destroy()
    my_button['state'] = "disabled"
    window.update()
    LinkedInSearchSimplifier(window, url, title, desc, company)

my_label = tk.Label(window, text = "Enter URL: ")
my_label.grid(row = 0, column = 0)
my_entry = tk.Entry(window)
my_entry.grid(row = 0, column = 1)

my_label2 = tk.Label(window, text = "Enter title keywords to remove from the results seperated by '|' or enter 'None', if no keywords are needed. Ex: Manager|Senior: ")
my_label2.grid(row = 1, column = 0)
my_entry2 = tk.Entry(window)
my_entry2.grid(row = 1, column = 1)

my_label3 = tk.Label(window, text = "Enter description keywords to remove from the results seperated by '|' or enter 'None', if no keywords are needed. Ex: 2\+ years|2-4: ")
my_label3.grid(row = 2, column = 0)
my_entry3 = tk.Entry(window)
my_entry3.grid(row = 2, column = 1)

my_label4 = tk.Label(window, text = "Enter a company that you want to exclude from the results seperated by '|' or enter 'None', if no keywords are needed. Ex: The Job Network|Revature: ")
my_label4.grid(row = 3, column = 0)
my_entry4 = tk.Entry(window)
my_entry4.grid(row = 3, column = 1)


my_button = tk.Button(window, text = "Submit", command = Get_URL)
my_button.grid(row = 4, column = 1)


window.mainloop()
        
        
# if __name__ == "__main__":
    # LinkedInSearchSimplifier()