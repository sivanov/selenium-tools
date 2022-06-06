from datetime import datetime
import time
import json
import requests
import os
import psutil
import subprocess
import sys


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC

import logging

class Selenium_tools:
    '''Extend webdriver class'''

    counter = 0

    def __init__(self, conf, argv):
        Selenium_tools.counter +=1 # count new created instances
        self.start = time.time() # global timer for all test
        self.driver = None
        self.conf = conf
        # print('args: ', args.r)
        # print('args: ', args.b)
        self.argv = argv
        logging.basicConfig(
            filename = self.conf.LOG_FILE,
            filemode = self.conf.LOG_FILEMODE,
            format = self.conf.LOG_FORMAT,
            level = logging.INFO,
        )
        self.log = logging.getLogger("root")
        # LOG prefix: 2021-11-15 11:36:19,058 - INFO - project-name/test_name.py param1 param2 : log message
        self.from_test = f'{sys.argv[0]} {sys.argv[1]} {sys.argv[2]}'
        self.log.info('__init__ - Finish')