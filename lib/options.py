#!/usr/bin/env python
"""
	Shepard Options handler
"""
import sys
import getopt
from output import Output

class Options:
	def __init__(self):
		self.out = Output()

	def setVars(self,argv):
		try:
			opts, args = getopt.getopt(argv, "hvc:", ["help","version","example","config="])
		except getopt.GetoptError:
			self.out.optError()

		for opt, arg in opts:
			if opt in ("-h","--help"):
				self.out.generalHelp()
			elif opt in ("-v","--version"):
				self.out.versionInfo()
			elif opt in ("--example"):
				self.out.exampleInfo()
			elif opt in ("-c","--config"):
				self.config = arg
			else:
				self.out.unknownOptionError()

		if not hasattr(self, 'config'):
			self.out.requireVar()

		self.out.optionsSet()
