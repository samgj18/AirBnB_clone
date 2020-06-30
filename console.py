#!/usr/bin/python3
"""
This module contains the command interpeter
for managing Airbnb files
"""
import cmd
import models
from models.base_model import BaseModel
from datetime import datetime


class HBNBCommand(cmd.Cmd):

    intro = 'Welcome to Holberton shell. Type help or ? to list commands.\n'
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

    def do_all(self, args):
        """
        Prints all string representation of all instances
        based or not on the class name
        """
        elements = []
        objects = models.storage.all()
        if not args:
            for element in objects:
                elements.append(element)
            print(elements)
            return
        tokens = args.split()
        if tokens[0] in models.classes:
            print(objects)
        else:
            print("** class doesn't exist **")

    def do_destroy(self, args):
        """
        Deletes an instance based on the class name and id
        saves the changes into JSON file
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
                    del objects[key]
                    models.storage.save()
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

    def do_update(self, args):
        """
        Update an instance based on the class name and id by adding
        or updating attribute (save the change into the JSON file).
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
            elif len(tokens) < 3:
                print("** attribute name missing **")
                return
            elif len(tokens) < 4:
                print("** value missing **")
                return
            else:
                key = (tokens[0] + "." + tokens[1])
                try:
                    objects[key].__dict__[tokens[2]] = tokens[3]
                    objects[key].__dict__[
                        "updated_at"] = datetime.now()
                    models.storage.save()
                except KeyError:
                    print("** no instance found **")
        else:
            print("** class doesn't exist **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
