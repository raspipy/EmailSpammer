from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as EC
import pandas as pd


def signup(driver: webdriver.Chrome, file, email):
    df = pd.read_csv(file, sep=';')
    for i,y in enumerate(df['Websites']):
        driver.get(y)
        for i in eval(df['Inputs'][i]):
            email_field = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, i)))

            email_field.send_keys(email)

        for i in eval(df['Submits'][i]):
            submit_button = driver.find_element(By.XPATH, i)
            submit_button.click()
        email_field.send_keys(email)




if __name__ == "__main__":
    driver = webdriver.Chrome()
    file = "newsletters.csv"
    email = input("Enter email: ")
    signup(driver, file, email)
    driver.quit()