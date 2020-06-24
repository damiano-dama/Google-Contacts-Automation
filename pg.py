from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

def open_google_contact(executable_path):
    # get chrome driver
    driver = webdriver.Chrome(executable_path)
    # open whatsapp
    driver.get('https://contacts.google.com/')
    return driver

def login_google(driver,user,pwd):
    # define wait timeout
    timeout_sec = 10
    wait = WebDriverWait(driver,timeout_sec)
    # username
    userBox = wait.until(EC.element_to_be_clickable\
            ((By.CSS_SELECTOR,'input[aria-label="Email or phone"]')))
    time.sleep(0.5)
    userBox.click()
    userBox.send_keys(user)
    # avanti button
    AvantiButton = wait.until(EC.element_to_be_clickable\
            ((By.CSS_SELECTOR,'span[class="RveJvd snByac"]')))
    AvantiButton.click()
    # password
    pwdBox = wait.until(EC.element_to_be_clickable\
            ((By.CSS_SELECTOR,'input[aria-label="Enter your password"]')))
    time.sleep(0.5)
    pwdBox.click()
    pwdBox.send_keys(pwd)
    # avanti button
    AvantiButton = wait.until(EC.element_to_be_clickable\
            ((By.CSS_SELECTOR,'span[class="RveJvd snByac"]')))                                             
    AvantiButton.click()

def contact_lookup(driver,contact_number):
    # define wait timeout
    timeout_sec = 10
    wait = WebDriverWait(driver,timeout_sec)
    # contact lookup
    searchBox = wait.until(EC.element_to_be_clickable\
            ((By.CSS_SELECTOR,'input[aria-label="Search"]')))
    searchBox.click()
    searchBox.send_keys(Keys.CONTROL,"a")
    searchBox.send_keys(Keys.DELETE)
    searchBox.send_keys(contact_number)
    searchBox.send_keys(Keys.RETURN)
    time.sleep(0.5)
    ActionChains(driver).send_keys(Keys.TAB*16).perform() 
    time.sleep(0.5)
    elem = driver.switch_to.active_element
    return elem.text
 
def add_google_contact(driver,contact_name,contact_number):
    # define wait timeout
    timeout_sec = 10
    wait = WebDriverWait(driver,timeout_sec)
    # add new contact button
    createNewButt = wait.until(EC.element_to_be_clickable\
            ((By.CSS_SELECTOR,'div[class="tk3N6e-LgbsSe-ssJRIf VIpgJd-TzA9Ye-eEGnhe tk3N6e-LgbsSe"]')))
    createNewButt.click()
    # first name field
    time.sleep(0.5)
    nameBox = wait.until(EC.element_to_be_clickable\
            ((By.CSS_SELECTOR,'input[style="width: 135px;"]')))
    nameBox.click()
    nameBox.send_keys(contact_name)
    # phone field
    action = ActionChains(driver)
    action.send_keys(Keys.TAB * 7).send_keys(contact_number).send_keys(Keys.TAB).\
                              send_keys(Keys.RETURN).perform()
    time.sleep(2)

def close_google_contact(driver):
    driver.quit()








