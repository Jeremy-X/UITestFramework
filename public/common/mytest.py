#coding=utf-8

import unittest
from public.common import pyselenium
from config import globalparam
from public.common.log import Log
from selenium import webdriver

class MyTest(unittest.TestCase):
    """
    The base class is for all testcase.
    """
    # def setUp(self):
    #     self.logger = Log()
    #     self.logger.info('############################### START ###############################')
    #     self.dr = pyselenium.PySelenium(globalparam.browser)
    #
    #     self.dr.max_window()
    @classmethod
    def setUpClass(cls):
        cls.logger = Log()
        cls.logger.info('############################### START ###############################')
        cls.dr = pyselenium.PySelenium(globalparam.browser)

        cls.dr.max_window()


    # def tearDown(self):
    #     self.dr.quit()
    #     self.logger.info('###############################  End  ###############################')

    @classmethod
    def tearDownClass(cls):
        cls.dr.quit()
        cls.logger.info('###############################  End  ###############################')