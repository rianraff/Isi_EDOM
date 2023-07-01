from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def fill_EDOM(driver):
    # Wait for the table to load
    time.sleep(1)

    edom_value = "6"

    tr_tags_outer = driver.find_elements(By.TAG_NAME, "tr")

    # Loop through the <tr> tags and search for <a> tags
    for tr_outer in tr_tags_outer:
        # Find <a> tags within the current <tr> tag
        a_tags = tr_outer.find_elements(By.TAG_NAME, "a")

        # Loop through the <a> tags and print their text content
        for a in a_tags:
            a_text = a.text

            if a_text == "Isi EDOM":
                a.click()
                time.sleep(1)
                proceed_button = driver.find_element(By.ID, "proceed-button")
                proceed_button.click()

                input_tags = driver.find_elements(By.TAG_NAME, "input")
                for input_tag in input_tags:
                    value = input_tag.get_attribute("value")
                    if value == edom_value:
                        input_tag.click()

                    name = input_tag.get_attribute("name")
                    if name == "simpan":
                        submitButton = input_tag
                        submitButton.click()
                        time.sleep(2)

# Create a WebDriver instance
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://academic.ui.ac.id/main/Academic/HistoryByTerm")
main_page = driver.current_window_handle
time.sleep(1)

emailIN = driver.find_element(By.XPATH, '//*[@id="u"]')
passIN = driver.find_element(By.XPATH, '//*[@id="login"]/form/p[2]/input')
emailIN.send_keys('USERNAME')
passIN.send_keys('PASSWORD')
emailIN.send_keys(Keys.RETURN)
time.sleep(1)

akademikButton = driver.find_element(By.XPATH, '//*[@id="nv"]/li[3]/ul/li[1]/a')
driver.execute_script("arguments[0].click();", akademikButton)

ringkasanButton = driver.find_element(By.XPATH, '//*[@id="ti_m1"]/div[1]/ul/li[2]/a')
driver.execute_script("arguments[0].click();", ringkasanButton)

# Call the function to fill EDOM
while(1):
    fill_EDOM(driver)

# Quit the WebDriver
driver.quit()