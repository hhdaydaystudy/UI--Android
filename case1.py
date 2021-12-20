import unittest
import selenium
import time
from appium import webdriver

class MyTestCase1(unittest.TestCase):

    def setUp(self):
        # super().setUp()
        #print('selenium version = ', selenium.__version__)
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

        def swipeUp(driver, t=1000, n=3):
            '''向上滑动屏幕'''
            l = driver.get_window_size()
            x1 = l['width'] * 0.5  # x坐标
            y1 = l['height'] * 0.75  # 起始y坐标
            y2 = l['height'] * 0.25  # 终点y坐标
            for i in range(n):
                driver.swipe(x1, y1, x1, y2, t)
        swipeUp(self.driver)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    # 构造测试集  defaultTestLoader（）即TestLoader（）测试用例加载器，包括多个加载测试用例的方法，返回一个测试套件
    # loadTestsFromTestCase（）根据给定的测试类，获取其中的所有测试方法，并返回一个测试套件
    suite = unittest.TestLoader().loadTestsFromTestCase(MyTestCase1)

    # unittest框架的TextTestRunner（）类，通过该类下面的run（）方法来运行suite所组装的测试用例，入参为suite测试套件
    unittest.TextTestRunner(verbosity=2).run(suite)
    #unittest.main()