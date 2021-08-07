import unittest


def phone_number_list(phone_book):
    phone_book = sorted(phone_book)
    for i, j in zip(phone_book, phone_book[1:]):
        if j.startswith(i):
            return False
    return True


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(phone_number_list(["119", "97674223", "1195524421"]), False)
        self.assertEqual(phone_number_list(["123", "456", "789"]), True)
        self.assertEqual(phone_number_list(["12", "123", "1235", "567", "88"]), False)


if __name__ == '__main__':
    unittest.main()
