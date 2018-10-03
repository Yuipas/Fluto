class Token(object):


    def __init__(self, type, value):

        self.type = type
        self.value = value

    def __str__(self):
        """String representation of the class instance.

        Examples:
            Token(INTEGER, 3)
            Token(MUL, '*')
        """
        return 'Token({type}, {value})'.format(type = self.type, value = repr(self.value))

    __repr__ = __str__
