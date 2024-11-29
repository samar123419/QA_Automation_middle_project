import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

class Testcontactus():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.driver.get("https://www.telerik.com/")
    self.driver.maximize_window()
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_validInputs(self):
   
    self.driver.find_element(By.CSS_SELECTOR, ".TK-Button--CTA-Sec").click()
    self.driver.find_element(By.ID, "Dropdown-1").click()
    dropdown = self.driver.find_element(By.ID, "Dropdown-1")
    dropdown.find_element(By.XPATH, "//option[. = 'Renewal']").click()
    self.driver.find_element(By.ID, "Dropdown-2").click()
    dropdown = self.driver.find_element(By.ID, "Dropdown-2")
    dropdown.find_element(By.XPATH, "//option[. = 'UI for ASP.NET AJAX']").click()

    time.sleep(6)

    self.driver.find_element(By.ID, "Textbox-1").click()
    self.driver.find_element(By.ID, "Textbox-1").send_keys("first")

    time.sleep(7)
    self.driver.find_element(By.ID, "Textbox-2").click()
    self.driver.find_element(By.ID, "Textbox-2").send_keys("last")

    self.driver.find_element(By.ID, "Email-1").click()
    self.driver.find_element(By.ID, "Email-1").send_keys("mail1@mail.com")
    self.driver.find_element(By.ID, "Textbox-3").click()
    self.driver.find_element(By.ID, "Textbox-3").send_keys("QA")

    time.sleep(5)

    self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div/div[6]/select").click()
    dropdown = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div/div[6]/select")
    dropdown.find_element(By.XPATH, "//option[. = 'Andorra']").click()

    self.driver.find_element(By.ID, "Textbox-4").click()
    self.driver.find_element(By.ID, "Textbox-4").send_keys("142")


    self.driver.find_element(By.ID, "Textarea-1").click()
    self.driver.find_element(By.ID, "Textarea-1").send_keys("comments")

    time.sleep(5)

    self.driver.find_element(By.CSS_SELECTOR, "#form--1 > form > div > div:nth-child(13) > button").click()

    time.sleep(5)
    WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "#ContentPlaceholder1_C018_Col01 > h1")))
    assert "Thank you for contacting us" in self.driver.title
  
  def test_empty_first_name_field(self): 
    self.driver.find_element(By.CSS_SELECTOR, ".TK-Button--CTA-Sec").click()
    self.driver.find_element(By.ID, "Dropdown-1").click()
    dropdown = self.driver.find_element(By.ID, "Dropdown-1")
    dropdown.find_element(By.XPATH, "//option[. = 'Renewal']").click()
    self.driver.find_element(By.ID, "Dropdown-2").click()
    dropdown = self.driver.find_element(By.ID, "Dropdown-2")
    dropdown.find_element(By.XPATH, "//option[. = 'UI for ASP.NET AJAX']").click()

    self.driver.find_element(By.ID, "Textbox-1").click()
    self.driver.find_element(By.ID, "Textbox-1").send_keys("")

    self.driver.find_element(By.ID, "Textbox-2").click()
    self.driver.find_element(By.ID, "Textbox-2").send_keys("last")

    self.driver.execute_script("window.scrollTo(0, 200)")

    self.driver.find_element(By.ID, "Email-1").click()
    self.driver.find_element(By.ID, "Email-1").send_keys("mail1@mail.com")

    self.driver.find_element(By.ID, "Textbox-3").click()
    self.driver.find_element(By.ID, "Textbox-3").send_keys("QA") 
    
    time.sleep(2)

    self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div/div[6]/select").click()
    dropdown = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div/div[6]/select")
    dropdown.find_element(By.XPATH, "//option[. = 'Andorra']").click()

    self.driver.find_element(By.ID, "Textbox-4").click()
    self.driver.find_element(By.ID, "Textbox-4").send_keys("142")
    self.driver.find_element(By.ID, "Textarea-1").click()

    self.driver.find_element(By.ID, "Textarea-1").send_keys("dgdvse")

    time.sleep(2)

    self.driver.find_element(By.CSS_SELECTOR, "#form--1 > form > div > div:nth-child(13) > button").click()

    time.sleep(2)
    WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".sfError")))
    assert "First name is required" in self.driver.find_element(By.CSS_SELECTOR, ".sfError").text
 
  def test_empty_last_name_field(self):
    self.driver.find_element(By.CSS_SELECTOR, ".TK-Button--CTA-Sec").click()
    self.driver.find_element(By.ID, "Dropdown-1").click()
    dropdown = self.driver.find_element(By.ID, "Dropdown-1")
    dropdown.find_element(By.XPATH, "//option[. = 'Renewal']").click()
    
    time.sleep(3)

    self.driver.find_element(By.ID, "Dropdown-2").click()
    dropdown = self.driver.find_element(By.ID, "Dropdown-2")
    dropdown.find_element(By.XPATH, "//option[. = 'UI for ASP.NET AJAX']").click()

    time.sleep(3)

    self.driver.find_element(By.ID, "Textbox-1").click()
    self.driver.find_element(By.ID, "Textbox-1").send_keys("first")

    # time.sleep(3)
    # self.driver.find_element(By.ID, "Textbox-2").click()
    # self.driver.find_element(By.ID, "Textbox-2").send_keys("")
    self.driver.execute_script("window.scrollTo(0, 200)")

    self.driver.find_element(By.ID, "Email-1").click()
    self.driver.find_element(By.ID, "Email-1").send_keys("mail1@mail.com")
    self.driver.find_element(By.ID, "Textbox-3").click()
    self.driver.find_element(By.ID, "Textbox-3").send_keys("QA")

    self.driver.execute_script("window.scrollTo(0, 160)")
    
    time.sleep(3)

    self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div/div[6]/select").click()
    dropdown = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div/div[6]/select")
    
    time.sleep(2)
    
    dropdown.find_element(By.XPATH, "//option[. = 'Andorra']").click()

    self.driver.find_element(By.ID, "Textbox-4").click()
    self.driver.find_element(By.ID, "Textbox-4").send_keys("142")

    self.driver.find_element(By.ID, "Textarea-1").click()
    self.driver.find_element(By.ID, "Textarea-1").send_keys("comments")

    time.sleep(5)

    self.driver.find_element(By.CSS_SELECTOR, "#form--1 > form > div > div:nth-child(13) > button").click()

    time.sleep(5)
    WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "#form--1 > form > div > div.sf-fieldWrp.Required.sfErrorWrp > p")))
    assert "Last name is required" in self.driver.find_element(By.CSS_SELECTOR, "#form--1 > form > div > div.sf-fieldWrp.Required.sfErrorWrp > p")
  
  def test_specialCharactersInLastNameField(self):
    self.driver.find_element(By.CSS_SELECTOR, ".TK-Button--CTA-Sec").click()
    self.driver.find_element(By.ID, "Dropdown-1").click()
    dropdown = self.driver.find_element(By.ID, "Dropdown-1")
    dropdown.find_element(By.XPATH, "//option[. = 'Renewal']").click()
    self.driver.find_element(By.ID, "Dropdown-2").click()
    dropdown = self.driver.find_element(By.ID, "Dropdown-2")
    dropdown.find_element(By.XPATH, "//option[. = 'UI for ASP.NET AJAX']").click()

    self.driver.find_element(By.ID, "Textbox-1").click()
    self.driver.find_element(By.ID, "Textbox-1").send_keys("first")

    self.driver.execute_script("window.scrollTo(0, 200)")

    self.driver.find_element(By.ID, "Textbox-2").click()
    self.driver.find_element(By.ID, "Textbox-2").send_keys(" ")

    self.driver.find_element(By.ID, "Email-1").click()
    self.driver.find_element(By.ID, "Email-1").send_keys("mail1@mail.com")

    self.driver.find_element(By.ID, "Textbox-3").click()
    self.driver.find_element(By.ID, "Textbox-3").send_keys("QA") 

    time.sleep(5)
    
    self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div/div[6]/select").click()
    dropdown = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div/div[6]/select")
    dropdown.find_element(By.XPATH, "//option[. = 'Andorra']").click()

    self.driver.find_element(By.ID, "Textbox-4").click()
    self.driver.find_element(By.ID, "Textbox-4").send_keys("142")
    self.driver.find_element(By.ID, "Textarea-1").click()

    self.driver.find_element(By.ID, "Textarea-1").send_keys("dgdvse")

    time.sleep(2)

    self.driver.find_element(By.CSS_SELECTOR, "#form--1 > form > div > div:nth-child(13) > button").click()

    time.sleep(2)

    WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR,".sfError")))
    assert "Your Last name has special characters." in self.driver.find_element(By.CSS_SELECTOR, ".sfError").text
 
  def test_emptyEmailField(self):
    
    self.driver.find_element(By.CSS_SELECTOR, ".TK-Button--CTA-Sec").click()
    self.driver.find_element(By.ID, "Dropdown-1").click()
    dropdown = self.driver.find_element(By.ID, "Dropdown-1")
    dropdown.find_element(By.XPATH, "//option[. = 'Renewal']").click()

    self.driver.find_element(By.ID, "Dropdown-2").click()
    dropdown = self.driver.find_element(By.ID, "Dropdown-2")
    dropdown.find_element(By.XPATH, "//option[. = 'UI for ASP.NET AJAX']").click()

    self.driver.find_element(By.ID, "Textbox-1").click()
    self.driver.find_element(By.ID, "Textbox-1").send_keys("first")

    self.driver.find_element(By.ID, "Textbox-2").click()
    self.driver.find_element(By.ID, "Textbox-2").send_keys("last")

    self.driver.execute_script("window.scrollTo(0, 250)")

    self.driver.find_element(By.ID, "Textbox-3").click()
    self.driver.find_element(By.ID, "Textbox-3").send_keys("QA") 
    
    time.sleep(3)

    self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div/div[6]/select").click()
    dropdown = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div/div[6]/select")
    dropdown.find_element(By.XPATH, "//option[. = 'Andorra']").click()
    
    time.sleep(5)
    
    self.driver.find_element(By.ID, "Textbox-4").click()
    self.driver.find_element(By.ID, "Textbox-4").send_keys("142")


    self.driver.find_element(By.ID, "Textarea-1").click()
    self.driver.find_element(By.ID, "Textarea-1").send_keys("comments: empty email field")

    time.sleep(2)

    self.driver.find_element(By.CSS_SELECTOR, "#form--1 > form > div > div:nth-child(13) > button").click()

    time.sleep(2)

    WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".sfError")))
    assert "Email address is required" in self.driver.find_element(By.CSS_SELECTOR, ".sfError").text

  def test_tooltipPhoneField(self):
    self.driver.find_element(By.CSS_SELECTOR, ".TK-Button--CTA-Sec").click() 
    
    self.driver.execute_script("window.scrollTo(0, 250)")

    element = self.driver.find_element(By.CSS_SELECTOR, "#form--1 > form > div > div:nth-child(9) > label > span")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    
    tooltip_locator = (By.CSS_SELECTOR, "#form--1 > form > div > div:nth-child(9) > label > span > span")
    tooltip_element = WebDriverWait(self.driver, 35).until(
    EC.visibility_of_element_located(tooltip_locator))

    tooltip_text = tooltip_element.text

    assert tooltip_text == "For an even faster response, please leave your telephone number." 

  def test_charsInPhone(self):
    self.driver.find_element(By.CSS_SELECTOR, ".TK-Button--CTA-Sec").click()
    self.driver.find_element(By.ID, "Dropdown-1").click()
    dropdown = self.driver.find_element(By.ID, "Dropdown-1")
    dropdown.find_element(By.XPATH, "//option[. = 'Renewal']").click()
    self.driver.find_element(By.ID, "Dropdown-2").click()
    dropdown = self.driver.find_element(By.ID, "Dropdown-2")
    dropdown.find_element(By.XPATH, "//option[. = 'UI for ASP.NET AJAX']").click()
    self.driver.find_element(By.ID, "Textbox-1").click()
    self.driver.find_element(By.ID, "Textbox-1").send_keys("first")
    self.driver.find_element(By.ID, "Textbox-2").click()
    self.driver.find_element(By.ID, "Textbox-2").send_keys("last")
    self.driver.find_element(By.ID, "Email-1").click()
    self.driver.find_element(By.ID, "Email-1").send_keys("mail1@mail.com")
    self.driver.find_element(By.ID, "Textbox-3").click()
    self.driver.find_element(By.ID, "Textbox-3").send_keys("QA")

    time.sleep(3)

    self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div/div[6]/select").click()
    dropdown = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div/div[6]/select")
    dropdown.find_element(By.XPATH, "//option[. = 'Andorra']").click()

    self.driver.find_element(By.ID, "Textbox-4").click()
    self.driver.find_element(By.ID, "Textbox-4").send_keys("abc12+/3")

    self.driver.find_element(By.ID, "Textarea-1").click()
    self.driver.find_element(By.ID, "Textarea-1").send_keys("Chars and speciel characters in phone number")

    self.driver.find_element(By.CSS_SELECTOR, "#form--1 > form > div > div:nth-child(13) > button").click()

    time.sleep(5)

    assert "Invalid phone number" in  self.driver.find_element(By.CSS_SELECTOR, ".sfError").text

