import re
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


logging.basicConfig(level=logging.INFO)

class ProductScraper:
    def __init__(self, url):
        self.url = self._validate_itesco_url(url)
        self.driver = webdriver.Chrome()
        self.driver.set_page_load_timeout(30)
        self.driver.set_script_timeout(10)
    
    def _validate_itesco_url(self, url):

        pattern = re.compile(r"^https?://www\.itesco\.cz/.*$")

        if not pattern.match(url):

            raise ValueError("Nejedná se validní odkaz.")

        return url
    
    def get_product_name (self):
        try:
            product_name = WebDriverWait(self.driver, 10).until(

                EC.presence_of_element_located((By.CLASS_NAME, "product-details-tile__title"))

        )
            return product_name.text
        except Exception as e:
             raise Exception("Selhalo nalezení názvu produktu.") from e
    
    def get_product_price(self):
        try:
            product_price = WebDriverWait(self.driver, 10).until(

            EC.presence_of_element_located((By.CLASS_NAME, "value"))

        )

            return product_price.text
        except Exception as e:
             raise Exception("Selhalo nalezení ceny produktu.") from e
    
    def scrape_product (self):
        try:
            self.driver.get(self.url)
            product_name = self.get_product_name()
            product_price = self.get_product_price()
            print(f"{product_name} stojí {product_price} Kč.")
        except Exception as e:
             raise Exception("Nepodařilo se zaanalyzovat produktu v odkaze.") from e
        finally:
            self.driver.quit()
    
if __name__ == "__main__":
        url = str(input("Zadejte URL ze stránek iTesco: "))
        scraper = ProductScraper(url)
        scraper.scrape_product()
