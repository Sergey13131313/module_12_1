import unittest
import myModule


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        obj = myModule.Runner('Ivan')
        for i in range(10):
            obj.walk()
        self.assertEqual(obj.distance, 50, 'test_walk')

    def test_run(self):
        obj = myModule.Runner('Petr')
        for i in range(10):
            obj.run()
        self.assertEqual(obj.distance, 100, 'test_run')

    def test_challenge(self):
        obj1 = myModule.Runner('Ivan')
        obj2 = myModule.Runner('Petr')
        for i in range(10):
            obj1.walk()
            obj2.run()
        self.assertNotEqual(obj1.distance, obj2.distance, 'test_challenge')


if __name__ == '__main__':
    unittest.main()
