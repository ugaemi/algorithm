import math
import unittest


def dev_func(progresses, speeds):
    max_day = 0
    result = [1]
    for idx, progress in enumerate(progresses):
        work = 100 - progress
        day = math.ceil(work / speeds[idx])
        if not idx:
            max_day = day
        else:
            if day <= max_day:
                result[-1] += 1
            else:
                result.append(1)
                max_day = day
    return result


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(dev_func([93, 30, 55], [1, 30, 5]), [2, 1])
        self.assertEqual(dev_func([40, 93, 30, 55, 60, 65], [60, 1, 30, 5, 10, 7]), [1, 2, 3])


if __name__ == '__main__':
    unittest.main()
