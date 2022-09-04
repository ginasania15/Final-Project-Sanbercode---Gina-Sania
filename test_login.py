import unittest
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
    def test_a_success_login(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(5)
        driver.find_element(by=By.NAME, value='username').send_keys('Admin')
        time.sleep(1)
        driver.find_element(by=By.NAME, value='password').send_keys('admin123')
        time.sleep(1)
        driver.find_element(By.XPATH, "//form[1]").submit()
        time.sleep(5)
        url = driver.current_url
        self.assertEqual(url, "https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList")
    def test_a_empty_username_login(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(5)
        driver.find_element(by=By.NAME, value='password').send_keys('admin123')
        time.sleep(1)
        driver.find_element(By.XPATH, "//form[1]").submit()
        time.sleep(5)
        errormessage = driver.find_element(By.XPATH, "//form[1]/div[1]/div/span").text
        self.assertEqual(errormessage, "Required")
    def test_a_username_invalid_login(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(5)
        driver.find_element(by=By.NAME, value='username').send_keys('ginasania')
        time.sleep(1)
        driver.find_element(by=By.NAME, value='password').send_keys('admin123')
        time.sleep(1)
        driver.find_element(By.XPATH, "//form[1]").submit()
        time.sleep(5)
        errormessage = driver.find_element(by=By.CSS_SELECTOR, value="p.oxd-text.oxd-text--p.oxd-alert-content-text").text
        self.assertEqual(errormessage, "Invalid credentials")       
    def test_a_username_insert_with_email_login(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(5)
        driver.find_element(by=By.NAME, value='username').send_keys('ginasania15@gmail.com')
        time.sleep(1)
        driver.find_element(by=By.NAME, value='password').send_keys('admin123')
        time.sleep(1)
        driver.find_element(By.XPATH, "//form[1]").submit()
        time.sleep(5)
        errormessage = driver.find_element(by=By.CSS_SELECTOR, value="p.oxd-text.oxd-text--p.oxd-alert-content-text").text
        self.assertEqual(errormessage, "Invalid credentials")       
    def test_a_empty_password_login(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(5)
        driver.find_element(by=By.NAME, value='username').send_keys('Admin')
        time.sleep(1)
        driver.find_element(By.XPATH, "//form[1]").submit()
        time.sleep(5)
        errormessage = driver.find_element(By.XPATH, "//form[1]/div[2]/div/span").text
        self.assertEqual(errormessage, "Required")       
    def test_a_password_invalid_login(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(5)
        driver.find_element(by=By.NAME, value='username').send_keys('Admin')
        time.sleep(1)
        driver.find_element(by=By.NAME, value='password').send_keys('Testing123')
        time.sleep(1)
        driver.find_element(By.XPATH, "//form[1]").submit()
        time.sleep(5)
        errormessage = driver.find_element(by=By.CSS_SELECTOR, value="p.oxd-text.oxd-text--p.oxd-alert-content-text").text
        self.assertEqual(errormessage, "Invalid credentials")       
    def tearDown(self):
        self.driver.close()
if __name__ == "__main__":
    unittest.main()