import os
import time
import config

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

OPEN_DIGIT=(By.ID,"document-digitization")
START_DIGIT=(By.ID,"start-translate")
INPUT_FILE=(By.XPATH,"//input[@type='file']")
SOURCE_LANG=(By.ID,"source-lang")
UPLOAD_FILE=(By.ID,"upload")
STATUS_VALUE=(By.XPATH,"//*[@id='MUIDataTableBodyRow-0']/td[3]/div[2]")

VIEW_DOC = (By.XPATH,'//*[@id="MUIDataTableBodyRow-0"]/td[last()]//a[2]')
DOWNLOAD_MAIN_BTN = (By.XPATH,'//button[.="Download"]')
DOWNLOAD_AS_BTN = (By.XPATH,'//div[@id="menu-appbar"]//li[.="{0}"]')

def performDocumentDigitization(driver, input_file,language, version):
    # go to digi page
    # wait for clicking
    wait = WebDriverWait(driver, 10)

    # click open digitization
    wait.until(EC.element_to_be_clickable(OPEN_DIGIT))
    digit_ele = driver.find_element(*OPEN_DIGIT)
    digit_ele.click()
    time.sleep(2)

    # click start digitization
    wait.until(EC.element_to_be_clickable(START_DIGIT))
    startdigit_ele = driver.find_element(*START_DIGIT)
    startdigit_ele.click()
    time.sleep(2)

    # click input file
    wait.until(EC.presence_of_element_located(INPUT_FILE))
    input_ele = driver.find_element(*INPUT_FILE)
    input_file=r'{0}'.format(input_file)
    input_ele.send_keys(input_file)
    time.sleep(2)

    # click source language
    wait.until(EC.element_to_be_clickable(SOURCE_LANG))
    source_lang_ele = driver.find_elements(*SOURCE_LANG)[0]
    source_lang_ele.click()
    driver.find_element_by_id(language).click()
    time.sleep(2)

    # click version
    versiondict1 = {'1.0': 'WF_A_FCOD10GVOTK',
             '1.5': 'WF_A_FCWDLDBSOD15GVOTK',
             '2.0':'WF_A_FCWDLDBSOD20TESOTK'}

    wait.until(EC.element_to_be_clickable(SOURCE_LANG))
    version_ele = driver.find_elements(*SOURCE_LANG)[1]
    version_ele.click()
    driver.find_element_by_id(versiondict1[version]).click()
    time.sleep(5)

    # click upload
    wait.until(EC.presence_of_element_located(UPLOAD_FILE))
    upload_ele = driver.find_element(*UPLOAD_FILE)
    #driver.execute_script("arguments[0].click()",upload_ele)  #it will run in backend(used JS)
    ActionChains(driver).move_to_element(upload_ele).perform() #used actions here
    upload_ele.click()
    time.sleep(2)

    while True:
        time.sleep(15)
        wait.until(EC.presence_of_element_located(STATUS_VALUE))
        status = driver.find_element(*STATUS_VALUE).text.strip()
        if status == 'COMPLETED':
            break
        else:
            print('waiting for 15 seconds ... STATUS = {0}'.format(status))

    # to click on view document
    wait.until(EC.element_to_be_clickable(VIEW_DOC))
    driver.find_element(*VIEW_DOC).click()
    time.sleep(2)

    download_list = {'As TXT':'zip', 'As PDF':'zip', 'As DOCX':'docx'}
    result_list = []
    for dtype in download_list.keys():
        # click main download button
        wait.until(EC.element_to_be_clickable(DOWNLOAD_MAIN_BTN))
        driver.find_element(*DOWNLOAD_MAIN_BTN).click()
        time.sleep(2)

        # click as_download btn
        d_btn =list(DOWNLOAD_AS_BTN)
        d_btn[1] = d_btn[1].format(dtype)
        d_btn=tuple(d_btn)
        wait.until(EC.element_to_be_clickable(d_btn))
        driver.find_element(*d_btn).click()
        time.sleep(2)

        # check download code
        d_count = 0
        while True:
            if len(os.listdir(config.DOWNLOAD_DIR)) >1 and os.listdir(config.DOWNLOAD_DIR)[0][-3:]==download_list[dtype][-3:]:
                print('sucessfully Downloaded -> {0}'.format(dtype))
                # remove first file in download_dir
                result_list.append(True)
                os.remove(os.path.join(config.DOWNLOAD_DIR,os.listdir(config.DOWNLOAD_DIR)[0]))
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