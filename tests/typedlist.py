import unittest
import sys
sys.path.insert(0, './')

from pyast.typedlist import TypedList


class BaseTypedListTestCase(unittest.TestCase):
    def test_basic(self):
        a = TypedList(types=(str,), null=True)

        a.append("foo")
        self.assertRaises(TypeError, a.append, 2)

        a.insert(1, "foo2")
        self.assertEquals(a[1], "foo2")
        self.assertRaises(TypeError, a.insert, 0, 2)

        a.extend(["foo3", "foo4"])
        self.assertEquals(len(a), 4)
        self.assertEquals(a[3], "foo4")

        self.assertRaises(TypeError, a.extend, ["foo", 2])
        a[0]='foo'
        self.assertRaises(TypeError, a.__setitem__, 0, 2)

        a[0:2] = ['foo', 'foo2']

        self.assertRaises(TypeError, a.__setitem__, slice(0, 2), ['f', 3])
   
    def test_str_value(self):
        a = TypedList(types=("ab",), null=True)

        a.append("ab")

        self.assertRaises(TypeError, a.append, "ce")

    def test_not_null(self):
        self.assertRaises(TypeError, TypedList, (str,))

        a = TypedList(str, init=["Hello"])
        self.assertEquals(len(a), 1)
        self.assertEquals(a[0], "Hello")

        self.assertRaises(TypeError, a.__delitem__, 0)
        self.assertRaises(TypeError, a.__delslice__, (0, 0))

        del a[-4:-1]
        self.assertEquals(len(a), 1)

        del a[1:]
        self.assertRaises(TypeError, a.pop, 0) 

    def test_mixed_type(self):
        a = TypedList(types=("ab", 2, "ba"), null=True)

        a.append("ab")
        a.append(2)

        self.assertRaises(TypeError, a.append, 3)
        self.assertRaises(TypeError, a.append, "cd")

        a.append("ab")
        a.append("ba")


if __name__ == '__main__':
    unittest.main()


