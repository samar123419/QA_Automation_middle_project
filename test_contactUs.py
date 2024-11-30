import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC

class Testcontactus():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    # self.driver = webdriver.Edge()
    self.driver.get("https://www.telerik.com/")
    self.driver.maximize_window()
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_valid_inputs(self):
    self.driver.find_element(By.CSS_SELECTOR, ".TK-Button--CTA-Sec").click()
    time.sleep(2)
    dropdown = self.driver.find_element(By.ID, "Dropdown-1")
    select = Select(dropdown)
    select.select_by_index(3)
    
    time.sleep(2)

    dropdown = self.driver.find_element(By.ID, "Dropdown-2")
    select = Select(dropdown)
    select.select_by_index(3)

    time.sleep(2)

    self.driver.find_element(By.ID, "Textbox-1").click()
    self.driver.find_element(By.ID, "Textbox-1").send_keys("first")

    time.sleep(3)
    self.driver.find_element(By.ID, "Textbox-2").click()
    self.driver.find_element(By.ID, "Textbox-2").send_keys("last")

    self.driver.execute_script("window.scrollTo(0, 300)")

    self.driver.find_element(By.ID, "Email-1").click()
    self.driver.find_element(By.ID, "Email-1").send_keys("mail1@mail.com")
    self.driver.find_element(By.ID, "Textbox-3").click()
    self.driver.find_element(By.ID, "Textbox-3").send_keys("QA")

    time.sleep(3)
    
    dropdown = self.driver.find_element(By.ID, "Country-1")
    select = Select(dropdown)
    select.select_by_value("Israel")
  
    time.sleep(2)

    self.driver.find_element(By.ID, "Textbox-4").click()
    self.driver.find_element(By.ID, "Textbox-4").send_keys("142")

    self.driver.execute_script("window.scrollTo(0, 700)")

    self.driver.find_element(By.ID, "Textarea-1").click()
    self.driver.find_element(By.ID, "Textarea-1").send_keys("comments: valid inputs, e2e test")

    # time.sleep(5)
    # element = self.driver.find_element(By.CSS_SELECTOR, "#OptInOutField-1")
    # if element.is_displayed:
    #   element.click()

    #OptInOutField-1
    time.sleep(2)
    self.driver.find_element(By.CSS_SELECTOR, "#form--1 > form > div > div:nth-child(13) > button").click()

    """if check box appear manual check"""
    time.sleep(5)

    WebDriverWait(self.driver, 50).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "#ContentPlaceholder1_C018_Col01 > h1")))
    assert "Thank you for contacting us" in self.driver.title
  
  def test_unselected1(self): 
    self.driver.find_element(By.CSS_SELECTOR, ".TK-Button--CTA-Sec").click()
    
    # dropdown = self.driver.find_element(By.ID, "Dropdown-1")
    # select = Select(dropdown)
    # select.select_by_index(3)
    
    time.sleep(2)

    dropdown = self.driver.find_element(By.ID, "Dropdown-2")
    select = Select(dropdown)
    select.select_by_index(3)

    time.sleep(2)

    self.driver.find_element(By.ID, "Textbox-1").click()
    self.driver.find_element(By.ID, "Textbox-1").send_keys("first")

    time.sleep(3)
    self.driver.find_element(By.ID, "Textbox-2").click()
    self.driver.find_element(By.ID, "Textbox-2").send_keys("last")

    time.sleep(3)
    self.driver.execute_script("window.scrollTo(0, 550)")

    self.driver.find_element(By.ID, "Email-1").click()
    self.driver.find_element(By.ID, "Email-1").send_keys("mail1@mail.com")
    self.driver.find_element(By.ID, "Textbox-3").click()
    self.driver.find_element(By.ID, "Textbox-3").send_keys("QA")

    time.sleep(3)

    dropdown = self.driver.find_element(By.ID, "Country-1")
    select = Select(dropdown)
    select.select_by_index(22)
    
    time.sleep(3)

    self.driver.find_element(By.ID, "Textbox-4").click()
    self.driver.find_element(By.ID, "Textbox-4").send_keys("142")

    self.driver.find_element(By.ID, "Textarea-1").click()
    self.driver.find_element(By.ID, "Textarea-1").send_keys("comments: unselect option")

    self.driver.execute_script("window.scrollTo(0, 600)")
   
    time.sleep(2)

    self.driver.find_element(By.CSS_SELECTOR, "#form--1 > form > div > div:nth-child(13) > button").click()

    # time.sleep(2)
    WebDriverWait(self.driver, 40).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".sfError")))
    assert "Please select an option" in self.driver.find_element(By.CSS_SELECTOR, ".sfError").text
  
  def test_unselect_product_interest(self): 
    self.driver.find_element(By.CSS_SELECTOR, ".TK-Button--CTA-Sec").click()
    
    dropdown = self.driver.find_element(By.ID, "Dropdown-1")
    select = Select(dropdown)
    select.select_by_index(3)
    
    # time.sleep(2)

    # dropdown = self.driver.find_element(By.ID, "Dropdown-2")
    # select = Select(dropdown)
    # select.select_by_index(3)

    time.sleep(2)

    self.driver.find_element(By.ID, "Textbox-1").click()
    self.driver.find_element(By.ID, "Textbox-1").send_keys("first")

    time.sleep(3)
    self.driver.find_element(By.ID, "Textbox-2").click()
    self.driver.find_element(By.ID, "Textbox-2").send_keys("last")

    time.sleep(3)
    self.driver.execute_script("window.scrollTo(0, 550)")

    self.driver.find_element(By.ID, "Email-1").click()
    self.driver.find_element(By.ID, "Email-1").send_keys("mail1@mail.com")
    self.driver.find_element(By.ID, "Textbox-3").click()
    self.driver.find_element(By.ID, "Textbox-3").send_keys("QA")

    time.sleep(3)

    dropdown = self.driver.find_element(By.ID, "Country-1")
    select = Select(dropdown)
    select.select_by_index(22)
    
    time.sleep(3)

    self.driver.find_element(By.ID, "Textbox-4").click()
    self.driver.find_element(By.ID, "Textbox-4").send_keys("142")

    self.driver.find_element(By.ID, "Textarea-1").click()
    self.driver.find_element(By.ID, "Textarea-1").send_keys("comments: unselect option")

    self.driver.execute_script("window.scrollTo(0, 600)")
    
    time.sleep(2)

    self.driver.find_element(By.CSS_SELECTOR, "#form--1 > form > div > div:nth-child(13) > button").click()

    # time.sleep(2)
    WebDriverWait(self.driver, 40).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".sfError")))
    assert "Please select a product interest" in self.driver.find_element(By.CSS_SELECTOR, ".sfError").text
  
  def test_empty_first_name_field(self): 
    self.driver.find_element(By.CSS_SELECTOR, ".TK-Button--CTA-Sec").click()
    
    dropdown = self.driver.find_element(By.ID, "Dropdown-1")
    select = Select(dropdown)
    select.select_by_index(3)
    
    time.sleep(2)

    dropdown = self.driver.find_element(By.ID, "Dropdown-2")
    select = Select(dropdown)
    select.select_by_index(3)

    time.sleep(2)

    # self.driver.find_element(By.ID, "Textbox-1").click()
    # self.driver.find_element(By.ID, "Textbox-1").send_keys("first")

    self.driver.find_element(By.ID, "Textbox-2").click()
    self.driver.find_element(By.ID, "Textbox-2").send_keys("last")

    time.sleep(3)
    self.driver.execute_script("window.scrollTo(0, 550)")

    self.driver.find_element(By.ID, "Email-1").click()
    self.driver.find_element(By.ID, "Email-1").send_keys("mail1@mail.com")
    self.driver.find_element(By.ID, "Textbox-3").click()
    self.driver.find_element(By.ID, "Textbox-3").send_keys("QA")

    time.sleep(3)

    dropdown = self.driver.find_element(By.ID, "Country-1")
    select = Select(dropdown)
    select.select_by_index(22)
    
    time.sleep(3)

    self.driver.find_element(By.ID, "Textbox-4").click()
    self.driver.find_element(By.ID, "Textbox-4").send_keys("142")

    self.driver.find_element(By.ID, "Textarea-1").click()
    self.driver.find_element(By.ID, "Textarea-1").send_keys("comments: empty first name field")

    self.driver.execute_script("window.scrollTo(0, 600)")
    time.sleep(2)

    self.driver.find_element(By.CSS_SELECTOR, "#form--1 > form > div > div:nth-child(13) > button").click()

    # time.sleep(2)
    WebDriverWait(self.driver, 40).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".sfError")))
    assert "First name is required" in self.driver.find_element(By.CSS_SELECTOR, ".sfError").text
 
  def test_empty_last_name_field(self):
    self.driver.find_element(By.CSS_SELECTOR, ".TK-Button--CTA-Sec").click()
    dropdown = self.driver.find_element(By.ID, "Dropdown-1")
    select = Select(dropdown)
    select.select_by_index(2)
    
    time.sleep(2)

    dropdown = self.driver.find_element(By.ID, "Dropdown-2")
    select = Select(dropdown)
    select.select_by_index(3)

    time.sleep(2)
    
    self.driver.find_element(By.ID, "Textbox-1").click()
    self.driver.find_element(By.ID, "Textbox-1").send_keys("first")
    
    # time.sleep(3)
    # self.driver.find_element(By.ID, "Textbox-2").click()
    # self.driver.find_element(By.ID, "Textbox-2").send_keys("last")

    self.driver.execute_script("window.scrollTo(0, 500)")
    time.sleep(3)

    self.driver.find_element(By.ID, "Email-1").click()
    self.driver.find_element(By.ID, "Email-1").send_keys("maail1@mail.com")
    self.driver.find_element(By.ID, "Textbox-3").click()
    self.driver.find_element(By.ID, "Textbox-3").send_keys("QA")

    self.driver.execute_script("window.scrollTo(0, 600)")
    time.sleep(3)

    dropdown = self.driver.find_element(By.ID, "Country-1")
    select = Select(dropdown)
    select.select_by_visible_text("Kuwait")
    
    time.sleep(3)
    self.driver.execute_script("window.scrollTo(0, 700)")

    self.driver.find_element(By.ID, "Textbox-4").click()
    self.driver.find_element(By.ID, "Textbox-4").send_keys("142")

    self.driver.find_element(By.ID, "Textarea-1").click()
    self.driver.find_element(By.ID, "Textarea-1").send_keys("comments: empty last name field")

    time.sleep(2)

    self.driver.find_element(By.CSS_SELECTOR, "#form--1 > form > div > div:nth-child(13) > button").click()

    time.sleep(2)

    # WebDriverWait(self.driver, 60).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "#form--1 > form > div > div.sf-fieldWrp.Required.sfErrorWrp > p")))
    assert self.driver.find_element(By.CSS_SELECTOR, ".sfError").text == "Last name is required"
  
  def test_special_characters_in_last_nameField(self):
    self.driver.find_element(By.CSS_SELECTOR, ".TK-Button--CTA-Sec").click()
    dropdown = self.driver.find_element(By.ID, "Dropdown-1")
    select = Select(dropdown)
    select.select_by_index(3)
    
    time.sleep(2)

    dropdown = self.driver.find_element(By.ID, "Dropdown-2")
    select = Select(dropdown)
    select.select_by_index(3)

    time.sleep(2)
    
    self.driver.find_element(By.ID, "Textbox-1").click()
    self.driver.find_element(By.ID, "Textbox-1").send_keys("first")
    
    time.sleep(3)
    self.driver.find_element(By.ID, "Textbox-2").click()
    self.driver.find_element(By.ID, "Textbox-2").send_keys("1 *12")

    self.driver.execute_script("window.scrollTo(0, 500)")
    time.sleep(3)

    self.driver.find_element(By.ID, "Email-1").click()
    self.driver.find_element(By.ID, "Email-1").send_keys("maail1@mail.com")
    self.driver.find_element(By.ID, "Textbox-3").click()
    self.driver.find_element(By.ID, "Textbox-3").send_keys("QA")

    self.driver.execute_script("window.scrollTo(0, 600)")
    time.sleep(3)

    dropdown = self.driver.find_element(By.ID, "Country-1")
    select = Select(dropdown)
    select.select_by_value("Hong Kong")
    
    time.sleep(3)
    self.driver.execute_script("window.scrollTo(0, 700)")

    self.driver.find_element(By.ID, "Textbox-4").click()
    self.driver.find_element(By.ID, "Textbox-4").send_keys("142")

    self.driver.find_element(By.ID, "Textarea-1").click()
    self.driver.find_element(By.ID, "Textarea-1").send_keys("comments: special characters in last name field")

    time.sleep(2)

    self.driver.find_element(By.CSS_SELECTOR, "#form--1 > form > div > div:nth-child(13) > button").click()

    time.sleep(2)

    WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR,".sfError")))
    assert "Your Last name has special characters." in self.driver.find_element(By.CSS_SELECTOR, ".sfError").text
 
  def test_empty_emailField(self):
    self.driver.find_element(By.CSS_SELECTOR, ".TK-Button--CTA-Sec").click()
    dropdown = self.driver.find_element(By.ID, "Dropdown-1")
    select = Select(dropdown)
    select.select_by_index(3)
    
    time.sleep(2)

    dropdown = self.driver.find_element(By.ID, "Dropdown-2")
    select = Select(dropdown)
    select.select_by_index(3)

    time.sleep(2)
    self.driver.find_element(By.ID, "Textbox-1").click()
    self.driver.find_element(By.ID, "Textbox-1").send_keys("first")
    time.sleep(3)
    self.driver.find_element(By.ID, "Textbox-2").click()
    self.driver.find_element(By.ID, "Textbox-2").send_keys("last")

    self.driver.execute_script("window.scrollTo(0, 500)")
    time.sleep(3)

    self.driver.find_element(By.ID, "Email-1").click()
    self.driver.find_element(By.ID, "Email-1").send_keys("")
    self.driver.find_element(By.ID, "Textbox-3").click()
    self.driver.find_element(By.ID, "Textbox-3").send_keys("QA")

    self.driver.execute_script("window.scrollTo(0, 600)")
    time.sleep(3)

    dropdown = self.driver.find_element(By.ID, "Country-1")
    select = Select(dropdown)
    select.select_by_value("Fiji")
    
    time.sleep(3)
    self.driver.execute_script("window.scrollTo(0, 700)")

    self.driver.find_element(By.ID, "Textbox-4").click()
    self.driver.find_element(By.ID, "Textbox-4").send_keys("142")

    self.driver.find_element(By.ID, "Textarea-1").click()
    self.driver.find_element(By.ID, "Textarea-1").send_keys("comments: empty email address field")

    time.sleep(2)

    self.driver.find_element(By.CSS_SELECTOR, "#form--1 > form > div > div:nth-child(13) > button").click()

    time.sleep(2)

    WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".sfError")))
    assert "Email address is required" in self.driver.find_element(By.CSS_SELECTOR, ".sfError").text

  def test_invalid_email_address(self):
    self.driver.find_element(By.CSS_SELECTOR, ".TK-Button--CTA-Sec").click()
    dropdown = self.driver.find_element(By.ID, "Dropdown-1")
    select = Select(dropdown)
    select.select_by_index(3)
    
    time.sleep(2)

    dropdown = self.driver.find_element(By.ID, "Dropdown-2")
    select = Select(dropdown)
    select.select_by_index(3)

    time.sleep(2)

    self.driver.find_element(By.ID, "Textbox-1").click()
    self.driver.find_element(By.ID, "Textbox-1").send_keys("first")
    time.sleep(3)
    self.driver.find_element(By.ID, "Textbox-2").click()
    self.driver.find_element(By.ID, "Textbox-2").send_keys("last")

    self.driver.execute_script("window.scrollTo(0, 500)")
    time.sleep(3)

    self.driver.find_element(By.ID, "Email-1").click()
    self.driver.find_element(By.ID, "Email-1").send_keys("email@home")
    self.driver.find_element(By.ID, "Textbox-3").click()
    self.driver.find_element(By.ID, "Textbox-3").send_keys("QA")

    self.driver.execute_script("window.scrollTo(0, 600)")
    time.sleep(3)

    dropdown = self.driver.find_element(By.ID, "Country-1")
    select = Select(dropdown)
    select.select_by_visible_text("Egypt")
    
    time.sleep(3)
    self.driver.execute_script("window.scrollTo(0, 700)")

    self.driver.find_element(By.ID, "Textbox-4").click()
    self.driver.find_element(By.ID, "Textbox-4").send_keys("142")

    self.driver.find_element(By.ID, "Textarea-1").click()
    self.driver.find_element(By.ID, "Textarea-1").send_keys("comments: email@home")

    time.sleep(2)

    self.driver.find_element(By.CSS_SELECTOR, "#form--1 > form > div > div:nth-child(13) > button").click()

    time.sleep(2)

    WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "#form--1 > form > div > div.sf-fieldWrp.Required.sfErrorWrp > p")))
    assert "Email address is invalid" in self.driver.find_element(By.CSS_SELECTOR, "#form--1 > form > div > div.sf-fieldWrp.Required.sfErrorWrp > p").text

  def test_tooltip_phoneField(self):
    self.driver.find_element(By.CSS_SELECTOR, ".TK-Button--CTA-Sec").click() 
    
    self.driver.execute_script("window.scrollTo(0, 600)")
    time.sleep(3)

    element = self.driver.find_element(By.CSS_SELECTOR, "#form--1 > form > div > div:nth-child(9) > label > span")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    
    time.sleep(2)

    tooltip_locator = (By.CSS_SELECTOR, "#form--1 > form > div > div:nth-child(9) > label > span > span")
    tooltip_element = WebDriverWait(self.driver, 35).until(
    EC.visibility_of_element_located(tooltip_locator))

    tooltip_text = tooltip_element.text

    assert tooltip_text == "For an even faster response, please leave your telephone number." 

  def test_empty_phone_field(self):
    """input include only "international dialog code" """
    
    self.driver.find_element(By.CSS_SELECTOR, ".TK-Button--CTA-Sec").click()
    dropdown = self.driver.find_element(By.ID, "Dropdown-1")
    select = Select(dropdown)
    select.select_by_index(3)
    
    time.sleep(2)

    dropdown = self.driver.find_element(By.ID, "Dropdown-2")
    select = Select(dropdown)
    select.select_by_index(3)

    time.sleep(2)

    self.driver.find_element(By.ID, "Textbox-1").click()
    self.driver.find_element(By.ID, "Textbox-1").send_keys("first")
    time.sleep(3)
    self.driver.find_element(By.ID, "Textbox-2").click()
    self.driver.find_element(By.ID, "Textbox-2").send_keys("last")

    self.driver.execute_script("window.scrollTo(0, 500)")
    time.sleep(3)

    self.driver.find_element(By.ID, "Email-1").click()
    self.driver.find_element(By.ID, "Email-1").send_keys("email@home")
    self.driver.find_element(By.ID, "Textbox-3").click()
    self.driver.find_element(By.ID, "Textbox-3").send_keys("QA")

    self.driver.execute_script("window.scrollTo(0, 600)")
    time.sleep(3)

    dropdown = self.driver.find_element(By.ID, "Country-1")
    select = Select(dropdown)
    select.select_by_index(100)
    
    
    time.sleep(3)
    self.driver.execute_script("window.scrollTo(0, 700)")

    self.driver.find_element(By.ID, "Textbox-4").click()
    self.driver.find_element(By.ID, "Textbox-4").send_keys("")

    time.sleep(3)

    self.driver.find_element(By.ID, "Textarea-1").click()
    self.driver.find_element(By.ID, "Textarea-1").send_keys("comments: empty phone feild")

    assert "Phone is required" in  self.driver.find_element(By.CSS_SELECTOR, "#form--1 > form > div > div.sf-fieldWrp.Required.sfErrorWrp > p.sfError").text

  def test_chars_in_phone(self):
    self.driver.find_element(By.CSS_SELECTOR, ".TK-Button--CTA-Sec").click()
    dropdown = self.driver.find_element(By.ID, "Dropdown-1")
    select = Select(dropdown)
    select.select_by_index(3)
    
    time.sleep(2)

    dropdown = self.driver.find_element(By.ID, "Dropdown-2")
    select = Select(dropdown)
    select.select_by_index(3)

    time.sleep(2)

    self.driver.find_element(By.ID, "Textbox-1").click()
    self.driver.find_element(By.ID, "Textbox-1").send_keys("first")
    self.driver.find_element(By.ID, "Textbox-2").click()
    self.driver.find_element(By.ID, "Textbox-2").send_keys("last")
    self.driver.find_element(By.ID, "Email-1").click()
    self.driver.find_element(By.ID, "Email-1").send_keys("mail1@mail.com")
    self.driver.find_element(By.ID, "Textbox-3").click()
    self.driver.find_element(By.ID, "Textbox-3").send_keys("QA")

    time.sleep(3)

    dropdown = self.driver.find_element(By.ID, "Country-1")
    select = Select(dropdown)
    select.select_by_value("Isreal")
    
    self.driver.find_element(By.ID, "Textbox-4").click()
    self.driver.find_element(By.ID, "Textbox-4").send_keys("abc12+/3")

    self.driver.find_element(By.ID, "Textarea-1").click()
    self.driver.find_element(By.ID, "Textarea-1").send_keys("Chars and speciel characters in phone number")

    self.driver.find_element(By.CSS_SELECTOR, "#form--1 > form > div > div:nth-child(13) > button").click()

    time.sleep(5)

    assert "Invalid phone number" in  self.driver.find_element(By.CSS_SELECTOR, ".sfError").text

