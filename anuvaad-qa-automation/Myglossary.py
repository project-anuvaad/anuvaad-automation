from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.support import expected_conditions as EC

MY_GLOSSARY=(By.XPATH,'//*[@id="my-glossary"]')
CREATE_GLOSSARY=(By.XPATH,'//button[.="Create Glossary"]')
LANG_ELE=(By.ID,'demo-simple-select-outlined')
TXT_ELE=(By.ID,'outlined-name')
SUBMIT_ELE=(By.XPATH,'//button[.="Submit"]')

def performglossary(driver,src_lang,tgt_lang,inp_file):
    # wait for clicking
    wait = WebDriverWait(driver, 10)

    # my glossary
    # wait.until(EC.element_to_be_clickable(MY_GLOSSARY))
    # glossary_ele = driver.find_element(*MY_GLOSSARY)
    # glossary_ele.click()
    driver.get('https://developers.anuvaad.org/my-glossary')
    time.sleep(2)

    # # create glossary
    wait.until(EC.element_to_be_clickable(CREATE_GLOSSARY))
    glossary_create = driver.find_element(*CREATE_GLOSSARY)
    glossary_create.click()
    time.sleep(2)

    # select source language
    wait.until(EC.element_to_be_clickable(LANG_ELE))
    driver.find_elements(*LANG_ELE)[0].click()
    time.sleep(2)
    driver.find_element(By.XPATH,'//li[@data-value="'+src_lang+'"]').click()
    time.sleep(2)

    # select target language
    wait.until(EC.element_to_be_clickable(LANG_ELE))
    driver.find_elements(*LANG_ELE)[1].click()
    time.sleep(2)
    driver.find_element(By.XPATH,'//li[@data-value="'+tgt_lang+'"]').click()
    time.sleep(2)

    # enter source text
    wait.until(EC.presence_of_element_located(TXT_ELE))
    driver.find_elements(*TXT_ELE)[0].send_keys(inp_file)
    time.sleep(2)

    # enter target text
    wait.until(EC.presence_of_element_located(TXT_ELE))
    driver.find_elements(*TXT_ELE)[1].send_keys(inp_file)
    time.sleep(2)

    # submit
    wait.until(EC.presence_of_element_located(SUBMIT_ELE))
    driver.find_element(*SUBMIT_ELE).click()
    time.sleep(5)

    # verify url redirection
    if "my-glossary" in driver.current_url:
        return True
    else:
        return False


