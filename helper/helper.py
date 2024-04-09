import os
import re

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from utils.logger import LoggerInitializer

load_dotenv()


class Helper:
    def __init__(self):
        self.logging = LoggerInitializer.init_loggers("Helper")

    @staticmethod
    def clean_data_from_string(content):
        """
        Cleans and combines a list of text elements into a single string.

        Args:
            content (str): A list of text elements to be cleaned and combined.

        Returns:
            str: Combined and cleaned text from the list of elements.
        """
        return content.replace('\\n', '').replace('\n', '').replace('\xa0', '').replace('\t', '').replace("  ",
                                                                                                          ' ').strip() if content else ''

    def scrap_element_attribute_list(self, element, by, locator, attribute):
        """
        Scrapes a specific attribute from a list of elements and returns a list of attribute values.

        Args:
            element: The parent element within which to locate elements.
            by: The locating strategy to be used.
            locator: The locator expression to find elements.
            attribute: The attribute name to be scraped from elements.

        Returns:
            list: A list of attribute values scraped from the elements.
        """
        try:
            element = WebDriverWait(element, 5).until(EC.visibility_of_all_elements_located((by, locator)))
            elements_list = [ele.get_attribute(attribute) for ele in element]
            return elements_list or None
        except Exception as e:
            self.logging.info(f"Error while locating element or fetching attribute: {e}")

    def scrap_element_attribute_string(self, element, by, locator, attribute):
        """
        Scrapes a specific attribute from an element and returns its value.

        Args:
            element: The parent element within which to locate the element.
            by: The locating strategy to be used.
            locator: The locator expression to find the element.
            attribute: The attribute name to be scraped from the element.

        Returns:
            str: The attribute value scraped from the element.
        """
        try:
            element = WebDriverWait(element, 5).until(EC.visibility_of_all_elements_located((by, locator)))
            elements_list = [ele.get_attribute(attribute) for ele in element]

            return ','.join(elements_list).strip() if elements_list else None
        except Exception as e:
            self.logging.info(f"Error while locating element or fetching attribute: {e}")

    def scrap_element_object(self, element, by, locator):
        """
        Locates and returns an element based on the provided locating strategy and expression.

        Args:
            element: The parent element within which to locate the element.
            by: The locating strategy to be used.
            locator: The locator expression to find the element.

        Returns:
            obj: The located element or None if not found.
        """
        try:
            element = WebDriverWait(element, 10).until(EC.visibility_of_all_elements_located((by, locator)))
            if len(element) == 1:
                return element[0]
            else:
                return element
        except Exception as e:
            self.logging.info(f"Error while locating element or fetching attribute: {e}")

    def click_button_exception(self, element, browser):
        """
        Clicks a button element using JavaScript and handles exceptions.

        Args:
            element: The element to be clicked.
            browser: The browser instance.

        Returns:
            None
        """
        if element:
            try:
                clickable_element = WebDriverWait(browser, 10).until(EC.element_to_be_clickable(element))
                browser.execute_script("arguments[0].click();", clickable_element)
            except Exception as e:
                self.logging.info(f"Error while locating element or fetching attribute: {e}")

    @staticmethod
    def scroll(browser):
        """
        Scrolls the web page to the middle position.

        Args:
            browser: The browser instance.

        Returns:
            None
        """
        window_height = browser.execute_script("return window.innerHeight;")
        middle_position = window_height / 2  # change as per your requirement
        browser.execute_script(f"window.scrollTo(0, {middle_position});")

    @staticmethod
    def regex_email(job_description):
        email_pattern = r"[\w\.-]+@[\w\.-]+"
        try:
            email_match = re.search(email_pattern, job_description).group()
        except Exception:
            email_match = ""
        return email_match

    @staticmethod
    def regex_mobile_number(string):
        """
        Regex for mobile number

        Args:
            string (str): String

        Returns:
            str: Mobile number
        """
        mobile_number_pattern = r"\+?\d? ?\(?(\d{3})?\)?[-.\s]?(\d{3})[-.\s]?(\d{4})"
        try:
            mobile_number_match = re.search(mobile_number_pattern, string).group()
        except Exception:
            mobile_number_match = ""
        return mobile_number_match

    @staticmethod
    def chrome_options():
        """
        chrome options for chrome driver

        Returns:
            obj: chrome options
        """
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        options.add_argument('--no-sandbox')
        options.add_argument("--headless")
        options.binary_location = os.getenv('CHROME_BINARY_LOCATION')
        options.add_argument("--disable-popup-blocking")
        return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
