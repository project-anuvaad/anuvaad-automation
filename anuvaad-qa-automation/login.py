from config import LOGIN_URL,ANUVAAD_USERNAME,ANUVAAD_PASSWORD
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# selector variables
LOGIN_USERNAME = (By.NAME,'email')
LOGIN_PASSWORD = (By.NAME,'password')
LOGIN_SUBMIT_BTN = (By.XPATH,'//button[.="Login"]')
LOGIN_CHECK = (By.ID,'view-document')

def perform_login(driver):
    # to get a link in browser
    driver.get(LOGIN_URL)
    wait = WebDriverWait(driver,10)

    # enter username
    wait.until(EC.presence_of_element_located(LOGIN_USERNAME))
    uname_ele = driver.find_element(*LOGIN_USERNAME)
    uname_ele.send_keys(ANUVAAD_USERNAME)
    time.sleep(3)

    # enter password
    wait.until(EC.presence_of_element_located(LOGIN_PASSWORD))
    uname_ele = driver.find_element(*LOGIN_PASSWORD)
    uname_ele.send_keys(ANUVAAD_PASSWORD)
    time.sleep(2)

    # submit login
    wait.until(EC.element_to_be_clickable(LOGIN_SUBMIT_BTN))
    uname_ele = driver.find_element(*LOGIN_SUBMIT_BTN)
    uname_ele.click()
    time.sleep(2)

    # check for login
    try:
        wait.until(EC.presence_of_element_located(LOGIN_CHECK))
        login_status = True
    except Exception as e:
        # print('error ->',traceback.format_exc())
        login_status = False

    return login_status


