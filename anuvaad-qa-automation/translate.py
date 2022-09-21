from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

INSTANT_TRANSLATE_ELE = (By.ID,'instant-translate')
LANGUAGE_ELE = (By.ID,'demo-simple-select-outlined')
INPUT_TXT_ELE = (By.ID,'standard-multiline-static')
SUBMIT_ELE = (By.XPATH,'//button[.="submit"]')
OUTPUT_ELE = (By.TAG_NAME,'h6')


def performtranslatesentence(driver,src_lang,tgt_lang,inp_file):

    wait = WebDriverWait(driver,10)
    long_wait = WebDriverWait(driver,25)

    # click translate tab
    wait.until(EC.element_to_be_clickable(INSTANT_TRANSLATE_ELE))
    driver.find_element(*INSTANT_TRANSLATE_ELE).click()
    time.sleep(2)

    # select source-lang
    wait.until(EC.element_to_be_clickable(LANGUAGE_ELE))
    driver.find_elements(*LANGUAGE_ELE)[0].click()
    time.sleep(2)
    driver.find_element(By.XPATH,'//li[@data-value="'+str(src_lang)+'"]').click()
    time.sleep(2)

    # select target-lang
    wait.until(EC.element_to_be_clickable(LANGUAGE_ELE))
    driver.find_elements(*LANGUAGE_ELE)[1].click()
    time.sleep(2)
    driver.find_element(By.XPATH,'//li[@data-value="'+str(tgt_lang)+'"]').click()
    time.sleep(2)

    # enter input text
    wait.until(EC.presence_of_element_located(INPUT_TXT_ELE))
    driver.find_element(*INPUT_TXT_ELE).send_keys(inp_file)
    time.sleep(2)

    # submit
    wait.until(EC.presence_of_element_located(SUBMIT_ELE))
    driver.find_element(*SUBMIT_ELE).click()
    time.sleep(2)

    # get output text
    try:
        long_wait.until(EC.presence_of_element_located(OUTPUT_ELE))
        output = driver.find_element(*OUTPUT_ELE).text.strip()
    except:
        output = 'no output'
    time.sleep(2)
    return output