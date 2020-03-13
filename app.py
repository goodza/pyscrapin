from selenium import webdriver
from flask import Flask, jsonify


GOOGLE_CHROME_PATH = '/app/.apt/usr/bin/google_chrome'
CHROMEDRIVER_PATH = '/app/.chromedriver/bin/chromedriver'

chrome_options = webdriver.ChromeOptions()

chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')
chrome_options.binary_location = GOOGLE_CHROME_PATH

driver = webdriver.Chrome(execution_path=CHROMEDRIVER_PATH, chrome_options=chrome_options)

app = Flask(__name__)

@app.route('/')
def hello():
	driver.get("https://mlcourse.ai/roadmap")
	return jsonify({"len":len(driver.find_elements_by_tag_name('tbody'))})

if __name__ == '__main__':
    app.run()

