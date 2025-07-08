from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from time import sleep

def fetch_products():
    url = "https://www.aunika.com/"
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)
    driver.get(url)
    sleep(3)
    items = driver.find_elements_by_css_selector(".product-item")
    products = []
    for el in items:
        title = el.find_element_by_css_selector(".product-title").text
        price = el.find_element_by_css_selector(".price").text
        products.append({"title": title, "price": price})
    driver.quit()
    return products
