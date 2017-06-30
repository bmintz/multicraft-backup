#!/usr/bin/env python3
# encoding: utf-8

"""
server: utilities to start, and stop the server
"""

import selenium
import selenium.webdriver
from selenium.webdriver.common.keys import Keys


class ServerBase:
	def __init__(self, config):
		self._config = config
		
		self.browser = selenium.webdriver.Chrome()
		
		# actions should timeout after 3 seconds
		self.implicitly_wait(3)
		self.set_script_timeout(3)
		
		self._login()
	
	
	def _login(self):
		self.get(self._config['host']['login_page'])
		
		# get the first two relevant input elements only
		username_elem, password_elem = self.find_elements_by_css_selector(
			'.row > input'
		)[:2]
		
		username_elem.send_keys(self._config['login']['username'])
		password_elem.send_keys(self._config['login']['password'])
		password_elem.send_keys(Keys.ENTER)
	
	
	
	def __getattribute__(self, attribute):
		"""make all self.browser attributes appear to be self attributes"""
		
		try:
			return object.__getattribute__(self, attribute)
		except AttributeError:
			return self.browser.__getattribute__(attribute)
