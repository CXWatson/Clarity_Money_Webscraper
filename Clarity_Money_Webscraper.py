from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup as soup
import time
import os



chrome_options = Options()
chrome_options.add_argument("--user-data-dir=C:\\Users\\Charles\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 1")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--profile-directory=Profile 1")
driver = webdriver.Chrome(executable_path="chromedriver.exe", options = chrome_options)
email=os.getenv("CLARITY_MONEY_USER")
password=os.getenv("CLARITY_MONEY_PASS")
url = 'https://app.claritymoney.com'
dash_url= 'https://app.claritymoney.com/dashboard'
driver.get(url)
driver.find_element_by_name('email').send_keys(email)
driver.find_element_by_name('password').send_keys(password)
driver.find_element_by_class_name('btn-deepblue.mb-1.btn.btn-full').click()
WebDriverWait(driver,200).until(EC.url_to_be(dash_url))
driver.find_element_by_class_name('transactions-header-title').click()
#WebDriverWait(driver,200).until(EC.element_to_be_clickable(('className', 'btn.btn-primary')))
time.sleep(1)
#driver.execute_script("window.scrollTo(0, 10000)")
time.sleep(1)
#Clicks the show more button
driver.find_element_by_css_selector('#modal-transactions > div.ta-c.p-1 > div').click()
time.sleep(1)
driver.find_element_by_css_selector('#modal-transactions > div.ta-c.p-1 > div').click()
time.sleep(1)
driver.find_element_by_css_selector('#modal-transactions > div.ta-c.p-1 > div').click()
time.sleep(1)
html_source = driver.page_source
#modal-undefined > div.ta-c.p-1 > div
#document.querySelector("#modal-undefined > div.ta-c.p-1 > div")
page_soup = soup(html_source, "html.parser")
transaction_container = page_soup.findAll("div", {"class":"transactions"})



# Gets the transactions by CSS Selector
transactions_soup = page_soup.select("#modal-transactions>div")

# Gets the transactions by CSS Selector
transactions_soup = page_soup.select("#modal-transactions>div")

# Prints the first group of transactions
transactions_soup[0]

# Filters out the HTML for the date of the transaction
transactions_soup[0].find("span",{"class":"date"}).text

# Filters out the transactions associated with the date
transactions_soup[0].find_all("div",{"class":"transaction-name"})

# Finds just the one transaction and filters out the HTML tags
transactions_soup[0].find("div",{"class":"transaction-name"}).find_all(text=True)

# Finds all the transaction prices
html_transaction_info = page_soup.findAll("div", {"class":"transaction-info"})

# Prints the first transactions and filters out the HTML tags
html_transaction_info[0].text

# Finding the date for a corresponding transaction
transactions_soup[0].find("div",{"class":"transaction-name"}).find_previous("span",{"class":"date"}).text

# Create an empty list to store data values
transactions_list=[]
# Loops through  transactions to find the transaction name, date, and information.
for transactions in transactions_soup[:-1]:
    current_date = transactions.find("div",{"class":"transaction-name"}).find_previous("span",{"class":"date"}).text
    transaction_date = transactions.find("span",{"class":"date"}).text
    transaction_name = transactions.find_all("div",{"class":"transaction-name"})
    transaction_info = transactions.find_all("div",{"class":"transaction-info f-jcv"})
    
    # Loop combines name, date, information into 1 list.
    for i in range(len(transaction_name)):
        transactions_list.append(current_date.replace(',',''))
        transactions_list.append(transaction_name[i].text.replace(',',""))
        transactions_list.append(transaction_info[i].text.replace(',',""))
        
        
# Check list
print(transactions_list[0:50])

# Sample to convert the string into a float
html_transaction_info = page_soup.findAll("div", {"class":"transaction-info"})
price = html_transaction_info[0].text
price.replace('$',"")

# Write the transactions out to a csv file
# test_string = transactions_list[0:7]
with open('transactions_may142020.csv', 'w') as csvfile:
    count = 0
    for i in transactions_list:
        if count < 3:
            csvfile.write(i)
            csvfile.write(',')
            count+=1
        else:
            csvfile.write('\n')
            csvfile.write(i)
            csvfile.write(',')
            count = 1
# Used to reference and view html gathered.
# print(page_soup)