import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestLemonChallengesgrimmerCheckoutTest():
  def setup_method(self, method):
    self.driver = webdriver.Remote(command_executor='https://demo.testim.io/', desired_capabilities=DesiredCapabilities.CHROME)
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_lemonChallengesgrimmerCheckoutTest(self):
    # Test name: Lemon_Challenge_sgrimmer_CheckoutTest
    # Step # | name | target | value
    # 1 | open | / | 
    self.driver.get("https://demo.testim.io/")
    # 2 | setWindowSize | 1936x1048 | 
    self.driver.set_window_size(1936, 1048)
    # 3 | mouseOver | css=.theme__card___2nWQb:nth-child(1) .theme__button___1iKuo | 
    element = self.driver.find_element(By.CSS_SELECTOR, ".theme__card___2nWQb:nth-child(1) .theme__button___1iKuo")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 4 | click | css=.theme__card___2nWQb:nth-child(1) .theme__button___1iKuo | 
    self.driver.find_element(By.CSS_SELECTOR, ".theme__card___2nWQb:nth-child(1) .theme__button___1iKuo").click()
    # 5 | mouseOut | css=.theme__cardActions___1aHjq:nth-child(5) > .theme__button___1iKuo | 
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    # 6 | click | css=.CustomerInfo__input___eFffe:nth-child(1) > .theme__inputElement___27dyY | 
    self.driver.find_element(By.CSS_SELECTOR, ".CustomerInfo__input___eFffe:nth-child(1) > .theme__inputElement___27dyY").click()
    # 7 | type | css=.CustomerInfo__input___eFffe > .theme__filled___1UI7Z | Sofia
    self.driver.find_element(By.CSS_SELECTOR, ".CustomerInfo__input___eFffe > .theme__filled___1UI7Z").send_keys("Sofia")
    # 8 | type | css=.CustomerInfo__input___eFffe:nth-child(2) > .theme__inputElement___27dyY | sofiagrimmer01@gmail.com
    self.driver.find_element(By.CSS_SELECTOR, ".CustomerInfo__input___eFffe:nth-child(2) > .theme__inputElement___27dyY").send_keys("sofiagrimmer01@gmail.com")
    # 9 | click | css=.theme__input___qUQeP:nth-child(3) > .theme__inputElement___27dyY | 
    self.driver.find_element(By.CSS_SELECTOR, ".theme__input___qUQeP:nth-child(3) > .theme__inputElement___27dyY").click()
    # 10 | click | css=.theme__input___qUQeP:nth-child(3) > .theme__inputElement___27dyY | 
    self.driver.find_element(By.CSS_SELECTOR, ".theme__input___qUQeP:nth-child(3) > .theme__inputElement___27dyY").click()
    # 11 | click | css=.theme__input___qUQeP:nth-child(3) > .theme__inputElement___27dyY | 
    self.driver.find_element(By.CSS_SELECTOR, ".theme__input___qUQeP:nth-child(3) > .theme__inputElement___27dyY").click()
    # 12 | type | css=.theme__input___qUQeP:nth-child(3) > .theme__inputElement___27dyY | 253-03-0001
    self.driver.find_element(By.CSS_SELECTOR, ".theme__input___qUQeP:nth-child(3) > .theme__inputElement___27dyY").send_keys("253-03-0001")
    # 13 | click | css=.theme__input___qUQeP:nth-child(4) > .theme__inputElement___27dyY | 
    self.driver.find_element(By.CSS_SELECTOR, ".theme__input___qUQeP:nth-child(4) > .theme__inputElement___27dyY").click()
    # 14 | type | css=.theme__input___qUQeP:nth-child(4) > .theme__inputElement___27dyY | 541123879330
    self.driver.find_element(By.CSS_SELECTOR, ".theme__input___qUQeP:nth-child(4) > .theme__inputElement___27dyY").send_keys("541123879330")
    # 15 | click | css=.CustomerInfo__dropzone-label___AXLFz | 
    self.driver.find_element(By.CSS_SELECTOR, ".CustomerInfo__dropzone-label___AXLFz").click()
    # 16 | type | css=input:nth-child(2) | C:\fakepath\image (60).png
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(2)").send_keys("C:\\fakepath\\image (60).png")
    # 17 | click | css=.theme__check___2B20W | 
    self.driver.find_element(By.CSS_SELECTOR, ".theme__check___2B20W").click()
    # 18 | click | css=.flexboxgrid__row___1y_mg:nth-child(8) > .flexboxgrid__col-xs___1ROHR | 
    self.driver.find_element(By.CSS_SELECTOR, ".flexboxgrid__row___1y_mg:nth-child(8) > .flexboxgrid__col-xs___1ROHR").click()
  
