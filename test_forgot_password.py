import unittest
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
class TestForgot(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
    def test_a_success_forgot(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/requestPasswordResetCode")
        time.sleep(5)
        driver.find_element(by=By.NAME, value='username').send_keys('Admin')
        time.sleep(1)
        driver.find_element(By.XPATH, "//form[1]").submit()
        time.sleep(5)
        url = driver.current_url
        self.assertEqual(url, "https://opensource-demo.orangehrmlive.com/web/index.php/auth/sendPasswordReset")
    def test_a_empty_username_forgot(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/requestPasswordResetCode")
        time.sleep(5)
        driver.find_element(By.XPATH, "//form[1]").submit()
        time.sleep(5)
        errormessage = driver.find_element(By.XPATH, "//form[1]/div[1]/div/span").text
        self.assertEqual(errormessage, "Required")       
    def test_a_invalid_username_forgot(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/requestPasswordResetCode")
        time.sleep(5)
        driver.find_element(by=By.NAME, value='username').send_keys('ginasania')
        time.sleep(1)
        driver.find_element(By.XPATH, "//form[1]").submit()
        time.sleep(5)
        errormessage = driver.find_element(By.XPATH, "//form[1]/div[1]/div/span").text
        self.assertEqual(errormessage, "Username doesn't exist")
    def tearDown(self):
        self.driver.close()
if __name__ == "__main__":
    unittest.main()