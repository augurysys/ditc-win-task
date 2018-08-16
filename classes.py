class BClass(object):
    def __repr__(self):
        return 'd'

class DClass(BClass):
    def __str__(self):
        return 'i' 

class MClass(object):
    def __repr__(self):
        return 'm' + repr(DClass()) + str(DClass()) + repr(DClass())

class ClassyClass(MClass):

    def __repr__(self):
        return super(ClassyClass, self).__repr__()