from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
usrname=input('Enter Your Username:')
password=input('Enter Your Password:')
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.facebook.com/')
print ("Opened facebook")
sleep(1)

username_box = driver.find_element_by_id('email')
username_box.send_keys(usrname)
print ("Your user name has been entered")
sleep(1)

password_box = driver.find_element_by_id('pass')
password_box.send_keys(password)
print ("you password has been entered")

login_box = driver.find_element_by_name('login')
login_box.click()
print ("Done")
input('You can type quit to exist')
driver.quit()
print("Finished")