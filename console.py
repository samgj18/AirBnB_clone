#!/usr/bin/python3
"""
This module contains the command interpeter
for managing Airbnb files
"""
import cmd
import models
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    intro = 'Welcome to the Holberton shell.   Type help or ? to list commands.\n'
    prompt = '(hbnb) '

    def do_help(self, args):
        """
        Command lists all help details for each command
        """
        cmd.Cmd.do_help(self, args)

    def do_create(self, args):
        """
        Creates a new instance of BaseModel, saves it to JSON file
        and prints the id
        """
        tokens = args.split()
        if not args:
            print("** class name missing **")
            return
        if tokens[0] in models.classes:
            instance = eval(tokens[0] + "()")
            instance.save()
            print("{}".format(instance.id))
        else:
            print("** class doesn't exist **")

    def do_show(self, args):
        """
        Show string representation of an instance
        """
        tokens = args.split()
        objects = models.storage.all()
        if len(tokens) == 0:
            print("** class name missing **")
            return
        if tokens[0] in models.classes:
            if len(tokens) < 2:
                print("** instance id missing **")
                return
            else:
                key = (tokens[0] + "." + tokens[1])
                try:
                    print(objects[key])
                except KeyError:
                    print("** no instance found **")
        else:
            print("** class doesn't exist **")

    @staticmethod
    def do_quit(args):
        """
        Quit command to exit the program
        """
        quit()

    @staticmethod
    def do_EOF(args):
        """
        EOF command to exit the program
        """
        quit()

    def do_all(self, args):
        """
        Prints all string representation of all instances
        based or not on the class name
        """
        token = args.split()
        objects = models.storage.all()
        if (len(token) == 0):
            for key, value in objects.items():
                print(value)
        elif (token[0] in models.classes):
            for token[0], value in objects.items():
                print(value)
        else:
            print("** class doesn't exist **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
