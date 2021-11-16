import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException

class InscUser:

    def __init__(self, user):
        op = webdriver.chrome.options.Options()
        op.add_argument("--headless")
        op.binary_location = "/usr/bin/google-chrome"
        driver = webdriver.Chrome(options = op)

        #course_page = "https://sport.unil.ch/?pid=80&aid=23#content" # (basketball)
        course_page = "https://sport.unil.ch/?pid=80&aid=58#content" # (volley)

        #login = "hakimdao"
        #pwd = "Se2E3abUg"

        login = user["login"]
        pwd = user["pwd"]

        driver.get('https://sport.unil.ch/?pid=29')
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
            for group in item.find_elements(By.CLASS_NAME, "group"):
                #print(group.text)
                try:
                    link = group.find_element(By.CSS_SELECTOR, ".inscr .btn_insc")
                    freeSlots.append({
                        "heure": group.find_element(By.CLASS_NAME, "hour").text,
                        "dt": group.find_element(By.CLASS_NAME, "dt").text,
                        "link": link.get_attribute("href")
                    })
                except NoSuchElementException:
                    pass # this item is not free

        for freeSlot in freeSlots:
            def inscrire(date):
                return (freeSlot["heure"] == date["heure"] or date["heure"] == "") and (freeSlot["dt"] == date["dt"] or date["dt"] == "")
            if user["dates"] is None or True in [inscrire(date) for date in user["dates"]]:
                driver.get(freeSlot["link"])
                try:
                    if "mercredi" in user and user["mercredi"]:
                        driver.find_element(By.CSS_SELECTOR, '.btn_insc[data-type="2"]').click()
                        time.sleep(0.5)
                        driver.find_element(By.NAME, "groupe_nom").send_keys("Les Rhourbis")
                        driver.find_element(By.NAME, "confirm_valid").click()
                    else:
                        driver.find_element(By.CLASS_NAME, "btn_insc").click()
                        time.sleep(0.5)
                    driver.find_element(By.CSS_SELECTOR, 'button.shop_cours_info.add').click()
                    print(datetime.now().strftime("[%d/%m/%Y %H:%M:%S]") + login + " inscrit avec succès.")
                except NoSuchElementException:
                    pass
                except ElementNotInteractableException:
                    pass # dirty fix
                driver.get(course_page)

        driver.get("https://sport.unil.ch/cms_core/auth/logout")
