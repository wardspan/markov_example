import unittest

import mc


class TestMarkov(unittest.TestCase):
    def test_predict(self):
        m = mc.Markov('xyz')
        res = m.predict('y')
        self.assertEqual(res, 'z')

    def test_predict2(self):
        m= mc.Markov('xyz', size=2)
        res = m.predict('xy')
        self.assertEqual(res, 'z')

    def test_get_table(self):
        res = mc.get_table('ab')
        self.assertEqual(res, {'a': {'b': 1}})
    
    def test_get_table2(self):
        res = mc.get_table('abacab')
        self.assertEqual(res, {'a': {'b': 2, 'c': 1}, 'b': {'a': 1}, 'c': {'a': 1}})

    def test_get_table3(self):
        res = mc.get_table('abc', size=2)
        self.assertEqual(res, {'ab': {'c': 1}})

if __name__ == '__main__':
    print("running")
    unittest.main(exit=False)
else:
    print('loading')