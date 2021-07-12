# Allows to have property on class level (and instance level)
from typing import Any, Callable


class ClassPropertyContainer(object):
    """Allows to create class level property (functionality for decorator)"""

    def __init__(self, prop_get: Any, prop_set: Any = None):
        """
        Create a container that allows to have class property decorator.
        :param prop_get: Getter.
        :param prop_set: Setter.
        """
        self.prop_get: Any = prop_get
        self.prop_set: Any = prop_set

    def __get__(self, obj: Any, cls: type = None) -> Callable:
        """
        Get the property getter.
        :param obj: Instance of class.
        :param cls: Type of class.
        :return: Class property getter
        """
        if cls is None:
            cls = type(obj)
        return self.prop_get.__get__(obj, cls)()

    def __set__(self, obj, value) -> Callable:
        """
        Get the property setter.
        :param obj: Instance of class.
        :param value: Value to be set.
        :return: Class property setter.
        """
        if not self.prop_set:
            raise AttributeError("can't set attribute")
        _type: type = type(obj)
        if _type == ClassPropertyMetaClass:
            _type = obj
        return self.prop_set.__get__(obj, _type)(value)

    def setter(self, func: Callable) -> 'ClassPropertyContainer':
        """
        Allows to create setter in a property like way.
        :param func: Getter function.
        :return: Setter object for decorator.
        """
        if not isinstance(func, (classmethod, staticmethod)):
            func = classmethod(func)
        self.prop_set = func
        return self


def classproperty(func):
    """
    Create decorator for class level property
    :param func: Function that is to be decorated
    :return: Modify method to be a class level property.
    """
    if not isinstance(func, (classmethod, staticmethod)):
        # Method has to be a classmethod
        func = classmethod(func)
    return ClassPropertyContainer(func)


class ClassPropertyMetaClass(type):
    """
    Meta class that allows setter.
    """
    def __setattr__(self, key, value):
        """Overload setter for class"""
        if key in self.__dict__:
            obj = self.__dict__.get(key)
        if obj and type(obj) is ClassPropertyContainer:
            return obj.__set__(self, value)

        return super(ClassPropertyMetaClass, self).__setattr__(key, value)


class ClassPropertiesMixin(metaclass=ClassPropertyMetaClass):
    """
    This mixin allows to use class properties setter (getter works correctly
    even without this mixin)
    """
    pass
