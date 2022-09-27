import time
import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class TestURLs(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def tearDown(self):
        self.driver.close()

    def test_add_new_post(self):
        """ Tests if the new post page saves a Post object to the
            database
            1. Log the user in
            2. Go to the new_post page
            3. Fill out the fields and submit the form
            4. Go to the blog home page and verify that the post is
               on the page
        """
        # login
        self.driver.get("http://localhost:5000/auth/login")

        username_field = self.driver.find_element("name", "username")
        username_field.send_keys("teste")
        password_field = self.driver.find_element("name", "password")
        password_field.send_keys("teste")
        login_button = self.driver.find_element("id", "login_button")
        login_button.click()

        # fill out the form
        self.driver.get("http://localhost:5000/blog/new")
        title_field = self.driver.find_element("name", "title")
        title_field.send_keys("Test Title")

        # Locate the CKEditor iframe

        basic_page_body_xpath = "//div[contains(@id, 'cke_1_contents')]/iframe"
        ckeditor_frame = self.driver.find_element("xpath", basic_page_body_xpath)

        # Switch to iframe
        self.driver.switch_to.frame(ckeditor_frame)
        editor_body = self.driver.find_element("xpath", "//body")
        editor_body.send_keys("Test content")
        self.driver.switch_to.default_content()
        post_button = self.driver.find_element("id", "new_post_button")
        post_button.click()
        time.sleep(3)
        # verify the post was created
        self.driver.get("http://localhost:5000/blog")
        self.assertIn("Test Title", self.driver.page_source)
        self.assertIn("Test content", self.driver.page_source)


if __name__ == "__main__":
    unittest.main()
