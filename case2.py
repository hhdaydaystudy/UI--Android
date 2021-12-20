import unittest
import selenium
import time
from appium import webdriver
import huadong


class MyTestCase2(unittest.TestCase):

    def setUp(self):
        # super().setUp()
        print('selenium version = ', selenium.__version__)
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '9'
        desired_caps['deviceName'] = '16a3c4b7'
        desired_caps['appPackage'] = 'com.ss.android.article.news'
        desired_caps["noReset"] = True
        desired_caps['appActivity'] = 'com.ss.android.article.news.activity.MainActivity'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def testQQLogin(self):
        time.sleep(2)
        #截图
        self.driver.get_screenshot_as_file("/Users/lihu/Downloads/Android-UI-automation/jietu/test_01.png")
        time.sleep(2)
        #滑动
        huadong.swipeUp(self.driver)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    # 构造测试集  defaultTestLoader（）即TestLoader（）测试用例加载器，包括多个加载测试用例的方法，返回一个测试套件
    # loadTestsFromTestCase（）根据给定的测试类，获取其中的所有测试方法，并返回一个测试套件
    suite = unittest.TestLoader().loadTestsFromTestCase(MyTestCase2)

    # unittest框架的TextTestRunner（）类，通过该类下面的run（）方法来运行suite所组装的测试用例，入参为suite测试套件
    unittest.TextTestRunner(verbosity=2).run(suite)
    #unittest.main()