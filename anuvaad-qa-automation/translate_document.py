import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

OPEN_TRANS=(By.ID,"view-document")
START_TRANS=(By.ID,"start-translate")
INPUT_FILE_TRANS=(By.XPATH,"//input[@type='file']")
SOURCE_LANG=(By.ID,"source-lang")
TARGET_LANG=(By.ID,"target-lang")
UPLOAD_FILE=(By.ID,"upload")
PROCEED_BUTTN=(By.ID,"")
VIEW_DOC=(By.ID)

def performTranslateDocument(driver,input_file,source_inp,target_inp):
    # go to TRANS page
    # wait for clicking
    wait = WebDriverWait(driver, 10)

    # click open translate document
    wait.until(EC.element_to_be_clickable(OPEN_TRANS))
    trans_ele = driver.find_element(*OPEN_TRANS)
    trans_ele.click()
    time.sleep(2)

    # click on start translate
    wait.until(EC.element_to_be_clickable(START_TRANS))
    start_trans_ele = driver.find_element(*START_TRANS)
    start_trans_ele.click()
    time.sleep(2)

    # Click input file
    wait.until(EC.presence_of_element_located(INPUT_FILE_TRANS))
    input_ele = driver.find_element(*INPUT_FILE_TRANS)
    input_file = r'{0}'.format(input_file) # r is to skip those char
    input_ele.send_keys(input_file)
    time.sleep(2)

    # click source language
    wait.until(EC.element_to_be_clickable(SOURCE_LANG))
    source_lang_ele = driver.find_elements(*SOURCE_LANG)[0]
    source_lang_ele.click()
    driver.find_element_by_xpath("//li[@data-value='"+source_inp+"']").click()
    time.sleep(2)

    # click target language
    wait.until(EC.element_to_be_clickable(TARGET_LANG))
    source_lang_ele = driver.find_elements(*TARGET_LANG)[0]
    source_lang_ele.click()
    dri=driver.find_element_by_xpath("//li[@data-value='" + target_inp+ "']")
    driver.execute_script("arguments[0].click()", dri)  # it will run in backend(used JS)
    time.sleep(2)

    # click upload
    wait.until(EC.element_to_be_clickable(UPLOAD_FILE))
    upload_ele = driver.find_element(*UPLOAD_FILE)
    upload_ele.click()
    time.sleep(2)

    # understood proceed button
    wait.until(EC.element_to_be_clickable(PROCEED_BUTTN))
    PROCEED_BUTTN.click()
    time.sleep(2)

    # to click on view document
    wait.until(EC.element_to_be_clickable(VIEW_DOC))
    driver.find_element(*VIEW_DOC).click()
    time.sleep(2)





