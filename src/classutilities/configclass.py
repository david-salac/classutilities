# Impose a filter on class members for configuration classes


class ConfigClassMeta(type):
    """
    Metaclass that validates class variables in configuration class.

    Requirements for class members are:
        - All members have to be upper case (if they do not start
        with an underscore).
        - There is no constructor in the class.
        - There is no standard (instance) method in the class. Only
        class methods and static methods are allowed.
    """

    def __new__(cls, name, bases, attrs):
        # Filter all class attributes (variables, methods, etc.)
        #   and check if match conditions:
        for attrname, attrvalue in attrs.items():
            if callable(attrvalue):
                # Test standard (instance) methods
                raise RuntimeError(
                    f"no 'standard' methods (instance-level methods) are "
                    f"allowed in the config class. Only classmethods and "
                    f"staticmethods are allowed "
                    f"('{attrname}' is a 'standard' method).")
            if not attrname.startswith("_") \
                    and not isinstance(attrvalue, (classmethod, staticmethod)):
                if attrname != attrname.upper():
                    raise RuntimeError(
                        f"all class variable names in class {name} "
                        f"must be upper case ('{attrname}' value is not)")
        # Create the new type
        new_config_class: type = type.__new__(cls, name, bases, attrs)

        # Disable class constructor (raises an error if called)
        def _raise_runtime_error(*args, **kwargs):
            raise RuntimeError("configuration class cannot be instantiated")
        new_config_class.__init__ = _raise_runtime_error

        return new_config_class


class ConfigClassMixin(metaclass=ConfigClassMeta):
    """Mixin for configuration classes.

    Requirements for class members are:
        - All members have to be upper case (if they do not start
        with an underscore).
        - There is no constructor in the class.
        - There is no standard (instance) method in the class. Only
        class methods and static methods are allowed.
    """
    pass
