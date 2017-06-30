#!/usr/bin/env python3
# encoding: utf-8

"""
server: utilities to start, and stop the server
"""

import selenium


class ServerBase:
	def __init__(self, config):
		self.browser = selenium.webdriver.Chrome()
		
		# actions should timeout after 3 seconds
		self.implicitly_wait(3)
		self.set_script_timeout(3)
		
		self._login()
	
	
	def __getattribute__(self, attribute):
		"""make all self.browser attributes appear to be self attributes"""
		
		try:
			return object.__getattribute__(self, attribute)
		except AttributeError:
			return self.browser.__getattribute__(attribute)
