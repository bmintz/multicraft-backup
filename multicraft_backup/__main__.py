#!/usr/bin/env python3
# encoding: utf-8

import multicraft_backup
from configparser import ConfigParser


def main(argv):
	try:
		cp = ConfigParser()
		cp.read('multicraft_backup.ini')
		
		server = multicraft_backup.ServerBase(cp)
		backup = multicraft_backup.BackerUpper(cp, argv[1])
		
		server.stop()
		# we only need the server to be down for the initial backup
		backup.backup()
		server.start()
		backup.post_download()
		
		# close the browser window
		server.close()
	else:
		return 0


if __name__ == '__main__': # can't see any reason why it wouldn't, but so it goes
	import sys
	
	sys.exit(main(sys.argv))
