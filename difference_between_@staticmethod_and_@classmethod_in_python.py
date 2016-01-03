"""
Difference between @staticmethod and @classmethod in Python
from zhihu: https://www.zhihu.com/question/20021164
from stack overflow:http://stackoverflow.com/questions/12179271/python-classmethod-and-staticmethod-for-beginner/12179325#12179325
"""

#example
class Kls(object):
    def _init_(self, data):
        self.data = data

    def printd(self):
        print(self.data)

    @staticmethod
    def smethod(*arg):
        print('static:', arg)

    @classmethod
    def cmethod(*arg):
        print('clase:', arg)

#classmethod before
def get_no_of_instances(cls_obj):
    return cls_obj.no_inst


class Kls(object):
    no_inst = 0
    def __init__(self):
        Kls.no_inst = Kls.no_inst + 1


ik1 = Kls()
ik2 = Kls()
print(get_no_of_instances(Kls))


#classmethod after
class Kls(object):
    no_inst = 0
    def __init__(self):
        Kls.no_inst = Kls.no_inst + 1

    @classmethod
    def get_no_of_instance(cls_obj):
        return cls_obj.no_inst


ik1 = Kls()
ik2 = Kls()
print ik1.get_no_of_instance()
print Kls.get_no_of_instance()


#staticmethod before
IND = 'ON'

def checkind():
    return (IND == 'ON')


class Kls(object):
    def __init__(self,data):
        self.data = data

    def do_reset(self):
        if checkind():
            print('Reset done for:', self.data)

    def set_db(self):
        if checkind():
            self.db = 'new db connection'
            print('DB connection made for:',self.data)


ik1 = Kls(12)
ik1.do_reset()
ik1.set_db()


#staticmethod after
IND = 'ON'
class Kls(object):
    def __init__(self, data):
        self.data = data

    @staticmethod
    def checkind():
        return (IND == 'ON')

    def do_reset(self):
        if self.checkind():
            print('Reset done for:', self.data)

    def set_db(self):
        if self.checkind():
            self.db = 'New db connection'
        print('DB connection made for: ', self.data)


ik1 = Kls(12)
ik1.do_reset()
ik1.set_db()
