from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductScraper:
    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome()
    
    def get_product_name (self):
        product_name = WebDriverWait(self.driver, 10).until(

            EC.presence_of_all_elements_located((By.CLASS_NAME, "product-details-tile__title"))

        )

        return product_name[0].text
    
    def get_product_price(self):
        product_price = WebDriverWait(self.driver, 10).until(

            EC.presence_of_all_elements_located((By.CLASS_NAME, "value"))

        )

        return product_price[0].text
    
    def scrape_product (self):
        self.driver.get(self.url)
        product_name = self.get_product_name()
        product_price = self.get_product_price()
        print(f"{product_name} stojí {product_price} Kč.")
        self.driver.quit()
    
if __name__ == "__main__":
        url = str(input("Zadejte URL ze stránek iTesco: "))
        scraper = ProductScraper(url)
        scraper.scrape_product()
