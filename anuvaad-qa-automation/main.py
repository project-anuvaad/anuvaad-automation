import argparse
import sys
from config import CHROMEDRIVER_PATH,DOWNLOAD_DIR

from login import perform_login
from document_digitization import performDocumentDigitization
from driver_script import get_driver
from Myglossary import performglossary
from translate import performtranslatesentence
from translate_document import performTranslateDocument

# arg parser
arg_obj = argparse.ArgumentParser()
arg_obj.add_argument('-l', '--login', help="flag for login", action="store_true")
# arg_obj.add_argument('-v', '--version', help="flag for version",type=str,default="1.0")
arg_obj.add_argument('-d', '--digitization', help="flag for digitization", action="store_true")
arg_obj.add_argument('-src', '--source', help="flag for sourcelanguage",type=str,default="English")
arg_obj.add_argument('-tgt', '--target', help="flag for targetlanguage",type=str,default="Kannada")
arg_obj.add_argument('-i', '--input', help="flag for inputfile",type=str,default="")
arg_obj.add_argument('-td','--translate-document',help='flag for transdoc',action="store_true")
arg_obj.add_argument('-ts','--translate-sentence',help='flag for transentence',action="store_true")
arg_obj.add_argument('-g','--glossary', help="flag for glossary", action="store_true")


args = arg_obj.parse_args()
login_flag = args.login
digi_flag=args.digitization
# version_inp=args.version
source_inp=args.source
target_inp=args.target
input_file=args.input
t_doc_flag=args.translate_document
t_snt_flag=args.translate_sentence
glossary_flag=args.glossary

# load driver object
driver=get_driver(CHROMEDRIVER_PATH,DOWNLOAD_DIR)

# code for login
login_status = perform_login(driver)
if login_status:
    print('login: success')
else:
    print('login: failed')
    login_flag=True

if login_flag:
    driver.close()
    driver.quit()
    sys.exit(0)
elif digi_flag:
    status = performDocumentDigitization(driver,input_file,source_inp)
    print(input_file, '->', status)
elif t_doc_flag:
    status= performTranslateDocument(driver, input_file,source_inp,target_inp)
    if status:
        print(f"translation of document={input_file} is successful")
    else:
        print(f"translation of document={input_file} is un-successful")
elif t_snt_flag:
    status= performtranslatesentence(driver,source_inp,target_inp,input_file)
    print(status)
elif glossary_flag:
    status= performglossary(driver,source_inp,target_inp,input_file)
    if status:
        print(f"glossary creation is successful")
    else:
        print(f"glossary creation is un-successful")
else:
    print('no argument/flag provided')

driver.close()
driver.quit()
sys.exit(0)
