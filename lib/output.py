#!/usr/bin/env python
"""
	Shepherd Output blocks
"""
import textwrap
import sys
import os
import subprocess

class Output:

	red   = "\033[91m"
	blue  = "\033[94m"
	green = "\033[92m"
	bold  = "\033[1m"
	clear = "\033[0m"

	error = bold + "==> " + red + "ERROR: "
	info  = bold + "==> " + blue + "INFO: "

	def generalHelp(self):
		print textwrap.dedent("""\
			""" + self.blue + """=======================""" + self.clear + """
			   """ + self.bold + """Shepherd's Book""" + self.clear + """
			""" + self.blue + """=======================""" + self.clear + """

			Shepherd is a search & replace tool that takes parameters from a json file and injects them into your files.
			It was built primarily for use with Docker. It enables you to build a Docker container with a default template
			for your configuration files and then easily inject the configuration into those templates at runtime.
			This enables you to run Docker containers in different environments without the need to rebuild the container
			for each environment.

			Usage:

			\t[""" + self.bold + """-h,--help""" + self.clear + """]        shows this help information
			\t[""" + self.bold + """-v,--version""" + self.clear + """]     shows the version of Python and Shepherd
			\t[""" + self.bold + """--example""" + self.clear + """]        shows example command and config
			\t[""" + self.bold + """-c,--config""" + self.clear + """]      pass the JSON config as a file path or a string

		""")
		self.exit(0)

	def versionInfo(self):
		p_version = subprocess.check_output(["python","--version"])
		v_file = open(os.path.dirname(os.path.realpath(__file__)) + "/../version")
		s_version = v_file.read()
		sys.stdout.write(p_version)
		sys.stdout.write("Shepherd " + s_version)
		self.exit(0)

	def exampleInfo(self):
		print textwrap.dedent("""\
			""" + self.blue + """=======================""" + self.clear + """
			  """ + self.bold + """Shepherd Examples""" + self.clear + """
			""" + self.blue + """=======================""" + self.clear + """

			The following example command and config file will replace 'Hello' with 'Hi' in the '/home/ubuntu/test_file.txt'
			and 'ENV1' with 'example.com' and 'ENV2' with 'test.example.com' in the file '/tmp/myfile.txt'

			""" + self.bold + """Command (config file):""" + self.clear + """
			shepherd -c /home/ubuntu/shepherd_config.json

			""" + self.bold + """Command (Environment variable):""" + self.clear + """
			# Cat your file as an environment variable or pass a direct string
			JSON=$(cat CONFIG_FILE_PATH)
			shepherd -c "${JSON}"

			""" + self.bold + """Config file:""" + self.clear + """
			{
			    "/home/ubuntu/test_file.txt": {
			        "Hello": "Hi",
			    },
			    "/tmp/myfile.txt": {
			        "ENV1": "example.com",
			        "ENV2": "test.example.com",
			    }
			}
		""")
		self.exit(0)
	
	# ERRORS
	def unknownOptionError(self):
		print self.error + "Invalid Option. To show Shepherd's Book, use the -h or --help options" + self.clear
		self.exit(1)

	def requireVar(self):
		print self.error + "[-c, --config] is required. For help, use the -h option" + self.clear
		self.exit(1)

	def fileNotFound(self, file_path):
		print self.error + "File '" + file_path + "' does not exist" + self.clear
		self.exit(1)

	def keyNotFound(self, key, file_path):
		print self.error + "Key '" + key + "' not found in file '" + file_path + "'" + self.clear
		self.exit(1)

	def invalidJson(self):
		print self.error + "Invalid JSON syntax" + self.clear
		self.exit(1)

	# INFO
	def optionsSet(self):
		print self.info + "Options set" + self.clear

	def fileSuccess(self, file_path):
		print self.info + "File '" + file_path + "' successfully configured" + self.clear

	def finalSuccess(self):
		print self.bold + "==> " + self.green + "SUCCESS: Finished configuring files" + self.clear
		self.exit(0)

	def configLoaded(self):
		print self.info + "JSON config loaded successfully" + self.clear

	def exit(self, code):
		if code > 0:
			print self.bold + "==> " + self.red + "Exiting with code " + str(code) + self.clear
		sys.exit(code)
