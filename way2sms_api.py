"""This module helps to send bulk sms for free using Way2sms.
   It uses selenium and chrome webdriver to interact with the website.
   You can run chrome in headless mode by setting options.headless = True.
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
OPTIONS = Options()
OPTIONS.headless = False
DRIVER = webdriver.Chrome(chrome_options=OPTIONS)
def login(username, password):
    """Functiion to login into the Way2sms website."""
    DRIVER.get("https://www.way2sms.com/")
    username_element = DRIVER.find_element_by_id("mobileNo")
    password_element = DRIVER.find_element_by_id("password")
    username_element.send_keys(username)
    password_element.send_keys(password)
    password_element.send_keys(Keys.ENTER)
def wait_to_load(wait_element):
    """Function to put webdriver on hold until the page is loaded and a certain element is found."""
    wait = WebDriverWait(DRIVER, 15)
    wait.until(EC.element_to_be_clickable((By.ID, wait_element)))
def send_sms(mobile_number, text_message):
    """Function to send text message to mobile number."""
    if len(text_message) > 140:
        print("Character Limit Exceeded.")
        return 0
    receiver_number = DRIVER.find_element_by_id("mobile")
    message = DRIVER.find_element_by_id("message")
    receiver_number.send_keys(mobile_number)
    message.send_keys(text_message)
    DRIVER.find_element_by_id("sendButton").click()
    if EC.alert_is_present():
        print("SUCCESS. Message Successfully Sent To %s"%mobile_number)
    else:
        print("Couldn't send the message to %s"%mobile_number)
    return 1
def send_bulksms(numbers, text_message):
    """Give numbers in a form of array of mobile numbers."""
    for i in numbers:
        send_sms(i, text_message)
login("your username goes here", "your password goes here")
wait_to_load("message") #keep this same to check if the message text box has been loaded.
send_sms("receivers number goes here", "body of text message goes here")
#Uncomment it if using headless mode to prevent chrome from running in background.
# DRIVER.quit()
