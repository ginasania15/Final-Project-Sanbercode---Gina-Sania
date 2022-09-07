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
    def test_a_required_add_first_name_employee(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(5)
        driver.find_element(by=By.NAME, value='username').send_keys('Admin')
        time.sleep(1)
        driver.find_element(by=By.NAME, value='password').send_keys('admin123')
        time.sleep(1)
        driver.find_element(By.XPATH, "//form[1]").submit()
        time.sleep(5)
        driver.find_element_by_xpath("//a[contains( text( ), 'Add Employee')]").click()
        time.sleep(4)
        rand = randint(0, 100)
        time.sleep(1)
        driver.find_element(By.XPATH, "//form[1]").submit()
        time.sleep(2)
        errormessage = driver.find_element(By.XPATH, "//form[1]/div/div[2]/div/div/div/div/div[2]/div[1]/span").text
        self.assertEqual(errormessage, "Required")
    def test_a_required_add_last_name_employee(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(5)
        driver.find_element(by=By.NAME, value='username').send_keys('Admin')
        time.sleep(1)
        driver.find_element(by=By.NAME, value='password').send_keys('admin123')
        time.sleep(1)
        driver.find_element(By.XPATH, "//form[1]").submit()
        time.sleep(5)
        driver.find_element_by_xpath("//a[contains( text( ), 'Add Employee')]").click()
        time.sleep(4)
        driver.find_element(by=By.NAME, value='firstName').send_keys('Sania')
        driver.find_element(By.XPATH, "//form[1]").submit()
        time.sleep(2)
        errormessage = driver.find_element(By.XPATH, "//form[1]/div/div[2]/div/div/div/div/div[2]/div[3]/span").text
        self.assertEqual(errormessage, "Required")
    def test_a_required_username_employee(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(5)
        driver.find_element(by=By.NAME, value='username').send_keys('Admin')
        time.sleep(1)
        driver.find_element(by=By.NAME, value='password').send_keys('admin123')
        time.sleep(1)
        driver.find_element(By.XPATH, "//form[1]").submit()
        time.sleep(5)
        driver.find_element_by_xpath("//a[contains( text( ), 'Add Employee')]").click()
        time.sleep(4)
        driver.find_element(by=By.NAME, value='firstName').send_keys('Sania')
        driver.find_element(By.XPATH, "//form[1]/div[1]/div[2]/div[2]/div/label/span").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//form[1]").submit()
        errormessage = driver.find_element(By.XPATH, "//form[1]/div[1]/div[2]/div[3]/div/div[1]/div/span").text
        time.sleep(1)
        self.assertEqual(errormessage, "Required")
        time.sleep(5)
    def test_a_required_password_employee(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(5)
        driver.find_element(by=By.NAME, value='username').send_keys('Admin')
        time.sleep(1)
        driver.find_element(by=By.NAME, value='password').send_keys('admin123')
        time.sleep(1)
        driver.find_element(By.XPATH, "//form[1]").submit()
        time.sleep(5)
        driver.find_element_by_xpath("//a[contains( text( ), 'Add Employee')]").click()
        time.sleep(4)
        driver.find_element(by=By.NAME, value='firstName').send_keys('Sania')
        driver.find_element(By.XPATH, "//form[1]/div[1]/div[2]/div[2]/div/label/span").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//form[1]").submit()
        errormessage = driver.find_element(By.XPATH, "//form[1]/div[1]/div[2]/div[4]/div/div[1]/div/span").text
        time.sleep(1)
        self.assertEqual(errormessage, "Required")
        time.sleep(5)
    def test_a_format_password_employee(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(5)
        driver.find_element(by=By.NAME, value='username').send_keys('Admin')
        time.sleep(1)
        driver.find_element(by=By.NAME, value='password').send_keys('admin123')
        time.sleep(1)
        driver.find_element(By.XPATH, "//form[1]").submit()
        time.sleep(5)
        driver.find_element_by_xpath("//a[contains( text( ), 'Add Employee')]").click()
        time.sleep(4)
        driver.find_element(by=By.NAME, value='firstName').send_keys('Sania')
        driver.find_element(By.XPATH, "//form[1]/div[1]/div[2]/div[2]/div/label/span").click()
        time.sleep(1)
        driver.find_element(by=By.XPATH, value="//input[@type='password']").send_keys('Sania')
        time.sleep(1)
        driver.find_element(By.XPATH, "//form[1]").submit()
        errormessage = driver.find_element(By.XPATH, "//form[1]/div[1]/div[2]/div[4]/div/div[1]/div/span").text
        time.sleep(1)
        self.assertEqual(errormessage, "Should have at least 8 characters")
        time.sleep(5)
    def tearDown(self):
        self.driver.close()
if __name__ == "__main__":
    unittest.main()