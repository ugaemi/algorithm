import unittest

from collections import Counter


def incomplete_player(participant, completion):
    answer = Counter(participant) - Counter(completion)
    return list(answer.keys())[0]


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(incomplete_player(["leo", "kiki", "eden"], ["eden", "kiki"]), "leo")
        self.assertEqual(incomplete_player(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]), "vinko")
        self.assertEqual(incomplete_player(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]), "mislav")


if __name__ == '__main__':
    unittest.main()
