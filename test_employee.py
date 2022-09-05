import unittest
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from random import randint
class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
    def test_a_success_add_employee(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(5)
        driver.find_element(by=By.NAME, value='username').send_keys('Admin')
        time.sleep(1)
        driver.find_element(by=By.NAME, value='password').send_keys('admin123')
        time.sleep(1)
        driver.find_element(By.XPATH, "//form[1]").submit()
        time.sleep(5)
        driver.find_element_by_xpath ("//a[contains( text( ), 'Add Employee')]").click()
        time.sleep(4)
        rand = randint(0, 100)
        driver.find_element(by=By.NAME, value='firstName').send_keys('Test'+str(rand))
        time.sleep(1)
        driver.find_element(by=By.NAME, value='middleName').send_keys('Gina')
        time.sleep(1)
        driver.find_element(by=By.NAME, value='lastName').send_keys('Sania')
        time.sleep(1)
        driver.find_element(By.XPATH, "//form[1]").submit()
        time.sleep(10)
        url = driver.current_url
        self.assertIn("https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewPersonalDetails/empNumber",url);
    def tearDown(self):
        self.driver.close()
if __name__ == "__main__":
    unittest.main()