import time
import pytest
import re
from selenium import webdriver
from selenium.webdriver.common.by import By

PATH = "C:\Program Files (x86)\chromedriver.exe"                # Chromedriver path
screen_resolution = [1382, 744]                                 # px
wait_before_action = 1                                          # Increase this time if there are unxedpected errors
dell_pc_name = "Dell i7 8gb"

class Test():
  def setup_method(self, method):
    self.driver = webdriver.Chrome(PATH)
    self.vars = {}
    self._preconditions()

  def teardown_method(self, method):
    self.driver.quit()

  def _preconditions(self):
    '''
      Test preconditions
    '''
    self.let_cart_empty()

  def let_cart_empty(self):
    '''
    This function deletes all items from the cart (one by one).
    '''
    # Accessing to cart
    self.driver.get("https://www.demoblaze.com/index.html")
    self.driver.set_window_size(screen_resolution[0], screen_resolution[1])
    self.driver.find_element(By.ID, "cartur").click()
    self.driver.refresh()
    time.sleep(wait_before_action)

    # Is the cart empty?
    cart_status = self.is_cart_empty()

    if cart_status == 1: # Cart empty
      print("Cart is empty. Nothing to do. Launching test...")
    else:
      i = 1
      print("Cart is NOT empty")

      while not cart_status:
        print("Deleting item", i, "...")
        self.driver.find_element(By.XPATH, "/html/body/div[6]/div/div[1]/div/table/tbody/tr[1]/td[4]/a").click()
        time.sleep(wait_before_action)
        self.driver.refresh()
        cart_status = self.is_cart_empty()
        i += 1

  def is_cart_empty(self):
    '''
    This function evaluates whether cart empty and returns a boolean:
      0: cart is NOT empty
      1: cart is empty
    '''

    # Get current total
    time.sleep(wait_before_action)
    cart_total_str = self.driver.find_element(By.ID, "totalp").text
    if len(cart_total_str) == 0:
      cart_total = 0
    else:
      cart_total = int(cart_total_str)

    if cart_total == 0:
      return 1
    else:
      return 0

  def text_to_price(self, text):
    '''
    This function extracts the price (integer) from a given string
    '''

    price = [int(price) for price in re.findall(r'-?\d+\.?\d*', text)]
    price = price[0]

    return price

  def text_to_integers(self, text):
    '''
    This function extracts the purchase id and amount from a given text.
    Example: "Id: 5384760 Amount: 790 USD Card Number: 0123456789 Name: Marcos Bronchal Date: 18/3/2022"
    '''

    int_array = [int(int_array) for int_array in re.findall(r'-?\d+\.?\d*', text)]
    int0 = int_array[0]
    int1 = int_array[1]

    return int0, int1

  @pytest.mark.parametrize("pIter", range(5))
  def test_general(self, pIter):
    # Test name: general test
    print("Performing iteration", pIter, "...")
    # Step # | name | target | value
    # 1 | click | Go to HOME |
    self.driver.find_element(By.CSS_SELECTOR, ".active > .nav-link").click()

    # 2 | click | ilinkText=Phones|
    time.sleep(wait_before_action)
    self.driver.find_element(By.ID, "itemc").click()

    # 3 | click | linkText=Laptops |
    time.sleep(wait_before_action)
    self.driver.find_element(By.LINK_TEXT, "Laptops").click()

    # 4 | click | linkText=Monitors |
    time.sleep(wait_before_action)
    self.driver.find_element(By.LINK_TEXT, "Monitors").click()

    # 5 | click | linkText=Laptops |
    time.sleep(wait_before_action)
    self.driver.find_element(By.LINK_TEXT, "Laptops").click()

    # 6 | click | linkText=Sony vaio i5 |
    time.sleep(wait_before_action)
    self.driver.find_element(By.LINK_TEXT, "Sony vaio i5").click()

    # 7 | storeText | css=.price-container | psony_i5_price
    time.sleep(wait_before_action)
    sony_i5_price_str = self.driver.find_element(By.CSS_SELECTOR, ".price-container").text
    sony_i5_price = self.text_to_price(sony_i5_price_str)

    # 8 | click | linkText=Add to cart |
    self.driver.find_element(By.LINK_TEXT, "Add to cart").click()

    # 9 | Confirm alert
    time.sleep(wait_before_action)
    alert_obj = self.driver.switch_to.alert
    alert_obj.accept()

    # 10 | click | css=.active > .nav-link |
    time.sleep(wait_before_action)
    self.driver.find_element(By.CSS_SELECTOR, ".active > .nav-link").click()

    # 11 | click | linkText=Laptops |
    time.sleep(wait_before_action)
    self.driver.find_element(By.LINK_TEXT, "Laptops").click()

    # 12 | click | linkText=Dell i7 8gb |
    time.sleep(wait_before_action)
    self.driver.find_element(By.LINK_TEXT, "Dell i7 8gb").click()

    # 13 | click | linkText=Add to cart |
    time.sleep(wait_before_action)
    self.driver.find_element(By.LINK_TEXT, "Add to cart").click()

    # 14 | Confirm alert
    time.sleep(wait_before_action)
    alert_obj = self.driver.switch_to.alert
    alert_obj.accept()

    # 15 | click | id=cartur |
    time.sleep(wait_before_action)
    self.driver.find_element(By.ID, "cartur").click()

    '''
    It was observed that web placed items purchased randomly in the cart (maybe it is a bug or a known behavior 
    for testing proposes). Two options were evaluated:
      1) Delete always the first item. The test would fail randomly. Several test executions would make sense
      2) Implement additional logic to delete the proper item (first or second position)
    Finally, option 2) has been implemented in combination with iteration mechanism
    '''
    # 16 | click | linkText=Delete |
    time.sleep(wait_before_action)

    item1 = self.driver.find_element(By.XPATH, "/html/body/div[6]/div/div[1]/div/table/tbody/tr[1]/td[2]").text
    item2 = self.driver.find_element(By.XPATH, "/html/body/div[6]/div/div[1]/div/table/tbody/tr[2]/td[2]").text

    if item1 == dell_pc_name:
      self.driver.find_element(By.XPATH, "/html/body/div[6]/div/div[1]/div/table/tbody/tr[1]/td[4]/a").click()
    elif item2 == dell_pc_name:
      self.driver.find_element(By.XPATH, "/html/body/div[6]/div/div[1]/div/table/tbody/tr[2]/td[4]/a").click()
    else:
      print(dell_pc_name, "item cannot be deleted because it is not in the cart")
      assert 0

    # 17 | click | css=.btn-success |
    time.sleep(wait_before_action)
    self.driver.find_element(By.CSS_SELECTOR, ".btn-success").click()

    # 18 | type | id=name | Marcos Bronchal
    time.sleep(wait_before_action)
    self.driver.find_element(By.ID, "name").send_keys("Marcos Bronchal")

    # 19 | type | id=country | Spain
    self.driver.find_element(By.ID, "country").send_keys("Spain")

    # 20 | type | id=city | Zaragoza
    self.driver.find_element(By.ID, "city").send_keys("Zaragoza")

    # 21 | type | id=card | 0123456789
    self.driver.find_element(By.ID, "card").send_keys("0123456789")

    # 22 | type | id=month | 11
    self.driver.find_element(By.ID, "month").send_keys("11")

    # 23 | type | id=year | 22
    self.driver.find_element(By.ID, "year").send_keys("22")

    # 24 | click | css=#orderModal .btn-primary |
    self.driver.find_element(By.CSS_SELECTOR, "#orderModal .btn-primary").click()

    # 25 | storeText | css=.lead | purchase_amount
    time.sleep(wait_before_action)
    purchase_details = self.driver.find_element(By.CSS_SELECTOR, ".lead").text
    [purchase_id, purchase_amount] = self.text_to_integers(purchase_details)
    print("Your ID purchase is", purchase_id, ". Amount: ", purchase_amount)

    ################################################################################
    # EXPECTATION - Purchase amount equals expected
    ################################################################################
    assert purchase_amount == sony_i5_price

    # 26 | click | css=.confirm |
    self.driver.find_element(By.CSS_SELECTOR, ".confirm").click()