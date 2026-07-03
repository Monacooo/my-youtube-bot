import requests
import random
from playwright.sync_api import sync_playwright

def get_random_proxy():
    # سحب قائمة بروكسيات مجانية
    url = "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt"
    proxies = requests.get(url).text.split('\n')
    return random.choice(proxies).strip()

def run_task():
    proxy = get_random_proxy()
    with sync_playwright() as p:
        # استخدام البروكسي في المتصفح
        browser = p.chromium.launch(proxy={"server": f"http://{proxy}"})
        page = browser.new_page()
        # ... بقية كود المشاهدة ...
