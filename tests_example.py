import pytest
from pylenium.driver import Pylenium
from cred import*
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import allure



def test_login(py: Pylenium):

            py.visit(url)
            py.getx(input_text).type(user_name)
            py.getx(pwd_input).type(password)
            py.getx(submit_button).click()
            assert py.should().contain_title('ULCA')


def test_models(py:Pylenium):
            py.visit(url)
            py.getx(input_text).type(user_name)
            py.getx(pwd_input).type(password)
            py.getx(submit_button).click()
            assert py.should().contain_title('ULCA')
            py.getx(model).click()

def test_asr(py:Pylenium):
            py.visit(url)
            py.getx(input_text).type(user_name)
            py.getx(pwd_input).type(password)
            py.getx(submit_button).click()
            assert py.should().contain_title('ULCA')
            py.getx(model).click()
            py.wait(8)
            py.getx(src_lang).click()
            py.getx(src_lang).type('English')
            time.sleep(10)
            py.getx(src_lang).type(Keys.DOWN,Keys.ENTER)
            py.wait(6)
            py.getx(tgt_lang).type('Hindi')
            time.sleep(10)
            py.getx(tgt_lang).type(Keys.DOWN,Keys.ENTER)
            py.wait(7)
            py.getx(batch_inference).click()
            py.getx(batch_inference_input).type(wav)
            py.getx(convert).click()
            py.getx('//h5').is_enabled()
            

def test_corrected_asr(py:Pylenium):
            py.visit(url)
            py.getx(input_text).type(user_name)
            py.getx(pwd_input).type(password)
            py.getx(submit_button).click()
            assert py.should().contain_title('ULCA')
            py.getx(model).click()
            py.wait(8)
            py.getx(src_lang).click()
            py.getx(src_lang).type('English')
            time.sleep(10)
            py.getx(src_lang).type(Keys.DOWN,Keys.ENTER)
            py.wait(6)
            py.getx(tgt_lang).type('Hindi')
            time.sleep(10)
            py.getx(tgt_lang).type(Keys.DOWN,Keys.ENTER)
            py.wait(7)
            py.getx(batch_inference).click()
            py.getx(batch_inference_input).type(wav)
            py.getx(convert).click()
            py.getx('//h5').is_enabled()
            element=py.getx(copy_text)
            element.scroll_into_view()
            element.click()
            py.getx(corrected_asr).click()
            py.getx(corrected_asr).type(Keys.SPACE,'All')
            py.getx(submit).click()
           
def test_corrected_translation(py:Pylenium):
            py.visit(url)
            py.getx(input_text).type(user_name)
            py.getx(pwd_input).type(password)
            py.getx(submit_button).click()
            assert py.should().contain_title('ULCA')
            py.getx(model).click()
            py.wait(8)
            py.getx(src_lang).click()
            py.getx(src_lang).type('English')
            time.sleep(10)
            py.getx(src_lang).type(Keys.DOWN,Keys.ENTER)
            py.wait(6)
            py.getx(tgt_lang).type('Hindi')
            time.sleep(10)
            py.getx(tgt_lang).type(Keys.DOWN,Keys.ENTER)
            py.wait(7)
            py.getx(batch_inference).click()
            py.getx(batch_inference_input).type(wav)
            py.getx(convert).click()
            py.getx('//h5').is_enabled()
            element=py.getx(copy_text)
            element.scroll_into_view()
            element.click()
            py.getx(corrected_asr).click()
            py.getx(corrected_asr).type(Keys.SPACE,'All')
            py.getx(submit).click()
            py.getx(copy).click()
            py.getx(corrected_translation).click()
            py.getx(corrected_translation).type(Keys.SPACE,'अध्यक्ष')
            py.getx(submit1).click()




    

    
    
    
    
   
   
   

    
