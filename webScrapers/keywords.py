from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://en.wikipedia.org/wiki/Special:Search?search=&go=Go"

wordChoices = input("Enter keywords as a comma separated list: ")
keywords = wordChoices.split(",")

options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("/Users/rylandhill/Desktop/py/userData")
driver = webdriver.Chrome(options=options)
driver.get(url)

element = driver.find_element(By.XPATH,'//*[@id="search"]/div[4]/div[1]/span/a')
element.click()

textBox = driver.find_element(By.ID,"ooui-35")
for item in keywords:
    textBox.send_keys(item)
    textBox.send_keys(",")

submitButton = driver.find_element(By.XPATH,'//*[@id="mw-search-top-table"]/div/div/div/span/span/button')
submitButton.click()

button500 = driver.find_element(By.XPATH,'//*[@id="mw-content-text"]/div[2]/div[7]/div/a[5]')
button500.click()

results = driver.find_elements(By.CLASS_NAME,"mw-search-result-heading")

def getNext5(index):
    temp = []
    for indexVal in range(index,index+5):
        temp.append(str(indexVal%5+1) +". "+results[indexVal].find_element(By.TAG_NAME,'a').get_attribute("title"))
    return temp

for index in range(0,500,5):
    currentFive = getNext5(index)
    print("")
    for item in currentFive:
        print(item)
    userQuestion = input("If you like any of these choices, type the number, if you would like 5 new ones type anything else: ")
    if (int(userQuestion)>0 and int(userQuestion)<6):
        newOptions = webdriver.ChromeOptions()
        newOptions.add_argument("/Users/rylandhill/Desktop/py/userData")
        openDriver = webdriver.Chrome(options=newOptions)
        openDriver.get(results[index+int(userQuestion)-1].find_element(By.TAG_NAME,'a').get_attribute("href"))
        while True:
            pass
while True:
    pass