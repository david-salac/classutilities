# Class utilities
Author: David Salac <https://github.com/david-salac>

Simple package with helpful utilities for classes.
That includes class level properties and filters for
configuration classes.

**Note:** this package does not require any external dependencies.

## How to install package
Use PIP command:
```
pip install classutilities
```

## How to use class level properties
Class level properties are properties defined on
class level. They behave exactly the same as
normal properties (but allow being called on
class level and not only on instance level).

Consider the following example (defining class
level properties):
```python
import classutilities

class SomeClass(classutilities.ClassPropertiesMixin):
    _some_variable = 8  # Some class variable

    @classutilities.classproperty
    def some_variable(cls):  # Example of getter
        return cls._some_variable

    @some_variable.setter
    def some_variable(cls, value):  # Example of setter
        cls._some_variable = value
```
`ClassPropertiesMixin` allows you to use a setter for
properties. However, if you only need a getter, it will
work even without this mixin.


Usage of class-level properties:
```python
# Getter:
value = SomeClass.some_variable
print(value)  # >>> 8

# Setter:
new_value = 9
SomeClass.some_variable = new_value
print(SomeClass.some_variable)  # >>> 9
print(SomeClass._some_variable)  # >>> 9
```
As you can see, class-level properties behave very
naturally.

## Configuration classes
Configuration classes usually follow standard patterns, mainly:
 - All members have to be upper case (if they do not start
   with an underscore).
 - There is no constructor in the class.
 - There is no standard (instance) method in the class. Only
   class methods and static methods are allowed.

It is beneficial to have some validator for a configuration
class that checks if all these conditions are followed.
This is precisely what ConfigClassMixin does. Consider
the following use-case:

```python
import classutilities

class SomeConfigClass(classutilities.ConfigClassMixin):
    # This is OK:
    DATABASE_HOST = "localhost"  # OK: variable name in uppercase
    DATABASE_NAME = "testing"  # OK: variable name in uppercase
    # ...
    
    # This is NOT OK (class variables must be uppercase):
    database_password = "pass"  # NO: must not be lowercase
    
    # This is OK (underscore on the beginning):
    _api_version = "1.0.0"  # OK: starts with an underscore
    
    # This is OK:
    @classmethod
    def connect_to_database(cls):  # Class methods are acceptable
        return ...
    
    # This is OK:
    @staticmethod
    def check_status():  # Static methods are acceptable
        return ...
    
    # This is NOT OK:
    def check_parameters(self):  # No instance-level methods
        return ...
```
Mixin `ConfigClassMixin` can be used together with
mixin for class-level properties. Class level properties
are also acceptable (this filter allows them).
