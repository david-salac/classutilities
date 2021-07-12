import unittest
import classutilities


class TestClassProperty(unittest.TestCase):
    """
    Test configuration class restrictions
    """
    def test_config_class(self):
        class ConfigClass(classutilities.ConfigClassMixin):
            X = 8
            Y: str = "sfsd"

            @classmethod
            def some_class_method(cls):
                pass

            @staticmethod
            def some_static_method():
                pass

        with self.assertRaises(RuntimeError):
            # Configuration class cannot be instantiated
            ConfigClass()

        with self.assertRaises(RuntimeError):
            # Only upper case vars
            class ConfigClass_upper(classutilities.ConfigClassMixin):
                X = 8
                lowercase: str = "sfsd"

        with self.assertRaises(RuntimeError):
            # No instance methods are allowed
            class ConfigClass_instance(classutilities.ConfigClassMixin):
                X = 8

                def some_instance_method(self):
                    pass
