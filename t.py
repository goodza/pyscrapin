from selenium import webdriver
from flask import Flask, escape, request


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
	name = request.args.get("name",  len(driver.find_elements_by_tag_name('tbody')))
    return f'Hello, {escape(name)}!'

	

