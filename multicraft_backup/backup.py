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
