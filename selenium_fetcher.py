from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep

def fetch_products():
    url = "https://www.aunika.com/"
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=options)
    driver.get(url)
    sleep(3)

    items = driver.find_elements(By.CSS_SELECTOR, ".product-item")
    products = []
    for el in items:
        title_el = el.find_element(By.CSS_SELECTOR, ".product-title")
        price_el = el.find_element(By.CSS_SELECTOR, ".price")

        title = title_el.text.strip()
        price = price_el.text.strip()
        products.append({"title": title, "price": price})

    driver.quit()
    return products
