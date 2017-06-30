#!/usr/bin/env python3
# encoding: utf-8

import yaml


class Config(dict):
	def __init__(self, config_filename):
		self._parse(config_filename)
	
	
	def _parse(self, config_filename):
		with open(config_filename) as config_file:
			config = yaml.load(config_file)
		
		self._convert_config(config)
	
	
	def _convert_config(self, config):
		for section in config:
			# section names are keys with no value
			section_name = [key for key, value in section.items() if value is None][0]
			
			del section[section_name]
			
			self[section_name] = section
