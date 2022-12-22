import os
import time
import config

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

OPEN_TRANS = (By.ID, "view-document")
START_TRANS = (By.ID, "start-translate")
INPUT_FILE_TRANS = (By.XPATH, "//input[@type='file']")
SOURCE_LANG = (By.ID, "source-lang")
TARGET_LANG = (By.ID, "target-lang")
UPLOAD_FILE = (By.ID, "upload")
PROCEED_BUTTN = (By.XPATH, '//button[.="I understand, proceed"]')

VIEW_DOC = (By.XPATH, '//*[@id="MUIDataTableBodyRow-0"]/td[11]/div[2]/div/a[2]')
DOWNLOAD_MAIN_BTN = (By.XPATH, '//button[.="Download"]')
DOWNLOAD_AS_BTN = (By.XPATH, '//div[@id="menu-appbar"]//li[.="{0}"]')


def performTranslateDocument(driver, input_file, source_inp, target_inp):
    # go to TRANS page
    # wait for clicking
    wait = WebDriverWait(driver, 10)

    # click open translate document
    wait.until(EC.element_to_be_clickable(OPEN_TRANS))
    trans_ele = driver.find_element(*OPEN_TRANS)
    trans_ele.click()
    time.sleep(5)

    # click on start translate
    wait.until(EC.element_to_be_clickable(START_TRANS))
    start_trans_ele = driver.find_element(*START_TRANS)
    start_trans_ele.click()
    time.sleep(2)

    # Click input file
    wait.until(EC.presence_of_element_located(INPUT_FILE_TRANS))
    input_ele = driver.find_element(*INPUT_FILE_TRANS)
    input_file = r'{0}'.format(input_file)  # r is to skip those char
    input_ele.send_keys(input_file)
    time.sleep(2)

    # click source language
    wait.until(EC.element_to_be_clickable(SOURCE_LANG))
    source_lang_ele = driver.find_elements(*SOURCE_LANG)[0]
    source_lang_ele.click()
    driver.find_element(By.XPATH, "//li[@data-value='" + source_inp + "']").click()
    time.sleep(2)

    # click target language
    wait.until(EC.element_to_be_clickable(TARGET_LANG))
    source_lang_ele = driver.find_elements(*TARGET_LANG)[0]
    source_lang_ele.click()
    dri = driver.find_element(By.XPATH, "//li[@data-value='" + target_inp + "']")
    driver.execute_script("arguments[0].click()", dri)  # it will run in backend(used JS)
    time.sleep(2)

    # click upload
    wait.until(EC.element_to_be_clickable(UPLOAD_FILE))
    upload_ele = driver.find_element(*UPLOAD_FILE)
    upload_ele.click()
    time.sleep(2)

    # understood proceed button
    wait.until(EC.presence_of_element_located(PROCEED_BUTTN))
    driver.find_element(*PROCEED_BUTTN).click()
    time.sleep(2)

    # while True:
    #     time.sleep(15)
    #     wait.until(EC.presence_of_element_located(STATUS_VALUE))
    #     status = driver.find_element(*STATUS_VALUE).text.strip()
    #     if status == 'COMPLETED':
    #         break
    #     else:
    #         print('waiting for 15 seconds ... STATUS = {0}'.format(status))

    # to click on view document
    wait.until(EC.element_to_be_clickable(VIEW_DOC))
    driver.find_element(*VIEW_DOC).click()
    time.sleep(2)

    download_list = {'As TXT': 'zip', 'As DOCX': 'docx'}
    result_list = []
    for dtype in download_list.keys():
        # click main download button
        wait.until(EC.element_to_be_clickable(DOWNLOAD_MAIN_BTN))
        dri = driver.find_element(*DOWNLOAD_MAIN_BTN)
        driver.execute_script("arguments[0].click()", dri)
        time.sleep(2)

        # click as_download btn
        d_btn = list(DOWNLOAD_AS_BTN)
        d_btn[1] = d_btn[1].format(dtype)
        d_btn = tuple(d_btn)

        wait.until(EC.element_to_be_clickable(d_btn))
        # print(len(driver.find_elements(*d_btn)))
        driver.find_element(*d_btn).click()
        time.sleep(2)

        # check download code
        d_count = 0
        while True:
            if len(os.listdir(config.DOWNLOAD_DIR)) > 1 and os.listdir(config.DOWNLOAD_DIR)[0][-3:] == download_list[
                                                                                                           dtype][-3:]:
                print('sucessfully Downloaded -> {0}'.format(dtype))
                # remove first file in download_dir
                result_list.append(True)
                os.remove(os.path.join(config.DOWNLOAD_DIR, os.listdir(config.DOWNLOAD_DIR)[0]))
                break
            elif d_count > 15:
                print('failed to Download -> {0}'.format(dtype))
                result_list.append(False)
                break
            else:
                time.sleep(5)
                d_count += 1

    status = True
    if False in result_list:
        status = False

    return status
