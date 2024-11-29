import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestAnchors:
    def setup_method(self, method):
        #self.driver = webdriver.Chrome()
        self.driver = webdriver.Edge()

        self.driver.get("https://www.telerik.com/")
        self.driver.maximize_window()
        self.driver
  
    def teardown_method(self, method):
        self.driver.quit()
    
    def test_anchor1(self):
        self.driver.get("https://www.telerik.com/")
        self.driver.maximize_window()
        self.driver.find_element(By.CSS_SELECTOR,"#js-tlrk-nav-drawer > ul.TK-Context-Menu.TK-Menu > li:nth-child(1) > a").click()
        anchor_tags = self.driver.find_element(By.CSS_SELECTOR, "#ContentPlaceholder1_T53129E6C012_Col00 > nav > div > div:nth-child(2) > a:nth-child(1)")
                                                            
        href = anchor_tags.get_attribute("href")
        text = anchor_tags.text
        
        # Optionally, check if the href is valid      
        assert href is not None, f"Anchor '{text}' does not have a valid href!"

    def test_anchor2(self):
        self.driver.get("https://www.telerik.com/")
        self.driver.maximize_window()
        
        self.driver.implicitly_wait(5)

        self.driver.find_element(By.CSS_SELECTOR,"#js-tlrk-nav-drawer > ul.TK-Context-Menu.TK-Menu > li:nth-child(1) > a").click()        
        
        self.driver.implicitly_wait(5)

        anchor_tags = self.driver.find_element(By.CSS_SELECTOR, "#ContentPlaceholder1_T53129E6C012_Col00 > nav > div > div:nth-child(2) > a:nth-child(2)")

        href = anchor_tags.get_attribute("href")
        text = anchor_tags.text
        print(f"Anchor Text: {text}, Href: {href}")
        
        # Optionally, check if the href is valid
        assert href is not None, f"Anchor '{text}' does not have a valid href!"

    def test_anchor3(self):
        self.driver.get("https://www.telerik.com/")
        self.driver.maximize_window()

        self.driver.implicitly_wait(5)

        self.driver.find_element(By.CSS_SELECTOR,"#js-tlrk-nav-drawer > ul.TK-Context-Menu.TK-Menu > li:nth-child(1) > a").click()        

        self.driver.implicitly_wait(5)

        anchor_tags = self.driver.find_element(By.CSS_SELECTOR, "#ContentPlaceholder1_T53129E6C012_Col00 > nav > div > div:nth-child(2) > a:nth-child(3)")

        href = anchor_tags.get_attribute("href")
        text = anchor_tags.text
        print(f"Anchor Text: {text}, Href: {href}")

        # Optionally, check if the href is valid
        assert href is not None, f"Anchor '{text}' does not have a valid href!" 
  
    def test_anchor4(self):
        self.driver.get("https://www.telerik.com/")
        self.driver.maximize_window()

        self.driver.implicitly_wait(5)

        self.driver.find_element(By.CSS_SELECTOR,"#js-tlrk-nav-drawer > ul.TK-Context-Menu.TK-Menu > li:nth-child(1) > a").click()        

        self.driver.implicitly_wait(5)

        anchor_tags = self.driver.find_element(By.CSS_SELECTOR, "#ContentPlaceholder1_T53129E6C012_Col00 > nav > div > div:nth-child(2) > a:nth-child(4)")

        href = anchor_tags.get_attribute("href")
        text = anchor_tags.text

        assert href is not None, f"Anchor '{text}' does not have a valid href!" 

    def test_anchor5(self):
        self.driver.get("https://www.telerik.com/")
        self.driver.maximize_window()

        self.driver.implicitly_wait(5)

        self.driver.find_element(By.CSS_SELECTOR,"#js-tlrk-nav-drawer > ul.TK-Context-Menu.TK-Menu > li:nth-child(1) > a").click()        

        self.driver.implicitly_wait(5)

        anchor_tags = self.driver.find_element(By.CSS_SELECTOR, "#ContentPlaceholder1_T53129E6C012_Col00 > nav > div > div:nth-child(2) > a:nth-child(5)")

        href = anchor_tags.get_attribute("href")
        text = anchor_tags.text

        assert href is not None, f"Anchor '{text}' does not have a valid href!" 

    def test_anchor6(self):
        self.driver.get("https://www.telerik.com/")
        self.driver.maximize_window()

        self.driver.implicitly_wait(5)

        self.driver.find_element(By.CSS_SELECTOR,"#js-tlrk-nav-drawer > ul.TK-Context-Menu.TK-Menu > li:nth-child(1) > a").click()        

        self.driver.implicitly_wait(5)

        anchor_tags = self.driver.find_element(By.XPATH, '//*[@id="ContentPlaceholder1_T53129E6C012_Col00"]/nav/div/div[2]/a[6]')

        href = anchor_tags.get_attribute("href")
        text = anchor_tags.text

        assert href is not None, f"Anchor '{text}' does not have a valid href!" 

    def test_anchor7(self):
        self.driver.get("https://www.telerik.com/")
        self.driver.maximize_window()

        self.driver.implicitly_wait(5)

        self.driver.find_element(By.CSS_SELECTOR,"#js-tlrk-nav-drawer > ul.TK-Context-Menu.TK-Menu > li:nth-child(1) > a").click()        

        self.driver.implicitly_wait(5)

        anchor_tags = self.driver.find_element(By.CSS_SELECTOR, '#ContentPlaceholder1_T53129E6C012_Col00 > nav > div > div:nth-child(2) > a:nth-child(7)')

        href = anchor_tags.get_attribute("href")
        text = anchor_tags.text

        assert href is not None, f"Anchor '{text}' does not have a valid href!" 

    def test_anchor8(self):
        self.driver.get("https://www.telerik.com/")
        self.driver.maximize_window()

        self.driver.implicitly_wait(5)

        self.driver.find_element(By.CSS_SELECTOR,"#js-tlrk-nav-drawer > ul.TK-Context-Menu.TK-Menu > li:nth-child(1) > a").click()        

        self.driver.implicitly_wait(5)

        anchor_tags = self.driver.find_element(By.CSS_SELECTOR, '#ContentPlaceholder1_T53129E6C012_Col00 > nav > div > div:nth-child(2) > a:nth-child(8)')

        href = anchor_tags.get_attribute("href")
        text = anchor_tags.text

        assert href is not None, f"Anchor '{text}' does not have a valid href!" 

