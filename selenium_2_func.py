from selenium import webdriver
from selenium.webdriver.common.by import By

def login_to_website(username, password):
    with webdriver.Chrome() as driver:
        driver.get('https://cs.wikipedia.org/w/index.php?returnto=Hlavn%C3%AD+strana&title=Speci%C3%A1ln%C3%AD:P%C5%99ihl%C3%A1sit&centralAuthAutologinTried=1&centralAuthError=Not+centrally+logged+in')

        username_field = driver.find_element(By.ID, 'wpName1')
        password_field = driver.find_element(By.ID, 'wpPassword1')
        login_button = driver.find_element(By.ID, 'wpLoginAttempt')

        username_field.send_keys(username)
        password_field.send_keys(password)
        login_button.click()

def main():
    username = input("Prosím, vložte své přihlašovací jméno pro přihlášení na Wikipedii: ")
    password = input("Prosím, vložte své heslo pro přihlášení na Wikipedii: ")
    login_to_website(username, password)

if __name__ == "__main__":
    main()
