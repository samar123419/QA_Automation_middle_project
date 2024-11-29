import pytest
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
  
  def test_demosTitle(self):
    self.driver.find_element(By.CSS_SELECTOR,"#js-tlrk-nav-drawer > ul.TK-Context-Menu.TK-Menu > li:nth-child(1) > a").click()
    assert self.driver.title == "Telerik Product Demos, Examples and Tutorials for all Telerik products"

  def test_servicesTitle(self):
    self.driver.find_element(By.CSS_SELECTOR,"#js-tlrk-nav-drawer > ul.TK-Context-Menu.TK-Menu > li:nth-child(2) > a").click()
    assert self.driver.title == "App Development, Consulting, Training and Outsourcing Services - Telerik"

  def test_blogsTitle(self): 
    self.driver.find_element(By.CSS_SELECTOR,"#js-tlrk-nav-drawer > ul.TK-Context-Menu.TK-Menu > li:nth-child(3) > a").click()
    assert self.driver.title == "Your Source for .NET & JavaScript Developer Info – Telerik Blogs"

  def test_documentationSupportTitle(self):
   self.driver.get("https://www.telerik.com/")
   self.driver.set_window_size(1536, 816)
   self.driver.find_element(By.CSS_SELECTOR,"#js-tlrk-nav-drawer > ul.TK-Context-Menu.TK-Menu > li:nth-child(4) > a").click()
   assert self.driver.title == "Support and Learning | Telerik"

  def test_pricingTitle(self):
   self.driver.find_element(By.CSS_SELECTOR,"#js-tlrk-nav-drawer > ul.TK-Context-Menu.TK-Menu > li:nth-child(5) > a").click()
   assert self.driver.title == "Purchase Telerik Software Development Tools"  

