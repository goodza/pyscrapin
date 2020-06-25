from selenium import webdriver
from flask import Flask, jsonify
import json

GOOGLE_CHROME_PATH = '/usr/bin/google-chrome'
CHROMEDRIVER_PATH = '/root/.pyenv/shims/chromedriver'

chrome_options = webdriver.ChromeOptions()

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

app = Flask(__name__)

@app.route('/')
def hello():
    chrome.get("https://mlcourse.ai/roadmap")
    title = chrome.title
    #chrome.quit()
    #return jsonify({"len":len(driver.find_elements_by_tag_name('tbody'))})
    return {
        'statusCode': 200,
        'body': json.dumps(title)

    }

if __name__ == '__main__':
    app.run()
