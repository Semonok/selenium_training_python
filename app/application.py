from selenium import webdriver
import random
import time
from pages.admin_panel_login_page import AdminPanelLoginPage
from pages.customer_list_page import CustomerListPage
from pages.registration_page import RegistrationPage
from pages.store_main_page import StoreMainPage
from pages.shopping_cart_page import ShoppingCartPage

class Application:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(2)
        self.registration_page = RegistrationPage(self.driver)
        self.admin_panel_login_page = AdminPanelLoginPage(self.driver)
        self.customer_list_page = CustomerListPage(self.driver)
        self.store_main_page = StoreMainPage(self.driver)
        self.shopping_cart_page = ShoppingCartPage(self.driver)

    def quit(self):
        self.driver.quit()

    def register_new_customer(self, customer):
        self.registration_page.open()
        self.registration_page.firstname_input.send_keys(customer.firstname)
        self.registration_page.lastname_input.send_keys(customer.lastname)
        self.registration_page.address1_input.send_keys(customer.address)
        self.registration_page.postcode_input.send_keys(customer.postcode)
        self.registration_page.city_input.send_keys(customer.city)
        self.registration_page.select_country(customer.country)
        self.registration_page.select_zone(customer.zone)
        self.registration_page.email_input.send_keys(customer.email)
        self.registration_page.phone_input.send_keys(customer.phone)
        self.registration_page.password_input.send_keys(customer.password)
        self.registration_page.confirmed_password_input.send_keys(customer.password)
        self.registration_page.create_account_button.click()

    def add_items_in_shopping_cart(self, quantity=1):
        self.store_main_page.open()
        self.store_main_page.open_ducks_list.click()
        for i in range(quantity):
            random.choice(self.store_main_page.duck_list).click()
            self.store_main_page.open_duck_item.click()
            try:
                self.store_main_page.select_size("Medium")
            except:
                pass
            finally:
                self.store_main_page.add_duck_in_shopping_cart.click()
                self.store_main_page.wait_add_item_in_cart(i)

    def quantity_item_in_shopping_cart_on_main_page(self):
        return self.store_main_page.quantity_item_in_cart

    def remove_all_items_in_shopping_cart(self):
        self.shopping_cart_page.open()
        items = self.shopping_cart_page.item_list
        for i in range(len(items)):
            i_price = self.shopping_cart_page.item_price.text
            subtotal_price = self.shopping_cart_page.subtotal_price_of_all_items.text
            self.shopping_cart_page.remove_item.click()
            if i != len(items) - 1:
                self.shopping_cart_page.change_subtotal_price(subtotal_price, i_price)
            else:
                break

    def text_when_shopping_cart_list_is_empty(self):
        return self.shopping_cart_page.text_when_list_is_empty

    def get_customer_ids(self):
        if self.admin_panel_login_page.open().is_on_this_page():
            self.admin_panel_login_page.enter_username("admin").enter_password("admin").submit_login()
        return self.customer_list_page.open().get_customer_ids()