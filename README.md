# Class utilities
Author: David Salac <https://github.com/david-salac>

Simple package with helpful utilities for classes.
That includes class level properties and filters for
configuration classes.

## How to install package
Use PIP command:
```
pip install classutilities
```

## How to use class level properties
Class level properties are properties defined on
class level. They behave exactly the same as
normal properties (but allows to be called on
class level and not only on instance level).

Consider the following example (defining class
level properties):
```python
import classutilities

class SomeClass(classutilities.ClassPropertiesMixin):
    _some_variable = 8  # Some class variable

    @classutilities.classproperty
    def some_variable(cls):  # Some getter
        return cls._some_variable

    @some_variable.setter
    def some_variable(cls, value):  # Some setter
        cls._some_variable = value
```
`ClassPropertiesMixin` allows you to use a setter for
properties, if you only need a getter, it will work even
without this mixin.


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
