from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
    browser.execute_script(
        "window.open('https://app.treasure.cloud/auth/signup?code=ODc4NTA3ZjEtNDRlMy0xMWVjLWI2ZjMtN2Q3Nzc1ZDA3ZWI2OmYwYTE0NjdhLTMyYzEtMTFlYi1iMWI4LTViYTQzMmY1ZjBkMA==');"
    )

    browser.switch_to.window(browser.window_handles[0])

    time.sleep(2)

    copyEmailButton = browser.find_element_by_css_selector(
        "body > div:nth-child(2) > div:nth-child(4) > div > a.blockLink.copy.cetc"
    )
    copyEmailButton.click()
    print("Email Copied!")

    browser.switch_to.window(browser.window_handles[1])
    print("Switching to Treasure Cloud!")

    time.sleep(2)

    coockclick = browser.find_element_by_css_selector(
        "body > div.cdk-overlay-container:nth-child(14) > div.cdk-global-overlay-wrapper:nth-child(2) > div#cdk-overlay-0.cdk-overlay-pane.mobile-fullscreen-dialog > mat-dialog-container#mat-dialog-0.mat-dialog-container.ng-tns-c164-5.ng-trigger.ng-trigger-dialogContainer.ng-star-inserted:nth-child(2) > app-manage-cookies.ng-star-inserted > div#cookies-action-buttons.mat-dialog-actions.manage-cookies-dialog-actions:nth-child(3) > button.mat-focus-indicator.primary-action.mat-raised-button.mat-button-base.mat-accent:nth-child(3)"
    )
    coockclick.click()
    print("Cookies Clicked")
    time.sleep(3)

    pasteEmailButton = browser.find_element_by_css_selector("#mat-input-0")
    pasteEmailButton.send_keys(Keys.CONTROL, "v")
    print("Email Pasted!")

    time.sleep(0.5)
    nameButton = browser.find_element_by_css_selector("#mat-input-1")
    nameButton.send_keys(names.get_full_name())

    pwo = PasswordGenerator()
    pwo.minlen = 10

    password = pwo.generate()

    passButton = browser.find_element_by_css_selector("#mat-input-2")
    passButton.send_keys(password)

    confirmPassButton = browser.find_element_by_css_selector("#mat-input-3")
    confirmPassButton.send_keys(password)
    print("Your passord=", password)
    print("Password and Name Filled")
    time.sleep(1)

    continueButton = browser.find_element_by_css_selector("#continue-button")
    continueButton.click()
    print("Signing Up")
    time.sleep(3)

    browser.switch_to.window(browser.window_handles[0])
    print("Switched to temp mail")
    time.sleep(1)

    print("Email Verification Process started")
    time.sleep(2)
    print("Waiting for the email")
    time.sleep(3)
    
    print(".................")

    time.sleep(1)
    print(".................")
    time.sleep(1)

    print(".................")
    time.sleep(1)
    print(".................")
    time.sleep(2)
    


    print("If there is no email and the process failed, try one more time please.")

    WebDriverWait(browser, 30).until(
    EC.text_to_be_present_in_element((By.XPATH, '//td[02]'), "Please verify your email address"))
    print("Email Foud")
    
    wpccBtn = browser.find_element_by_css_selector("a.wpcc-btn")
    wpccBtn.click()
    browser.refresh()
    time.sleep(1)
    print("Loading verification email")
    time.sleep(2)

    verifyEmail = browser.find_element_by_css_selector(
        "body > div.container:nth-child(2) > div.row.mailboxBlock.no-padding:nth-child(6) > div.row.tab-content > div#inbox.tab-pane.active.col-xs-12.no-side-padding.no-padding-bottom:nth-child(1) > table.table.table-hover.no-margin:nth-child(1) > tbody#schranka:nth-child(2) > tr.hidden-xs.hidden-sm.klikaciRadek:nth-child(1) > td:nth-child(2)"
    )
    verifyEmail.click()





    print("Verification Email loaded")
    time.sleep(2)

    browser.switch_to.frame("iframeMail")
    print("Switched to iFrame.")

    time.sleep(1)

    tester = browser.find_element_by_tag_name("a")
    tester.click()

    print("Verify Button Clicked")
    time.sleep(2)

    print("Process Completed")
    time.sleep(1)
    browser.switch_to.default_content()

    time.sleep(3)
    browser.switch_to.window(browser.window_handles[2])
    print("Tab switched to Tresure Cloud")

    time.sleep(3)

    wait = WebDriverWait(browser, 30)
    element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#mat-input-1")))

    print("Typing password")
    time.sleep(2)
    pasteloginpass = browser.find_element_by_css_selector("#mat-input-1")
    pasteloginpass.send_keys(password)

    clciksingin = browser.find_element_by_css_selector("#signin-button")
    clciksingin.click()

    print("Sign in clicked")
    time.sleep(2)
    print("Waiting untill user activation")

    wait = WebDriverWait(browser, 30)
    element = wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "#mat-checkbox-1 .mat-checkbox-inner-container")
        )
    )
    print("Page loaded and agreeing terms")
    termscheck = browser.find_element_by_css_selector(
        "#mat-checkbox-1 .mat-checkbox-inner-container"
    )
    termscheck.click()
    time.sleep(2)
    print("Terms Accepted")
    clickcontinue = browser.find_element_by_css_selector(
        "body > div.cdk-overlay-container:nth-child(17) > div.cdk-global-overlay-wrapper:nth-child(2) > div#cdk-overlay-1.cdk-overlay-pane.mobile-fullscreen-dialog > mat-dialog-container#mat-dialog-0.mat-dialog-container.ng-tns-c164-5.ng-trigger.ng-trigger-dialogContainer.ng-star-inserted:nth-child(2) > app-preferences-dialog.ng-star-inserted > div.mat-dialog-content.preferences-dialog-content > div.preferences-dialog-checkboxes:nth-child(3) > button.mat-focus-indicator.primary-action.mat-raised-button.mat-button-base.mat-accent:nth-child(4)"
    )
    clickcontinue.click()
    time.sleep(3)

    print("Referral Done")
    time.sleep(3)

    browser.quit()
