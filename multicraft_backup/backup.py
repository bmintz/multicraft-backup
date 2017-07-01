#!/usr/bin/env python3
# encoding: utf-8

import ftptool
import hashlib
import tarfile


class BackerUpper:
	def __init__(self, config):
		self._config = config
		
		self._host = ftptool.FTPHost.connect(config['ftp']['server_ip'],
			user='{email}.{id}'.format(
				email=config['login']['username'],
				id=config['server']['id_number'])
			password=config['login']['password']
		)
	
	
	def backup(self):
		"""back up the desired directory from the server.
		make sure you stop the server first!
		"""
		
		self._host.mirror_to_local(self._config['ftp']['desired_dir'], '.')
