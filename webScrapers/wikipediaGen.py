from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://wikiroulette.co/"

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument("/Users/rylandhill/Desktop/py/userData")
driver = webdriver.Chrome(options=options)
driver.get(url)

def openPage(url):
    openDriver = webdriver.Chrome()
    openDriver.get(url)
    while True:
        pass

def getNewURL(driver):
    driver.execute_script("navigate(1)")

def getPageURL(driver):
    element = driver.find_element(By.ID,'mainFrame')
    source = element.get_attribute('src')
    return source

def getPageName(url,options):
    tempDriver = webdriver.Chrome(options=options)
    tempDriver.get(url)
    pageName = tempDriver.title
    tempDriver.close()
    return pageName

def generate():
    getNewURL(driver)
    source = getPageURL(driver)
    print(getPageName(source,options))
    urlQ = input("Would you like the URL? (y/n) ")
    if (urlQ=="y"):
        print(getPageURL(driver))
    openQ = input("Would you like to open the page? (y/n) ")
    if (openQ == "y"):
        openPage(getPageURL(driver))
    newGen = input("Would you like a new page? (y/n) ")
    if (newGen=="y"):
        generate()
    else:
        print("Have a good day!")

def main():
    init = input("Would you like to generate a random Wikipedia Page? (y/n) ")
    if (init=="y"):
        generate()
    elif (init=="n"):
        print("Ok! Have a good day!")
        driver.close()
    else:
        print("Couldn't understand that, please try again.")
        main()
main()
