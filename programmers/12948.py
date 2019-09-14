import unittest


def blind_phone_number(phone_number):
    return '*' * (len(phone_number)-4) + phone_number[-4:]


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(blind_phone_number('01033334444'), '*******4444')
        self.assertEqual(blind_phone_number('027778888'), '*****8888')


if __name__ == '__main__':
    unittest.main()
