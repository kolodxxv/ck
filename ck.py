from selenium import webdriver
from selenium.webdriver.opera.options import Options
import time
import os
import sys


class ck():

    def input_form():
        # user interface
        acc = []
        email = input('Enter email: ')
        acc.append(email)
        password = input('Enter password: ')
        acc.append(password)
        ck.logon(acc[0], acc[1])

    def logon(acc, passw):
        # First Driver Settings
        options = Options()
        profile = 'C:/Users/user/Desktop/ck/bin/first/Opera Software/Opera Stable'
        options.add_argument('user-data-dir=' + profile)
        options.add_argument('private')
        options.add_argument("--kiosk-printing")
        options.add_argument("download.default_directory=C:/Users/{username}/Desktop/")
        #driver.minimize_window()
        global driver
        driver = webdriver.Opera(options=options)
        driver.get('https://www.creditkarma.com/auth/logon?originalFlow=true')
        time.sleep(2)
        for x in range(10):
            username = driver.find_element_by_xpath('//input[@type="email"]')
            username.click()
            username.send_keys(acc)
            password = driver.find_element_by_xpath('//input[@type="password"]')
            password.click()
            password.send_keys(passw)
            rememberme = driver.find_element_by_xpath('//label[@id="lbl-rememberEmail"]')
            rememberme.click()
            login = driver.find_element_by_xpath('//input[@id="Logon"]')
            time.sleep(1)
            login.click()
            time.sleep(1)
            current_url = driver.current_url
            oops = 'https://accounts.creditkarma.com/authorize' or 'https://www.creditkarma.com/auth/logon'
            nreg = 'https://www.creditkarma.com/registration/complete' or 'https://www.creditkarma.com/registration/complete/error'
            okay = 'https://www.creditkarma.com/dashboard' or 'https://accounts.creditkarma.com/dashboard'
            verif = 'https://accounts.creditkarma.com/checkpoint/phone-verification/verify-phone/code'
            if current_url == oops:
                print('Bad attempt, retrying')
                incorrect = driver.find_element_by_xpath('//*[@id="log-on-form-section"]/div')
                error_text = incorrect.text
                print(error_text)
                if error_text == 'The email or password you entered is incorrect. You can try again or get some help logging in.':
                    print(incorrect.text)
                    driver.quit()
                    sys.exit(1) 
                elif "You've entered the wrong email or password too many times. For your security, we've locked your account for" in error_text:
                    print(incorrect.text)
                    driver.quit()
                    break
                    sys.exit(1) 
                elif error_text == 'Oops, something went wrong while trying to perform your request. Try again later. We appreciate your feedback.':
                    continue
            elif current_url == okay:
                print("It's all good! We're in!")
                time.sleep(4)
                #print("Time's up, quitting")
                #driver.quit()
                ck.get_reports()
            elif current_url == nreg:
                print('Client has to complete registration procedure. Closing.')
                driver.quit()
                sys.exit(1)
            elif current_url == verif:
                print('Client has two-step verification enabled, please ask him to turn it off')
                driver.quit()
                sys.exit(1)   
        driver.quit()
        ck.logon2(acc, passw)

    def logon2(acc, passw):
        # Second Driver Settings
        options = Options()
        profile = 'C:/Users/user/Desktop/ck/bin/second/Opera Software/Opera Stable'
        options.add_argument('user-data-dir=' + profile)
        options.add_argument('private')
        options.add_argument("--kiosk-printing")
        options.add_argument("download.default_directory=C:/Users/{username}/Desktop/")
        #driver.minimize_window()
        global driver2
        driver2 = webdriver.Opera(options=options)
        driver2.get('https://www.creditkarma.com/auth/logon?originalFlow=true')
        time.sleep(2)
        for x in range(10):
            username = driver2.find_element_by_xpath('//input[@type="email"]')
            username.click()
            username.send_keys(acc)
            password = driver2.find_element_by_xpath('//input[@type="password"]')
            password.click()
            password.send_keys(passw)
            rememberme = driver2.find_element_by_xpath('//label[@id="lbl-rememberEmail"]')
            rememberme.click()
            login = driver2.find_element_by_xpath('//input[@id="Logon"]')
            time.sleep(1)
            login.click()
            time.sleep(1)
            current_url = driver2.current_url
            oops = 'https://accounts.creditkarma.com/authorize' or 'https://www.creditkarma.com/auth/logon'
            nreg = 'https://www.creditkarma.com/registration/complete' or 'https://www.creditkarma.com/registration/complete/error'
            okay = 'https://www.creditkarma.com/dashboard' or 'https://accounts.creditkarma.com/dashboard'
            verif = 'https://accounts.creditkarma.com/checkpoint/phone-verification/verify-phone/code'
            if current_url == oops:
                print('Bad attempt, retrying')
                incorrect = driver2.find_element_by_xpath('//*[@id="log-on-form-section"]/div')
                error_text = incorrect.text
                print(error_text)
                if error_text == 'The email or password you entered is incorrect. You can try again or get some help logging in.':
                    print(incorrect.text)
                    driver2.quit()
                    sys.exit(1) 
                elif "You've entered the wrong email or password too many times. For your security, we've locked your account for" in error_text:
                    print(incorrect.text)
                    driver2.quit()
                    sys.exit(1) 
                elif error_text == 'Oops, something went wrong while trying to perform your request. Try again later. We appreciate your feedback.':
                    continue
            elif current_url == okay:
                print("It's all good! We're in!")
                time.sleep(4)
                ck.get_reports()
            elif current_url == nreg:
                print('Client has to complete registration procedure. Closing.')
                driver2.quit()
                sys.exit(1)
            elif current_url == verif:
                print('Client has two-step verification enabled, please ask him to turn it off')
                driver2.quit()
                sys.exit(1) 
        driver2.quit()
        ck.logon(acc, passw)

    def get_reports():
        username = os.getlogin()
        drivers = driver or driver2
        time.sleep(3)
        drivers.get('https://www.creditkarma.com/credit-health/transunion/credit-report/print')
        time.sleep(3)
        drivers.execute_script("window.open('https://www.creditkarma.com/credit-health/equifax/credit-report/print');")
        time.sleep(180)
        drivers.quit()
        sys.exit(1)  

ck.input_form()
