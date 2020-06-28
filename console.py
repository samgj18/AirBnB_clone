#!/usr/bin/python3
"""
This module contains the command interpeter
for managing Airbnb files
"""
import cmd


class HBNBCommand(cmd.Cmd):
	intro = 'Welcome to the Holberton shell.   Type help or ? to list commands.\n'
	prompt = '(hbnb) '

	def do_help(self, args):
		"""
		Command lists all help details for each command
		"""
		cmd.Cmd.do_help(self, args)

	@staticmethod
	def do_quit(*args):
		"""
		Quit command to exit the program
		"""
		quit()

	@staticmethod
	def do_EOF(*args):
		"""
		EOF command to exit the program
		"""
		quit()


if __name__ == "__main__":
	HBNBCommand().cmdloop()
