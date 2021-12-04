"""
    Module singleton.py contains class Singleton
"""
# pylint: disable=C0301


class Singleton(type):
    """
        Class Singleton can be used as metaclass to any other class.
        Using Singleton as meta class allows any class to create no more than one instance of class.
        It can create as many copies of this instance as needed but but every copy has access to same data.
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
