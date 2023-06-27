# import required packages

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
from bs4 import BeautifulSoup

# Define the chromedriver service
s = Service('chromedriver.exe')

# instantiate the webdriver
driver = webdriver.Chrome(service=s)

# the base url for the pages to scrape
page_URL= "https://leetcode.com/problemset/all/?page="

# Function to get all the 'a' tags from a given URL

def get_a_tags(url):
    # load the URL in the browser
    driver.get(url)
    # wait for 7 seconds to ensure the page is fully loaded
    time.sleep(7)
    # find all the 'a' elements on the page
    links= driver.find_elements(By.TAG_NAME,"a")
    ans=[]
    pattern="/problems"
    
    # iterate over each 'a' element
    
    
    for i in links:
        try:
            # check if '/problems/' is in the href of the  'a' element
            if pattern in i.get_attribute("href"):
                # if it is, append it to the list of links
                ans.append(i.get_attribute("href"))
        except:
            pass   
    # Remove duplicate links using set
    ans = list(set(ans))
    return (ans)


# List to store the final list of links
my_ans =  []
# Loop through the pages you're interested in (in this case, page 1-28)
for i in range(1,55):
    # call the function to get the 'a' tags from each page and append the results to your list
    my_ans += (get_a_tags(page_URL+str(i)))
    

# remove any duplicates that might have been introduced in the process
my_ans = list(set(my_ans))
    
#open a file to write the results to
##with open('lc.txt','a') as f:
with open('X:\Web development hackatthon Algozenith\leetcode questions\lc.txt', 'a') as f:
    # Rest of the code

    # iterate over each link in your final list
    for j in my_ans:
        #write each link to the file, followed by a newline
        f.write(j+'\n')
            
# print the total no. of unique links found
print (len(my_ans))
    
#close the browser
driver.quit()
            
    
    
    
    
    
    
    