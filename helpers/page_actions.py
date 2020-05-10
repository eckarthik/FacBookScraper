from . import page_elements
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .DictToDot import DotDict

class FacebookActions:
    def __init__(self,driver):
        #Take the driver object
        self.driver = driver
        self.page_elements = DotDict(page_elements.elements)

    def find_element(self,locator):
        """Locate the element based on whether it is by XPATH or by CSS_SELECTOR"""

        return self.driver.find_element(locator[0],locator[1])

    def find_elements(self,locator):
        """Locate the element based on whether it is by XPATH or by CSS_SELECTOR"""

        return self.driver.find_elements(locator[0],locator[1])

    def login_to_facebook(self,username,password):
        """Enter the username and password and login to facebook"""

        self.driver.get("http://m.facebook.com")
        self.find_element(self.page_elements.login_username).send_keys(username)
        self.find_element(self.page_elements.login_password).send_keys(password)
        self.find_element(self.page_elements.login_button).click()

    def navigate_to_group(self,group_link):
        """Navigates to the group provided"""

        self.driver.get(group_link)
        #wait until the page is loaded and "Write Something" is visible
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(self.page_elements.write_something_group))

    def get_posts(self):
        """Get all the posts in the page"""

        return self.driver.find_elements(self.page_elements.posts[0], self.page_elements.posts[1])

    def open_post(self,post_url):
        """Opens a particular post"""

        self.driver.get(post_url)
        #Wait for the post to be loaded
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(self.page_elements.full_post_container))

    def get_post_content(self):
        """Returns the content of the post"""

        return self.find_element(self.page_elements.post_content).text

    def get_post_owner_name(self):
        """Gets the name of the person who made the post"""

        return self.find_element(self.page_elements.posted_by).text

    def get_post_reactions_count(self):
        """Returns the post reactions count - ALl reactions combined together"""

        return self.find_element(self.page_elements.post_reactions_count).text

    def get_post_reactions_order(self):
        """Returns the order of the reaction emojis"""

        reactions = self.find_elements(self.page_elements.reactions_order)
        return [reaction.get_attribute('innerText') for reaction in reactions]

    def scroll_to_end(self):
        """Scroll to the end of the page to load more posts"""

        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")

