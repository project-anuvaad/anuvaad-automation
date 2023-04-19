import scrapy
from scrapy.http import JsonRequest



class Anuvaad(scrapy.Spider):
    name="anuvaad"
    handle_httpstatus_list=[400,500,402,502]
    #start_urls=["https://users.anuvaad.org/"]


    def __init__(self):
        self.auth=""

    def start_requests(self):
        yield JsonRequest(url="https://auth.anuvaad.org/anuvaad/user-mgmt/v1/users/login",data={"userName":"****","password":"****"})


    def parse(self, response):
        if response.status!=200:
            raise Exception("login failed")
        # print("login successful")
        print(response.json())
        self.auth=response.json()["data"]["token"]
        yield {'api':'users/login','result':response.json()["http"]["status"]}

        yield JsonRequest(url="https://auth.anuvaad.org/anuvaad-etl/wf-manager/v1/workflow/jobs/search/bulk",data={"offset":0,"limit":0,"jobIDs":False,"taskDetails":True,"workflowCodes":["DP_WFLOW_FBT","WF_A_FCBMTKTR","DP_WFLOW_FBTTR","WF_A_FTTKTR"],"userIDs":[]},callback=self.read_bulk,
                          headers={"auth-token":self.auth} )
        

    def read_bulk(self,response):
        yield {'api':'search/bulk','result':response.json()["count"]}
        if response.status!=200:
            raise Exception("bulk failed")
        print("bulk successful")
        yield JsonRequest(url="https://auth.anuvaad.org/anuvaad/content-handler/v0/records/search",data={"record_ids":["A_FBTTR-qZsWM-1679385955828|0-1679386032789324.json","A_FTTTR-EWDrc-1678884436723|DOCX1-53148825-a354-4039-992e-92fba4e88f80.json","A_FBTTR-MKTbL-1678869814405|0-16788698815559764.json","A_FBTTR-nxEOp-1678856857863|0-16788572389104607.json","A_FBTTR-jGYXd-1678271902452|0-1678272039571193.json","A_FTTTR-YDnOC-1678201221361|DOCX1-513dd491-d6c0-4d84-8c53-88c752325151.json","A_FTTTR-FFHlW-1678200955173|DOCX1-97bd8a42-ea1c-4ccc-a1f2-2624436fa855.json","A_FTTTR-jpHsy-1678192590566|DOCX1-980f1535-1c93-4001-a731-a307e78fcdba.json","A_FBTTR-skNvt-1678182545548|0-16781827794183326.json"]},
                           headers={"auth-token":self.auth} ,callback=self.read_search)
       
    def read_search(self,response):
        yield {'api':'records/search','result':response.json()}
        if response.status!=200:
            raise Exception("search failed")
        print("search successful")
        request = JsonRequest(url="https://meity-auth.ulcacontrib.org/ulca/apis/v0/model/getTransliterationModelId?sourceLanguage=en&targetLanguage=hi",headers={"auth-token":self.auth} ,callback=self.read_transliteration)
    
    def read_transliteration(self,response):
         yield {'api':'records/search','result':response.json()}
         if response.status!=200:
            raise Exception("transliteration failed")
         print("transliteration successful")
         request= JsonRequest(url="https://auth.anuvaad.org/anuvaad/content-handler/v0/fetch-content?record_id=A_FBTTR-qZsWM-1679385955828%7C0-1679386032789324.json&start_page=1&end_page=2",headers={"auth-token":self.auth} ,callback=self.read_fetch)

    def read_fetch(self,response):
         if response.status!=200:
            raise Exception("fetch content failed")
         print("fetch content successful")
         yield JsonRequest(url="https://auth.anuvaad.org/anuvaad-etl/wf-manager/v1/workflow/sync/initiate",data={"workflowCode":"WF_S_TR","recordID":"A_FBTTR-qZsWM-1679385955828|0-1679386032789324.json","locale":"en","model":{"uuid":"687baea0-4512-4fb9-9264-5c7b368afc59","is_primary":True,"model_id":103,"model_name":"English-Hindi IndicTrans Model-1","source_language_code":"en","source_language_name":"English","target_language_code":"hi","target_language_name":"Hindi","description":"AAI4B en-hi model-1(indictrans/fairseq)","status":"ACTIVE","connection_details":{"kafka":{"input_topic":"KAFKA_AAI4B_NMT_TRANSLATION_INPUT_TOPIC","output_topic":"KAFKA_AAI4B_NMT_TRANSLATION_OUTPUT_TOPIC"},"translation":{"api_endpoint":"AAIB_NMT_TRANSLATE_ENDPOINT","host":"AAI4B_NMT_HOST"},"interactive":{"api_endpoint":"AAIB_NMT_IT_ENDPOINT","host":"AAI4B_NMT_HOST"}},"interactive_translation":True},"textBlocks":[{"attrib":"BOLD","avg_line_height":23,"block_id":"c8ba232bc6bf458bb4312f482988e235","block_identifier":"3670de91-6bb2-4e0d-bf6f-dd48aa71c521","children":[{"attrib":"BOLD","avg_line_height":23,"block_id":"c8ba232bc6bf458bb4312f482988e235","children":"null","font_color":"#000000","font_family":"DejaVuSans","font_size":19,"text":"REPORTABLE","text_height":23,"text_left":651,"text_top":31,"text_width":141,"parent_block_id":"c8ba232bc6bf458bb4312f482988e235","block_identifier":"3670de91-6bb2-4e0d-bf6f-dd48aa71c521","page_no":1,"sentence_id":"ee128480-ed9d-4ae0-98e4-3836ac0352bd"}],"font_color":"#000000","font_family":"DejaVuSans","font_size":19,"page_info":{"page_height":1263,"page_no":1,"page_width":892},"text":"REPORTABLE","text_height":23,"text_left":651,"text_top":31,"text_width":141,"tokenized_sentences":[{"batch_id":"0dffb1ac-837e-451a-b1ba-e1fc0628d9be","n_id":"A_FBTTR-qZsWM-1679385955828|0-1679386032789324.json|1|c8ba232bc6bf458bb4312f482988e235","s0_src":"REPORTABLE Page 2","s0_tgt":"रिपोर्ट योग्य पृष्ठ 2","s_id":"ee128480-ed9d-4ae0-98e4-3836ac0352bd","src":"REPORTABLE","tagged_src":"REPORTABLE Page 2","tagged_tgt":"रिपोर्ट योग्य पृष्ठ 2","tgt":"","tmx_phrases":[],"block_identifier":"3670de91-6bb2-4e0d-bf6f-dd48aa71c521","parent_block_id":"c8ba232bc6bf458bb4312f482988e235","page_no":1,"save":False},{"s_id":"66d4639b-569d-4a49-80de-bb294a4d5200","src":"Page 2","tgt":""}]}],"context":"JUDICIARY","modifiedSentences":["ee128480-ed9d-4ae0-98e4-3836ac0352bd","66d4639b-569d-4a49-80de-bb294a4d5200"],"retranslate":False},
                           headers={"auth-token":self.auth} ,callback=self.read_initiate)
         
    def read_initiate(self,response):
         if response.status!=200:
             print("merge and split failed")
         else:
            print("merge and split successful")
         yield JsonRequest(url="https://auth.anuvaad.org/anuvaad-etl/translator/v1/tmx/create",data={"userID":"bcc69d7cd7a34b08bffb15be0d66edd21606370034953","context":"JUDICIARY","sentences":[{"src":"CRIMINAL","tgt":"criminal","locale":"en|hi"}]},headers={"auth-token":self.auth},
                           callback=self.read_createGlossary)

    def read_createGlossary(self,response):
        if response.status!=200:
             print("glossary creation failed")
        else:
            print("glossary creation successful")
        yield JsonRequest(url="https://auth.anuvaad.org/anuvaad-etl/translator/v1/suggested-tmx/create",data={"orgID":"ANUVAAD","context":"JUDICIARY","translations":[{"src":"showing","tgt":"show","locale":"en|hi"}]},headers={"auth-token":self.auth},
                           callback=self.read_suggestGlossary)
        
    def read_suggestGlossary(self,response):
       if response.status!=200:
             print("Suggest glossary creation failed")
       else:
            print("Suggest glossary creation successful")
       yield JsonRequest(url="https://auth.anuvaad.org/anuvaad-etl/anuvaad-docx-downloader/v0/download-docx",data={"fname":"A_FBTTR-qZsWM-1679385955828|0-1679386032789324.docx","jobId":"A_FBTTR-qZsWM-1679385955828%7C0-1679386032789324.json","jobName":"41781","authToken":self.auth},callback=self.read_savecontent)

    def read_savecontent(self,response):
        if response.status!=200:
             print("docx download in translation failed")
        else:
            print("docx download in translation success")
        yield JsonRequest(url="https://auth.anuvaad.org/anuvaad/content-handler/v0/save-content-sentence",
                          data={"workflowCode":"DP_WFLOW_S_C","sentences":[{"batch_id":"0dffb1ac-837e-451a-b1ba-e1fc0628d9be","bleu_score":1,"n_id":"A_FBTTR-qZsWM-1679385955828|0-1679386032789324.json|1|979fa1ed8aa842f69ec4f53f3463b244","rating_score":"null","s0_src":"IN THE SUPREME COURT OF INDIA CRIMINAL APPELLATE JURISDICTION","s0_tgt":"भारत के सर्वोच्च न्यायालय में आपराधिक अपीलीय अधिकारिता","s_id":"0df857ee-b23f-4fce-a84a-cc7b65daaf22","save":True,"src":"IN THE SUPREME COURT OF INDIA CRIMINAL APPELLATE JURISDICTION","src_lang":"en","tagged_src":"IN THE SUPREME COURT OF INDIA CRIMINAL APPELLATE JURISDICTION","tagged_tgt":"भारत के उच्चतम न्यायालय में आपराधिक अपीलीय अधिकारिता","tgt":"भारत के सर्वोच्च न्यायालय में आपराधिक अपीलीय अधिकारिता","tgt_lang":"hi","time_spent_ms":10735,"tmx_phrases":[{"context":"JUDICIARY","hash":"8424a7e495c26bd10660d64b0934beaa91ce9418f4982e1389ead48f6298b807","locale":"en|hi","nmt_tgt":["भारत के उच्चतम न्यायालय में"],"orgID":"ANUVAAD","original":True,"src":"IN THE SUPREME COURT OF INDIA","timestamp":"1675743843","user_tgt":"भारत के सर्वोच्च न्यायालय में"},{"context":"JUDICIARY","hash":"8b3dfb10d0eb9bdec22939d5ecc1742af112a9d676b8c4c0731db1738652365f","locale":"en|hi","nmt_tgt":["न्यायालय","क्षेत्राधिकार","अपील"],"orgID":"ANUVAAD","src":"JURISDICTION","timestamp":"1675743842","user_tgt":"अधिकार क्षेत्र"}],"tmx_replacement":[{"src_color":"#1774e5","src_phrase":"IN THE SUPREME COURT OF INDIA","tgt":"भारत के उच्चतम न्यायालय में","tgt_color":"#1774e5","tmx_tgt":"भारत के सर्वोच्च न्यायालय में","type":"NMT"},{"src_color":"#8c5acd","src_phrase":"JURISDICTION","tgt":"न्यायालय","tgt_color":"#8c5acd","tmx_tgt":"अधिकार क्षेत्र","type":"NMT"}]}]},
                          headers={"auth-token":self.auth} ,callback= self.read_test)

    def read_test(self,response):
        if response.status!=200:
             print("sentence save failed")
        else:
            print("translated sentence saved successfully")

    
        
    
        

