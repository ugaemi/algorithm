import unittest


def sum_matrix(arr1, arr2):
    for i in range(len(arr1)):
        for j in range(len(arr1[0])):
            arr1[i][j] += arr2[i][j]
    return arr1


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sum_matrix([[1, 2], [2, 3]], [[3, 4], [5, 6]]), [[4, 6], [7, 9]])
        self.assertEqual(sum_matrix([[1], [2]], [[3], [4]]), [[4], [6]])


if __name__ == '__main__':
    unittest.main()
