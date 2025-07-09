from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def fetch_products():
    url = "https://www.aunika.com/"
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(options=options)
    driver.get(url)

    items = driver.find_elements_by_css_selector(".product-item")
    products = []
    for el in items:
        title = el.find_element_by_css_selector(".product-title").text
        price = el.find_element_by_css_selector(".price").text
        products.append({"title": title, "price": price})
    driver.quit()
    return products
