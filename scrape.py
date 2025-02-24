from selenium.webdriver import Remote, ChromeOptions
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.remote_connection import RemoteConnection
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chromium.remote_connection import ChromiumRemoteConnection
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os
import time
import requests

load_dotenv()

# SBR_WEBDRIVER = os.getenv("SBR_WEBDRIVER")

SBR_WEBDRIVER = "https://brd-customer-hl_61c358de-zone-scraping_browser1:xbv82eoq83wd@brd.superproxy.io:9515"

def scrape_website(website):
    print("Connecting to Scraping Browser...")
    # chrome_options = Options()
    # chrome_options.headless = False  # Disable headless mode
    sbr_connection = ChromiumRemoteConnection(SBR_WEBDRIVER, "goog", "chrome")
    with Remote(sbr_connection, options=ChromeOptions()) as driver:
    # with Remote(sbr_connection, options=chrome_options) as driver:
        driver.get(website)
        print("Waiting captcha to solve...")
        solve_res = driver.execute(
            "executeCdpCommand",
            {
                "cmd": "Captcha.waitForSolve",
                "params": {"detectTimeout": 10000},
            },
        )
        print("Captcha solve status:", solve_res["value"]["status"])
        print("Navigated! Scraping page content...")
        html = driver.page_source
        return html
    
# def scrape_website(website):
#     print("Connecting to Scraping Browser...")
    

# def scrape_website(website):
#     print("Connecting to Scraping Browser...")
#     chrome_options = Options()
#     chrome_options.headless = False  # Disable headless mode
#     chrome_options.add_experimental_option("detach", True)  # Keeps browser open
#     # Local WebDriver
#     driver = webdriver.Chrome(options=chrome_options)
#     driver.get(website)
#     WebDriverWait(driver, 20).until(
#             EC.presence_of_element_located((By.TAG_NAME, 'body'))  # You can also use another element like a footer or a header
#         )
#     time.sleep(10)
#     html = driver.page_source
#     print("Done")
#     return html

def extract_body_content(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    body_content = soup.body
    if body_content:
        return str(body_content)
    return ""


def clean_body_content(body_content):
    soup = BeautifulSoup(body_content, "html.parser")

    for script_or_style in soup(["script", "style", "svg", "header", "think", "img", "button"]):
        script_or_style.extract()

    # Retain <a> tags and their href attributes
    for a_tag in soup.find_all("a"):
        a_tag.insert_before(f" [{a_tag.get('href')}] ")
        a_tag.unwrap()  # Remove the <a> tags but keep the href text
        
    # Get text or further process the content
    cleaned_content = soup.get_text(separator="\n")
    cleaned_content = "\n".join(
        line.strip() for line in cleaned_content.splitlines() if line.strip()
    )
    # cleaned_content = str(soup)

    return cleaned_content


def split_dom_content(dom_content, max_length=6000):
    return [
        dom_content[i : i + max_length] for i in range(0, len(dom_content), max_length)
    ]
