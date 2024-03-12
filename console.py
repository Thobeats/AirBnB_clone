#!/usr/bin/python3
"""
Write a program called console.py that contains the
entry point of the command interpreter:
"""

import cmd
import re
from models import storage
from models.engine.classes_ import classes


class HBNBCommand(cmd.Cmd):
    """
    This defines an interactive shell for the AirBnB project
    """

    prompt = "(hbnb) "
    file = None

    def do_EOF(self, arg):
        """Quit command to exit the program
        """
        print("")
        return True

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        return True

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass

    def do_create(self, arg):
        """
        creates an instance of the BaseModel class
        and saves it into the JSON file
        Ex: create MyModel
        """
        args = self.parse(arg)
        if args['cls_name'] is None:
            print("** class name missing **")
            return

        if self.class_not_exists(args['cls_name']):
            return

        cls = classes[args['cls_name']]
        newObj = cls()
        newObj.save()
        print(newObj.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance
        based on the class name and id
        Ex: show myModel 877
        """
        args = self.parse(arg)
        if args['cls_name'] is None:
            print("** class name missing **")
            return

        if self.class_not_exists(args['cls_name']):
            return

        if self.instance_not_given(args['inst_id']):
            return

        objects = storage.all()
        cls = classes[args['cls_name']]
        key = "{}.{}".format(cls.__name__, args['inst_id'])

        if self.instance_not_exists(key, objects):
            return

        inst = objects[key]
        print(inst)

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and
        id (save the change into the JSON file).
        Ex: $ destroy BaseModel 1234-1234-1234
        """
        args = self.parse(arg)
        if args['cls_name'] is None:
            print("** class name missing **")
            return

        if self.class_not_exists(args['cls_name']):
            return

        if self.instance_not_given(args['inst_id']):
            return

        objects = storage.all()
        cls = classes[args['cls_name']]
        key = "{}.{}".format(cls.__name__, args['inst_id'])

        if self.instance_not_exists(key, objects):
            return

        storage.delete_by_id(key)

    def do_all(self, arg):
        """
        Prints all string representation of all instances
        based or not on the class name.
        Ex: $ all BaseModel or $ all
        """
        args = self.parse(arg)
        objects = storage.all()
        allInstances = []
        if args['cls_name'] is None:
            for obj in objects.keys():
                print_list = "{}".format(objects[obj])
                allInstances.append(print_list)
        else:
            if self.class_not_exists(args['cls_name']):
                return
            else:
                for obj in objects:
                    cls = classes[args['cls_name']]
                    if obj.split(".")[0] == cls.__name__:
                        print_list = "{}".format(objects[obj])
                        allInstances.append(print_list)

        print(allInstances)

    def default(self, arg):
        """
        default behaviour of the console
        """
        argdict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "update": self.do_update,
            "count": self.do_count
        }
        dotMatch = re.search(r"\.", arg)
        if dotMatch is None:
            print("*** Unknown syntax: {}".format(arg))
            return False
        else:
            argl = [arg[:dotMatch.span()[0]], arg[dotMatch.span()[1]:]]
            match = re.search(r"\((.*?)\)", argl[1])
            if match is not None:
                command = [argl[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in argdict.keys():
                    call = "{} {}".format(argl[0], command[1])
                    return argdict[command[0]](call)
            else:
                print("*** Unknown function: {}".format(arg))
                return False

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute (save the change into the JSON file).
        Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com"
        """
        args = self.parse(arg)
        objects = storage.all()

        if args['cls_name'] is None:
            print("** class name missing **")
            return

        if self.class_not_exists(args['cls_name']):
            return

        if self.instance_not_given(args['inst_id']):
            return

        cls = classes[args['cls_name']]
        key = "{}.{}".format(cls.__name__, args['inst_id'])

        if self.instance_not_exists(key, objects):
            return

        if self.attr_not_given(args['attr_name']):
            return

        if self.attrval_not_given(args['attr_val']):
            return

        self.updateFile(key, args)

    def do_count(self, arg):
        """
        Retrieve the number of instances of a class
        """
        args = self.parse(arg)
        objects = storage.all()
        count = 0

        if args['cls_name'] is not None:
            for obj in objects.keys():
                if self.class_not_exists(args['cls_name']):
                    return
                else:
                    for obj in objects:
                        cls = classes[args['cls_name']]
                        if obj.split(".")[0] == cls.__name__:
                            count += 1
        print(count)


    def precmd(self, line):
        """
        handles the command before it is being handled
        """
        # line = line.lower()
        return line

    @staticmethod
    def parse(arg):
        """
        splits the string into different arguments
        """
        quotes = re.search(r'\"(.*?)\"', arg)
        args = {}

        if quotes is None:
            argList = arg.split()
        else:
            lexer = arg[:quotes.span()[0]].split()
            argList = [i.strip(",") for i in lexer]
            argList.append(quotes.group())

        if len(argList) >= 1:
            args['cls_name'] = argList[0]
        else:
            args['cls_name'] = None

        if len(argList) >= 2:
            args['inst_id'] = argList[1]
        else:
            args['inst_id'] = None

        if len(argList) >= 3:
            args['attr_name'] = argList[2]
        else:
            args['attr_name'] = None

        if len(argList) >= 4:
            args['attr_val'] = argList[3]
        else:
            args['attr_val'] = None

        return args

    @staticmethod
    def class_not_exists(cls):
        """
        Checks if the class exists
        """
        if cls not in classes:
            print("** class doesn't exist **")
            return True

    @staticmethod
    def instance_not_given(inst):
        """
        Checks if the instance is given
        """
        if inst is None:
            print("** instance id missing **")
            return True

    @staticmethod
    def instance_not_exists(id, obj):
        """
        Checks if the id is an instance of the class
        """
        if id not in obj.keys():
            print("** no instance found **")
            return True

    @staticmethod
    def attr_not_given(attr):
        """
        Checks if the attribute name is given
        """
        if attr is None:
            print("** attribute name missing **")
            return True

    @staticmethod
    def attrval_not_given(attrval):
        """
        Checks if the attribute val is given
        """
        if attrval is None:
            print("** value missing **")
            return True

    @staticmethod
    def attr_not_exist(inst, attr):
        """
        Checks if the attribute name of instance exists
        """
        if attr not in inst:
            print("** attribute name not found **")
            return True

    @staticmethod
    def updateFile(key, args):
        """
        update the instance with the new attribute
        value
        """
        objects = storage.all()
        objectDict = objects[key].__dict__
        objectDict[args['attr_name']] = args['attr_val'].strip('"')
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
