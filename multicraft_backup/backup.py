#!/usr/bin/env python3
# encoding: utf-8

from ftputil import FTPHost
import hashlib
import tarfile

import os


class BackerUpper:
	def __init__(self, config, target_dir):
		self._config = config
		self._desired_dir = config['ftp']['desired_dir']
		
		self.target_dir = target_dir
		
		self._ftp = FTPHost(config['ftp']['server_ip'],
			'{email}.{id}'.format(
				email=config['login']['username'],
				id=config['server']['id_number']
			),
			config['login']['password']
		)
	
	
	def do_it_all_everything(self):
		self.backup()
		self.checksum()
		#~ self.tar_it_up()
	
	
	def backup(self):
		"""back up the desired directory from the server.
		make sure you stop the server first!
		"""
		
		# mkdir -p
		os.makedirs(
			os.path.join(self.target_dir, self._desired_dir),
			exist_ok=True,
		)
		
		os.chdir(self.target_dir)
		
		
		for dirname, _, filenames in self._ftp.walk(self._desired_dir):
			self._mkdir_safe(dirname)
			for filename in filenames:
				filename = os.path.join(dirname, filename)
				
				print('Downloading', filename)
				self._ftp.download_if_newer(filename, filename)
	
	
	
	def _mkdir_safe(self, dirname):
		try:
			os.mkdir(dirname)
		except FileExistsError:
			pass
	
	
	def checksum(self):
		"""checksum the files, and write to SHA256SUMS"""
		
		with open('SHA256SUMS', 'w') as sums:
			
			for dirname, _, filenames in os.walk(self._desired_dir):
				for filename in filenames:
					filename = os.path.join(dirname, filename)
					sums.write(self._get_checksum_line(filename) + '\n')
	
	
	def _get_checksum_line(self, filename, hash_algorithm='sha256'):
		with open(filename) as f:
			hasher = hashlib.new(hash_algorithm, f.read().encode('utf-8'))
			return '{} {}'.format(
				filename,
				hasher.hexdigest()
			)
