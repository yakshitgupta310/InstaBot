from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class InstragramBot:

    def __init__(self, username, password):
        self.PATH = "D:\STUDY\PYTHON\SELENIUM\chromedriver.exe"
        self.driver = webdriver.Chrome(self.PATH)
        self.username = username
        self.password = password

    def SignIn(self):
        self.driver.get("https://www.instagram.com")
        user_name = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "username")))
        user_name.send_keys(self.username)
        pass_word = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "password")))
        pass_word.send_keys(self.password)
        login = self.driver.find_element_by_css_selector("button[type = submit]")
        login.click()
        not_now = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Not Now')]")))
        not_now.click()
        not_now2 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Not Now')]")))
        not_now2.click()
        time.sleep(5)

    def UnFollow(self, username):
        self.driver.get("https://www.instagram.com/" + username + "/")
        try:
            unfollow = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[@class = '_5f5mN    -fzfL     _6VtSN     yZn4P   ']")))
            unfollow.click()
            sure = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Unfollow')]")))
            sure.click()
            print("You unfollowed the user.")
            time.sleep(5)
        except:
            print("You are not following this user.")

    def Follow(self, username):
        self.driver.get("https://www.instagram.com/" + username + "/")
        follow = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "button")))
        if follow.text == "Follow":
            follow.click()
            time.sleep(3)
        else:
            print("You are already following this user.")

    def closewindow(self):
        self.driver.quit()


insta = InstragramBot("yakshit_310", "billorani")
insta.SignIn()
# insta.Follow('therock')
insta.UnFollow('therock')
