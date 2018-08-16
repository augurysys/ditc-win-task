class BClass(object):
    def __repr__(self):
        return 'd'

class DClass(BClass):
    def __str__(self):
        return 'i' 

class MClass(object):
    def __repr__(self):
        return 'm' + str(DClass()) + repr(BClass()) +  repr(BClass())

class ClassyClass(MClass):

    def __repr__(self):
        return super(ClassyClass, self).__repr__() + 'le' 