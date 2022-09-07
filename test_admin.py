import unittest
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from random import randint
from selenium.webdriver.support.ui import Select
class TestAdmin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
    def test_a_success_add_admin(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(5)
        driver.find_element(by=By.NAME, value='username').send_keys('Admin')
        time.sleep(1)
        driver.find_element(by=By.NAME, value='password').send_keys('admin123')
        time.sleep(1)
        driver.find_element(By.XPATH, "//form[1]").submit()
        time.sleep(5)
        driver.find_element_by_xpath("//a[contains(@href,'/web/index.php/admin/viewAdminModule')]").click()
        time.sleep(4)
        driver.find_element(By.XPATH, "//html/body/div/div/div[2]/div[2]/div/div[2]/div/button").click()
        time.sleep(4)
        driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div').click()
        # select = Select(driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div'))
        # select.select_by_value('2')
        time.sleep(10)
    def tearDown(self):
        self.driver.close()
if __name__ == "__main__":
    unittest.main()