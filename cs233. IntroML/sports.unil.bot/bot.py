from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

op = webdriver.chrome.options.Options()
op.add_argument("--headless")
op.binary_location = "/usr/bin/google-chrome"
driver = webdriver.Chrome(options = op)

course_page = "https://sport.unil.ch/?pid=80&aid=23#content"
# course_page = "https://sport.unil.ch/?mid=90&aid=58"

login = "YOHANABE"
pwd = "didou100%"

driver.get('https://sport.unil.ch/?pid=29%27')
driver.find_element(By.TAG_NAME, "html").send_keys(Keys.ESCAPE)
time.sleep(1)
driver.find_element(By.NAME, "txtLogin").send_keys(login)
driver.find_element(By.NAME, "txtPassword").send_keys(pwd)
driver.find_element(By.NAME, "txtPassword").send_keys(Keys.ENTER)
driver.get(course_page)

inscriptions = driver.find_element(By.ID, "inscriptions")
items = inscriptions.find_elements(By.CLASS_NAME, "cours_items")

freeSlots = []

for item in items:
    for group in item.find_elements_by_class_name("group"):
        try:
            link = group.find_element_by_css_selector(".inscr .btn_insc")
            freeSlots.append({
                "hour": group.find_element_by_class_name("hour"),
                "link": link.get_attribute("href")
            })
        except NoSuchElementException:
            pass

for freeSlot in freeSlots:
    driver.get(freeSlot["link"])
    try:
        driver.find_element(By.CLASS_NAME, "btn_insc").click()
        time.sleep(0.5)
        driver.find_element(By.CSS_SELECTOR, 'button.shop_cours_info.add').click()
    except NoSuchElementException:
        pass
    driver.get(course_page)
