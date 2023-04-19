| Author   | Title |
| ---      | ---       |
| Hanumesh Kamatagi | `   Anuvaad-automation      |
| Apoorva Bellary | Anuvaad-Testing Stratergies |
| Apoorva Bellary | Anuvaad-API Automation |
| Hanumesh Kamatagi | `   Anuvaad-automation      |
| Apoorva Bellary | ulca-UI automation |
| Apoorva Bellary | Ulca-API Automation |

## Overview
The code in this repo could be utilized to automate procedures for  
translating/digitizing the documents Anuvaad website.

>IMPORTANT : This Script requires Chrome browser and its Respective Driver [Supported Browsers - Chrome].
> 
> ##Tests
> 
* Login : Test User login to Anuvaad.
* Translate sentence : Test User translate sentence to Anuvaad.
* Translate document : Test user translate document to Anuvaad.
* Digitize document : Test user digitize document to anuvaad.
* My glossary : Test user to glossary to Anuvaad.

Note : All examples/usage are given below.

## Usage

* ### For Login
*     python main.py -l

   Arguments: 
          *-l    (--login) : flag for login credentials.

* ### for translate sentence
*     python main.py -ts -src "en" -tgt "kn" --input "namaskara"
   
    Arguments:
          * -ts   (--translate sentence) : flag for translate sentence.

* ### for translate document
*     Python main.py -src "en" -i "c:\json\input\input\1.pdf.pdf" -tgt "kn" -td

    Arguments:
          * -td (--translate document) : flag for translate document.

* ### for Digitize document 
*      Python main.py -d -src "English" -i "c:\json\input\input\1.pdf.pdf"

    Arguments:
          * -d (--digitize document) : flag for digitize document.

* ### for My glossary 
*         python main.py -src "en" -tgt hi -i "how are you" -g
    
    Arguments:
*          * -g (--my glossary) : flag for my glossary.

### Content

1. config.py - contains data used for automation.
2. driver_script.py - contains code for loading browsers/driver.
3. elements.py - contains xpaths of elements in the website.
4. core_script.py - contains core functions for automation.
5. dataset_script.py - contains functions for dataset related automation.
6. model_script.py - contains functions for model related automation.
7. automate.py - main file for automation.
8. schema.yml - contains the schema used for automation.
9. requirements.txt - contains python-packages required to run automation. 

### Requirements

To install necessary packages for the script, run:

    pip install -r requirements.txt

## Notes

- update username/password [`ANUVAAD_USERNAME` / `ANUVAAD_PASSWORD`] in config.py file.
- For changing the Browser and Driver path, Update the config.py file
- default column names for CSV file are ["Dataset Name"], ["Dataset URL"]
- Required Drivers for Browser:
    - Google Chrome - chromedriver
