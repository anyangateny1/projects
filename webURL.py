
def findWebsiteURL(bookName):

    # imports webdriver
    from selenium import webdriver

    # import Action Chains
    from selenium.webdriver.common.action_chains import ActionChains

    #import keys
    from selenium.webdriver.common.keys import Keys
    
    # creates webdriver Object

    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument("window-size=1920,1080")

    driver = webdriver.Chrome(options=options)

    #  recieves website

    driver.get("https://onecard.network/client/en_AU/playford/")

    # waits for page to load
    
    driver.implicitly_wait(5)

    # inputs bookName into the search box

    ActionChains(driver)\
        .send_keys(bookName, Keys.ENTER)\
        .perform()

    driver.implicitly_wait(5)

    url = driver.current_url

    return url

def restrictBook(url):

    # imports webdriver
    from selenium import webdriver
    
    # import By
    from selenium.webdriver.common. by import By

    # creates webdriver Object

    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument("window-size=1920,1080")

    driver = webdriver.Chrome()

    driver.get(url)

    restrictToBooks = driver.find_elements(By.LINK_TEXT, "Books")
    
    if restrictToBooks:

        restrictToBooks = driver.find_element(By.LINK_TEXT, "Books").click()
    
    else:

        return False
    
    # gets the location of the title of the book and attempts to match to the first pop up

    column1 = driver.find_element(By.ID, "results_cell0")

    bookTitle =  column1.find_element(By.CLASS_NAME, "displayDetailLink").text
    
    bookPicture = driver.find_elements(By.CLASS_NAME, "stupid_ie_div")
    
    if bookPicture:

        driver.find_element(By.CLASS_NAME, "stupid_ie_div").click()

    else:
        
        print ("Book title does not match any books in SA Libraries.")

        return

    driver.implicitly_wait(3)

    area = driver.find_element(By.ID, "tabs-1")

    location = area.find_element(By.CLASS_NAME, "asyncFieldLIBRARY").text

    if area.find_elements(By.CLASS_NAME, "availSummaryCheckedOut"):
        
        status = area.find_element(By.CLASS_NAME, "availSummaryCheckedOut").text.lower()

        driver.close()

        print(f"This book is", status, "\nIt will be located at", location) 
    
    else: 

        print("Book is currently on shelf at ", location)

        driver.close()

        
