import unittest
import classutilities


class TestClassProperty(unittest.TestCase):
    """
    Test class properties
    """
    def test_class_level(self):
        """
        Test standard approach (property on class level)
        """
        class TestingOnClass(classutilities.ClassPropertiesMixin):
            class_var = 8  # Some class variable

            @classutilities.classproperty
            def var(cls):  # Some getter
                return cls.class_var

            @var.setter
            def var(cls, value):  # Some setter
                cls.class_var = value

        # Test getter
        self.assertEqual(TestingOnClass.var, 8)
        # Test setter
        TestingOnClass.var = 11
        self.assertEqual(TestingOnClass.var, 11)
        self.assertEqual(TestingOnClass.class_var, 11)

    def test_instance_level(self):
        """Test class properties on instance level"""
        class TestingOnClass(classutilities.ClassPropertiesMixin):
            class_var = 8  # Some class variable

            @classutilities.classproperty
            def var(cls):  # Some getter
                return cls.class_var

            @var.setter
            def var(cls, value):  # Some setter
                cls.class_var = value

        inst = TestingOnClass()
        # Test getter
        self.assertEqual(inst.var, 8)
        self.assertEqual(TestingOnClass.var, 8)
        # Test setter
        inst.var = 11
        self.assertEqual(inst.var, 11)
        self.assertEqual(inst.class_var, 11)
        self.assertEqual(TestingOnClass.var, 11)
        self.assertEqual(TestingOnClass.class_var, 11)
