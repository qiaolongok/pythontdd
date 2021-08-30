import sys,os
dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(dir)

from selenium import webdriver

browser=webdriver.Firefox()

browser.get("http://localhost:8000")

assert "django" in browser.page_source