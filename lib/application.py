#!/usr/bin/env python
"""
	Brain application handler class
"""
import os
import json
import fileinput
from output import Output

class Application:
	def __init__(self):
		self.out = Output()

	def configure(self, config):
		# If config is file path, load from file
		if os.path.isfile(config):
			json_data = open(config).read()
		else:
			json_data = config

		# Check JSON syntax
		try:
			data = json.loads(json_data)
		except ValueError:
			self.out.invalidJson()
		else:
			self.out.configLoaded()

		# Check files in config exist
		for (file_path, config) in data.items():
			if not os.path.isfile(file_path):
				self.out.fileNotFound(file_path)

		# Run the find and replace
		for (file_path, config) in data.items():
			f = open(file_path, 'r')
			file_data = f.read()
			f.close()

			for (key, value) in config.items():
				if file_data.find(key) == -1:
					self.out.keyNotFound(key, file_path)

			for (key, value) in config.items():
				file_data = file_data.replace(key, value)

			f = open(file_path, 'w')
			f.write(file_data)
			f.close()

			self.out.fileSuccess(file_path)

		self.out.finalSuccess()
