
from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self) -> None:
        self.browser=webdriver.Firefox()
        self.browser.implicitly_wait(3)
    def tearDown(self) -> None:
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        #伊迪丝听说有一个很酷的在线待办事宜应用
        #她去看了这个应用的首页
        self.browser.get("http://localhost:8000")
        #她注意到网页的标题和头部都包含“To-Do”这个词
        self.assertIn("To-Do",self.browser.title)
        self.fail("Finish the test")
        #应用缴请她输入一个待办事项


if __name__ == '__main__':
    unittest.main(warnings="ignore")
