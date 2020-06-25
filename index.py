from selenium import webdriver
import json
import os

def handler(event, context):
    
    print(str(os.getcwd()))
    print('#HANDLER::2::')
    options = webdriver.ChromeOptions()
    options.binary_location = "./bin/headless-chromium"
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1280x1696")
    options.add_argument("--disable-application-cache")
    options.add_argument("--disable-infobars")
    options.add_argument("--no-sandbox")
    options.add_argument("--hide-scrollbars")
    options.add_argument("--enable-logging")
    options.add_argument("--log-level=0")
    options.add_argument("--single-process")
    options.add_argument("--homedir=/tmp")
    options.add_argument("--ignore-certificate-errors")
    chrome = webdriver.Chrome('./bin/chromedriver',chrome_options=options)
    #chrome = webdriver.Chrome(chrome_options=options) 
    chrome.get('https://yandex.ru')
    title = chrome.title
    chrome.quit()
    return {
        'statusCode': 200,
        'body': json.dumps(title)
    }


#print(handler('',''))
