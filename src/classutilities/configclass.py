# Impose filter on class members for configuration classes

class ConfigClassMeta(type):
    """
    Meta class that validates class variables in configuration class.
    Requirements for class variables are:
        - All has to be upper case (if they do not start with underscore)
        - There is no constructor in the class (no instance is allowed)
        - There are no standard (instance) methods in the class, only
            class methods and static methods are allowed.
    """
    def __new__(cls, name, bases, attrs):
        # Filter all class attributes (variables, methods, etc)
        #   and check if match conditions:
        for attrname, attrvalue in attrs.items():
            if callable(attrvalue):
                # Test standard (instance) methods
                raise RuntimeError(
                    f"no 'standard' method (instance level methods) are "
                    f"allowed in config class, only classmethods and "
                    f"staticmethods are allowed "
                    f"('{attrname}' is a 'standard' method).")
            if not attrname.startswith("_") \
                    and not isinstance(attrvalue, (classmethod, staticmethod)):
                if attrname != attrname.upper():
                    raise RuntimeError(
                        f"all class variable names in class {name} "
                        f"has to be upper case ('{attrname}' value is not)")
        # Create type
        new_config_class: type = type.__new__(cls, name, bases, attrs)

        # Disable class constructor (raises error if called)
        def _raise_runtime_error(*args, **kwargs):
            raise RuntimeError("configuration class cannot be instantiated")
        new_config_class.__init__ = _raise_runtime_error

        return new_config_class


class ConfigClassMixin(metaclass=ConfigClassMeta):
    """Mixin for configuration classes.
    Requirements for class members are:
        - All class fields (variables) have to be upper case (if they do
            not start with an underscore)
        - There is no constructor in the class (no instance is allowed)
        - There are no standard (instance) methods in the class, only
            class methods and static methods are allowed.
    """
    pass
