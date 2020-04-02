from selenium import webdriver
from random import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


names = []
emails = []
PhoneNumber = []
address = []
startProgram = True

driver = webdriver.Firefox()
driver.get("https://es.fakenamegenerator.com/gen-random-us-us.php")

def main():
     f= open("users.txt","w+")
     for i in range(len(names)):
         f.write("Name: "+names[i]+'\n')
         f.write("Email: "+emails[i]+'\n')
         f.write(PhoneNumber[i]+'\n')
         f.write("Address: "+address[i]+'\n')
         f.write("======================="+'\n')
     f.close()


def generateFakePhoneNumber():
    areaCode = "786"
    randomNumbers = str(random())
    fakeNumber = "PhoneNumber: "+areaCode+"-"+randomNumbers[-3:]+"-"+randomNumbers[3:7]
    return fakeNumber


def saveUserInfo():
    userInfo = driver.find_element_by_tag_name('h3')
    names.append(userInfo.text)
    PhoneNumber.append(generateFakePhoneNumber())
    addressToSend = "1 1 4 69 North W... 34th ST"
    address.append(addressToSend)
    nameParse = str(userInfo.text).replace(" ", "")
    randomNumbers = str(random())
    endingGmail = "@gmail.com"
    email = nameParse.replace(".", "").lower() + randomNumbers[-3:] + endingGmail
    emails.append(email)
    main()
    wait = WebDriverWait(driver, 20)
    element = wait.until(EC.element_to_be_clickable((By.ID, 'genbtn')))
    element.click()

def invokeOperationXtimes(times):
    interationTimes = times
    adder = 0
    while adder < interationTimes:
        adder += 1
        saveUserInfo()
        print("records saved: "+str(adder))
        if adder == interationTimes:
            print("Finshed! Go check users.txt to see generated records")
            driver.quit()

if startProgram == True:
    invokeOperationXtimes(10)
