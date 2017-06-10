#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models.city import City
from models.amenity import Amenity
from models.state import State
from models.user import User
from models.engine.file_storage import FileStorage
from models import storage

"""module: console.py"""


class HBNBCommand(cmd.Cmd):
    """The HBNBCommand class"""

    prompt = '(hbnb) '
    file = None

    @classmethod
    def get_instanceCount(self, clsname=""):
        obj = storage.all()
        count = 0
        for k in obj.keys():
            obj_cls = (obj[k].__class__.__name__)
            if (obj_cls == clsname):
                count += 1
        return count

    def do_EOF(self, args):
        """Quit command to exit the program\n"""
        raise SystemExit

    def do_quit(self, args):
        """Quit command to exit the program\n"""
        raise SystemExit

    def do_create(self, args):
        """Creates a new instance: format - create <classname>\n"""
        if not args:
            print("** class name missing **")
        else:
            s = args.split()
            if s[0] is None:
                print("** class name missing **")
            else:
                if s[0] in classes:
                    inst = classes[s[0]]()
                    inst.save()
                    print(inst.id)
                else:
                    print("** class doesn't exist **")

    def do_show(self, args):
        """Show information of an instance: format - show <classname> <id>\n"""
        if not args:
            print("** class name missing **")
        else:
            s = args.split()

            if not s[0]:
                print("** class name missing **")
            try:
                s[1]
            except Exception:
                print("** instance id missing **")
            else:
                if s[0] in classes:
                    obj = storage.all()
                    key = str(s[0]) + '.' + str(s[1])
                    print(obj[key])
                else:
                    print("** class doesn't exist **")

    def do_destroy(self, args):
        """Destroys an instance: format - destroy <classname> <id>\n"""
        if not args:
            print("** class name missing **")
        else:
            s = args.split()
            if not s[0]:
                print("** class name missing **")
            try:
                s[1]
            except Exception:
                print("** instance id missing **")
            else:
                if s[0] in classes:
                    obj = storage.all()
                    key = str(s[0]) + '.' + str(s[1])
                    del obj[key]
                    storage.save()
                else:
                    print("** class doesn't exist **")

    def do_all(self, args):
        """Prints all instances in str format based on classname or not:\nformat(1) - all\nformat(2) all <classname>\n"""
        s = args.split()
        obj = storage.all()
        try:
            s[0]
            for k in obj.keys():
                obj_cls = (obj[k].__class__.__name__)
                if (obj_cls == s[0]):
                    print(obj[k])
        except:
            for k in obj.keys():
                print(obj[k])

    def do_update(self, args):
        """Updates the key/value pair of an instance\nformat - update <class> <id> <key> <value>\n"""
        if not args:
            print("** class name missing **")
        else:
            s = args.split()
            if not s[0]:
                print("** class name missing **")
            try:
                s[1]
            except Exception:
                print("** instance id missing **")
            else:
                if s[0] in classes:
                    obj = storage.all()
                    key = str(s[0]) + '.' + str(s[1])
                    if hasattr(obj[key], s[2]):
                        setattr(obj[key], s[2], s[3])
                        storage.save()
                    else:
                        print("** attribute doesn't exist **")
                else:
                    print("** class doesn't exist **")

    def do_BaseModel(self, args):
        if args == '.all()':
            self.do_all("BaseModel")
        elif args == '.count()':
            print(self.get_instanceCount("BaseModel"))
        elif args[0:5] == '.show':
            arg = 'BaseModel' + ' ' + args[7:-2]
            self.do_show(arg)

    def do_User(self, args):
        if args == '.all()':
            self.do_all("User")
        elif args == '.count()':
            print(self.get_instanceCount("User"))
        elif args[0:5] == '.show':
            arg = 'User' + ' ' + args[7:-2]
            self.do_show(arg)

    def do_State(self, args):
        if args == '.all()':
            self.do_all("State")
        elif args == '.count()':
            print(self.get_instanceCount("State"))
        elif args[0:5] == '.show':
            arg = 'State' + ' ' + args[7:-2]
            self.do_show(arg)

    def do_City(self, args):
        if args == '.all()':
            self.do_all("City")
        elif args == '.count()':
            print(self.get_instanceCount("City"))
        elif args[0:5] == '.show':
            arg = 'State' + ' ' + args[7:-2]
            self.do_show(arg)

    def do_Place(self, args):
        if args == '.all()':
            self.do_all("Place")
        elif args == '.count()':
            print(self.get_instanceCount("Place"))
        elif args[0:5] == '.show':
            arg = 'Place' + ' ' + args[7:-2]
            self.do_show(arg)

    def do_Amenity(self, args):
        if args == '.all()':
            self.do_all("Amenity")
        elif args == '.count()':
            print(self.get_instanceCount("Amenity"))
        elif args[0:5] == '.show':
            arg = 'Amenity' + ' ' + args[7:-2]
            self.do_show(arg)

    def do_Review(self, args):
        if args == '.all()':
            self.do_all("Review")
        elif args == '.count()':
            print(self.get_instanceCount("Review"))
        elif args[0:5] == '.show':
            arg = 'Review' + ' ' + args[7:-2]
            self.do_show(arg)

    def emptyline(self):
        pass

if __name__ == '__main__':
    classes = {'BaseModel': BaseModel, 'State': State, 'City': City, 'User': User}
    HBNBCommand().cmdloop()
