
import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestTitles():
  def setup_method(self, method):
    #self.driver = webdriver.Chrome()
    self.driver = webdriver.Edge()

    self.driver.get("https://www.telerik.com/")
    self.driver.maximize_window() 

  def teardown_method(self, method):
    self.driver.quit()

  
  def test_Button_TelerikDevCraft(self):
    self.driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[4]/div[1]/div[2]/div[1]/div/div/div[2]/a").click() 
    assert self.driver.title == "Telerik DevCraft - Best .NET & JavaScript UI Components"

  def test_button_kendoUI(self): 
    self.driver.find_element(By.CSS_SELECTOR, "#ContentPlaceholder1_C360_Col01 > div > div > div.col-9 > a").click()  # Replace with the actual ID of the button
    assert "Kendo UI" in self.driver.title 

  def test_button_enterprisesStandardize(self):
    self.driver.find_element(By.CSS_SELECTOR, "#ContentPlaceholder1_C346_Col00 > a").click() 
    time.sleep(7)
    assert "Enterprises Standardize" in self.driver.title 

  def test_button_allProudects(self):
    self.driver.find_element(By.CSS_SELECTOR, "#ContentPlaceholder1_C383_Col00 > a").click() 
    assert self.driver.title == "View all products | Telerik" 

  def test_button_pricing(self):  
    self.driver.find_element(By.CSS_SELECTOR, "#ContentPlaceholder1_C383_Col01 > a").click() 
    assert self.driver.title == "Purchase Telerik Software Development Tools" 

  def test_button_blogs(self): 
    self.driver.find_element(By.CSS_SELECTOR, "#ContentPlaceholder1_C416_Col00 > a").click() 
    assert self.driver.title == "Your Source for .NET & JavaScript Developer Info – Telerik Blogs" 




