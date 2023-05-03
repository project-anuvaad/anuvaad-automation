from locust import HttpUser, TaskSet, task,constant,SequentialTaskSet
import json
import os
import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder


class MyReqRes(SequentialTaskSet):
   
        def __init__(self,parent):
            super().__init__(parent)
            self.auth=""
           
            


        @task(1) 
       
        def login(self):
            # admin login and retrieving it's access token
            response = self.client.post( "https://auth.anuvaad.org/anuvaad/user-mgmt/v1/users/login",name='login',
                                json={'userName': *********,
                                            'password': *********})
            output=json.loads(response._content)
            self.auth=output["data"]["token"]
         
        @task(2)
        def contentHandler(self):
            # admin login and retrieving it's access token
            headers={'auth-token':self.auth}
            response = self.client.get( "https://auth.anuvaad.org/anuvaad/content-handler/v0/fetch-content?record_id=A_FBTTR-YoRNN-1677028341268%7C0-16770441763235571.json&start_page=1&end_page=2",headers=headers,name='upload')

            # output=json.loads(response._content)
         

        @task(3)
        def upload(self):
            
            headers={'auth-token':self.auth}
           
            files = {'file': open('//home//apoorvabellary//39135.docx', 'rb')}
            #files = r"/home/apoorvabellary/39135.docx"
            print(files)
            print(type(files))
            
            response = self.client.post("https://auth.anuvaad.org/anuvaad-api/file-uploader/v0/upload-file",name='upload',files=files, headers=headers)
            print(response.text)
            
        @task(4)
        def WFDigitize(self):
            
            headers={'auth-token':self.auth}
            payload ={
    "workflowCode": "WF_A_FCBMTKTR",
    "jobName": "bkk.pdf",
    "jobDescription": "",
    "files": [
        {
            "path": "//home//apoorvabellary//39948.pdf",
            "type": "pdf",
            "locale": "en",
            "model": {
                "uuid": "8bdaff5c-24c2-4c92-a07b-39e05ae6c5a4",
                "is_primary": True,
                "model_id": 103,
                "model_name": "English-Hindi IndicTrans Model-1",
                "source_language_code": "en",
                "source_language_name": "English",
                "target_language_code": "hi",
                "target_language_name": "Hindi",
                "description": "AAI4B en-hi model-1(indictrans/fairseq)",
                "status": "ACTIVE",
                "connection_details": {
                    "kafka": {
                        "input_topic": "KAFKA_AAI4B_NMT_TRANSLATION_INPUT_TOPIC",
                        "output_topic": "KAFKA_AAI4B_NMT_TRANSLATION_OUTPUT_TOPIC"
                    },
                    "translation": {
                        "api_endpoint": "AAIB_NMT_TRANSLATE_ENDPOINT",
                        "host": "AAI4B_NMT_HOST"
                    },
                    "interactive": {
                        "api_endpoint": "AAIB_NMT_IT_ENDPOINT",
                        "host": "AAI4B_NMT_HOST"
                    }
                },
                "interactive_translation": True
            },
            "context": "JUDICIARY",
            "modifiedSentences": "a"
        }
    ]
}
        
            
            response = self.client.post("https://auth.anuvaad.org/anuvaad-etl/wf-manager/v1/workflow/async/initiate",name='digitize', headers=headers,data=payload)
            print(response)
                   


class MySeqTask(HttpUser):
    wait_time=constant(1)
    host="https://auth.anuvaad.org"
    tasks=[MyReqRes]



	
