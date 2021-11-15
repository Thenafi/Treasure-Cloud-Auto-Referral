from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import names
from password_generator import PasswordGenerator
import itertools


# Create new Instance of Chrome

driver_path = "chromedriver.exe"
brave_path = "C:\Program Files\Google\Chrome\Application\chrome.exe"

option = webdriver.ChromeOptions()
option.binary_location = brave_path
option.add_argument("--incognito") 

for _ in itertools.repeat(None, 8):
    browser = webdriver.Chrome(executable_path=driver_path, chrome_options=option)

    # Temp Mail
    browser.get("https://www.minuteinbox.com")

    # Your Refereal Link
    browser.execute_script("window.open('https://app.treasure.cloud/auth/signup?code=ODc4NTA3ZjEtNDRlMy0xMWVjLWI2ZjMtN2Q3Nzc1ZDA3ZWI2OmYwYTE0NjdhLTMyYzEtMTFlYi1iMWI4LTViYTQzMmY1ZjBkMA==');")
    

    browser.switch_to.window(browser.window_handles[0])

    time.sleep(2) 

    copyEmailButton = browser.find_element_by_css_selector('body > div:nth-child(2) > div:nth-child(4) > div > a.blockLink.copy.cetc')
    copyEmailButton.click()
    print("Email Copied!")

    browser.switch_to.window(browser.window_handles[1])
    print("Switching to Treasure Cloud!")

    time.sleep(5) 

    coockclick= browser.find_element_by_css_selector("body > div.cdk-overlay-container:nth-child(14) > div.cdk-global-overlay-wrapper:nth-child(2) > div#cdk-overlay-0.cdk-overlay-pane.mobile-fullscreen-dialog > mat-dialog-container#mat-dialog-0.mat-dialog-container.ng-tns-c164-5.ng-trigger.ng-trigger-dialogContainer.ng-star-inserted:nth-child(2) > app-manage-cookies.ng-star-inserted > div#cookies-action-buttons.mat-dialog-actions.manage-cookies-dialog-actions:nth-child(3) > button.mat-focus-indicator.primary-action.mat-raised-button.mat-button-base.mat-accent:nth-child(3)")
    coockclick.click()
    time.sleep(3)
    print("donee")



    pasteEmailButton = browser.find_element_by_css_selector('#mat-input-0')
    pasteEmailButton.send_keys(Keys.CONTROL, 'v')
    print("Email Pasted!")

    time.sleep(0.5) 
    nameButton = browser.find_element_by_css_selector('#mat-input-1')
    nameButton.send_keys(names.get_full_name())

    pwo = PasswordGenerator()
    pwo.minlen = 10

    password = pwo.generate()

    passButton = browser.find_element_by_css_selector('#mat-input-2')
    passButton.send_keys(password)

    confirmPassButton = browser.find_element_by_css_selector('#mat-input-3')
    confirmPassButton.send_keys(password)
    print(password)

   
    continueButton = browser.find_element_by_css_selector('#continue-button')
    continueButton.click()
    print("singup clicked")
    time.sleep(3)

    browser.switch_to.window(browser.window_handles[0])

    print("switched")

    refreshButton = browser.find_element_by_css_selector('body > div:nth-child(2) > div:nth-child(4) > div > a.blockLink.refresh')
    refreshButton.click()
    time.sleep(10)
    print("Refresh Clicked!")
    time.sleep(5)

    refreshButton = browser.find_element_by_css_selector('body > div:nth-child(2) > div:nth-child(4) > div > a.blockLink.refresh')
    refreshButton.click()
    print("Refresh Clicked!2")
    time.sleep(3)

    wpccBtn =  browser.find_element_by_css_selector('a.wpcc-btn')
    wpccBtn.click()
    
    print("Viewing verification email")

    verifyEmail = browser.find_element_by_css_selector('tr > td.from')
    verifyEmail.click()

    print("loaded email")
    time.sleep(5) 

    


    browser.switch_to.frame('iframeMail')
    print("Switched to iFrame!")    

    time.sleep(2)

    print("going to click  the verify emal")
    verifyButton=browser.find_element_by_tag_name('td')
    verifyButton.click()
    print("Verify Button Clicking")
    time.sleep(3)
    print("waaiting")
    time.sleep(2)
    tester=browser.find_element_by_tag_name('a')
    tester.click()
    print("finally clicked")
    time.sleep(3)
    browser.switch_to.default_content()
    print("Switched Back")

    time.sleep(2)
    browser.switch_to.window(browser.window_handles[2])
    print("tab switched")

    time.sleep(2)

    print("typing password")
    time.sleep(2)
    pasteloginpass=browser.find_element_by_css_selector('#mat-input-1')
    pasteloginpass.send_keys(password)

    clciksingin=browser.find_element_by_css_selector('#signin-button')
    clciksingin.click()

    print("sign in cliked")
    time.sleep(3)

    print( "process completed")
    time.sleep(3)

    browser.quit()
    