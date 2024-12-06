import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.support import expected_conditions as EC


class TestTestaccount():
  def setup_method(self, method):
    #self.driver = webdriver.Chrome()
    self.driver = webdriver.Edge()

    self.driver.get("https://www.telerik.com/")
    self.driver.maximize_window()
  
  def teardown_method(self, method):
    self.driver.quit()
   
  def test_change_email(self):
    self.driver.find_element(By.CSS_SELECTOR, "#js-tlrk-nav-not-auth-container > .TK-Aside-Menu-Button").click()
    self.driver.find_element(By.ID, "email").click()
    self.driver.find_element(By.ID, "email").send_keys("pod90@gmail.com")
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()

    self.driver.implicitly_wait(5)

    wait = WebDriverWait(self.driver, 10)
    clickable_element = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Change Email")))

    clickable_element.click()

    assert "Enter Your Email to Sign in" in self.driver.find_element(By.CSS_SELECTOR, ".u-mb30").text

  def test_symbol_in_email_account(self):
    self.driver.find_element(By.CSS_SELECTOR, "#js-tlrk-nav-not-auth-container > .TK-Aside-Menu-Button").click()
    self.driver.find_element(By.ID, "email").click()
    self.driver.find_element(By.ID, "email").send_keys("po/90@gmail.com")
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
    WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".error-message")))
    assert self.driver.find_element(By.CSS_SELECTOR, "body > div.app-content > app > div:nth-child(3) > div > ng-component > div > loader > div.loader-content > div > form > div.form-field.u-mb30i > validation-messages > div > span").text == "Invalid email"

  def test_empty_email_account_field(self):
    self.driver.find_element(By.CSS_SELECTOR, "#js-tlrk-nav-not-auth-container > .TK-Aside-Menu-Button").click()
    self.driver.find_element(By.ID, "email").click()
    self.driver.find_element(By.ID, "email").send_keys("")
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
    WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".error-message")))
    assert self.driver.find_element(By.CSS_SELECTOR, "body > div.app-content > app > div:nth-child(3) > div > ng-component > div > loader > div.loader-content > div > form > div.form-field.u-mb30i > validation-messages > div > span").text == "Email is required"
  
  def test_tooltip_phone_field(self):
    self.driver.find_element(By.CSS_SELECTOR, "#js-tlrk-nav-not-auth-container > .TK-Aside-Menu-Button").click()
    self.driver.find_element(By.ID, "email").click()
    self.driver.find_element(By.ID, "email").send_keys("pod90@gmail.com")
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
    time.sleep(3)
    self.driver.execute_script("window.scrollTo(0, 200)")
    
    element = self.driver.find_element(By.CSS_SELECTOR, "#registerForm > div.row.u-mb15 > div:nth-child(4) > div")                                                                                                            
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()

    tooltip_locator = (By.CSS_SELECTOR, "#registerForm > div.row.u-mb15 > div:nth-child(4) > div > div")
    tooltip_element = WebDriverWait(self.driver, 10).until(
    EC.visibility_of_element_located(tooltip_locator)
)
    tooltip_text = tooltip_element.text

    assert tooltip_text == "To provide you with additional support and customized offers." 
    
  def test_tooltip_country_field(self):
    self.driver.find_element(By.CSS_SELECTOR, "#js-tlrk-nav-not-auth-container > .TK-Aside-Menu-Button").click()
    self.driver.find_element(By.ID, "email").click()
    self.driver.find_element(By.ID, "email").send_keys("pod90@gmail.com")
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()

    time.sleep(5)
   
    self.driver.execute_script("window.scrollTo(0, 200)")

    element = self.driver.find_element(By.CSS_SELECTOR, "#registerForm > div.row.u-mb15 > div.col-md-6.form-field.col-md-12 > div")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    
    tooltip_locator = (By.CSS_SELECTOR, "#registerForm > div.row.u-mb15 > div.col-md-6.form-field.col-md-12 > div > div")
    tooltip_element = WebDriverWait(self.driver, 30).until(
    EC.visibility_of_element_located(tooltip_locator)
)
    time.sleep(5)

    tooltip_text = tooltip_element.text

    assert tooltip_text == "To assign you to a local team that can support all your needs during the trial period." 

  def test_empty_country(self):
    self.driver.find_element(By.CSS_SELECTOR, "#js-tlrk-nav-not-auth-container > .TK-Aside-Menu-Button").click()
    self.driver.find_element(By.ID, "email").click()
    self.driver.find_element(By.ID, "email").send_keys("pod90@gmail.com")
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
    
    time.sleep(3)
    self.driver.execute_script("window.scrollTo(0, 200)")
    self.driver.find_element(By.ID, "password").click()
    self.driver.find_element(By.ID, "password").send_keys("111111")
    self.driver.find_element(By.ID, "fist-name").click()
    self.driver.find_element(By.ID, "fist-name").send_keys("first")
    self.driver.find_element(By.ID, "last-name").click()
    self.driver.find_element(By.ID, "last-name").send_keys("last")
    time.sleep(3)
    self.driver.find_element(By.ID, "company").click()
    self.driver.find_element(By.ID, "company").send_keys("comp")
    self.driver.find_element(By.ID, "phone").click()
    self.driver.find_element(By.ID, "phone").send_keys("14723")

    time.sleep(3)

    self.driver.find_element(By.CSS_SELECTOR, "#registerForm > div:nth-child(4) > button").click()

    assert "Country is required" in self.driver.find_element(By.CSS_SELECTOR, "#registerForm > div.row.u-mb15 > div.col-md-6.form-field.col-md-12 > validation-messages > div > span").text

  def test_empty_password_in_login(self):

    self.driver.find_element(By.CSS_SELECTOR, "#js-tlrk-nav-not-auth-container svg").click()
    self.driver.find_element(By.ID, "email").click()
    self.driver.find_element(By.ID, "email").send_keys("samar.abu.hdeeb@gmail.com")
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
    time.sleep(5)
    self.driver.find_element(By.XPATH,"/html/body/div[2]/app/div[2]/div/ng-component/div/loader/div[1]/div/div/form/div[4]/button").click()
    WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".error-message")))
    assert self.driver.find_element(By.CSS_SELECTOR, ".error-message").text == "Password is required"

  
  @pytest.mark.xfail
  def test_create_account(self):
    self.driver.find_element(By.CSS_SELECTOR, "#js-tlrk-nav-not-auth-container > .TK-Aside-Menu-Button").click()
    self.driver.find_element(By.ID, "email").click()
    self.driver.find_element(By.ID, "email").send_keys("1a22ddfghf@gmaail.com")
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
    self.driver.find_element(By.ID, "password").send_keys("Samar")
    self.driver.find_element(By.ID, "fist-name").click()
    self.driver.find_element(By.ID, "fist-name").send_keys("aqw")
    self.driver.find_element(By.ID, "last-name").click()
    self.driver.find_element(By.ID, "last-name").send_keys("qwe")
    self.driver.find_element(By.ID, "company").click()
    self.driver.find_element(By.ID, "company").send_keys("dfg")
    self.driver.find_element(By.ID, "phone").click()
    self.driver.find_element(By.ID, "phone").send_keys("14723")
    self.driver.find_element(By.CSS_SELECTOR, ".k-input-button:nth-child(3) > .k-button-icon").click()
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
    self.driver.switch_to.default_content()
    self.driver.switch_to.frame(0)
    self.driver.find_element(By.CSS_SELECTOR, "body").click()
    WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".u-mb20")))
    assert self.driver.find_element(By.CSS_SELECTOR, ".u-mb20").text == " If you did not get your email, check your Spam folder or "
  


  @pytest.mark.skip
  def test_login(self):
    self.driver.find_element(By.CSS_SELECTOR, "#js-tlrk-nav-not-auth-container svg").click()
    self.driver.find_element(By.ID, "email").click()
    self.driver.find_element(By.ID, "email").send_keys("samar.abu.hdeeb@gmail.com")
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
    self.driver.find_element(By.ID, "password").send_keys("Samar")
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".Title--xxxl").text == "Telerik Login"


    

