import unittest


def mok_exam(answers):
    j = 0
    k = 0
    pattern2 = [1, 3, 4, 5]
    pattern3 = [3, 1, 2, 4, 5]
    score = [0, 0, 0]
    result = []
    for i in range(0, len(answers)):
        if answers[i] == i % 5 + 1:
            score[0] += 1
        if i % 2 == 0:
            if answers[i] == 2:
                score[1] += 1
            if answers[i] == pattern3[j % len(pattern3)]:
                score[2] += 1
            k += 1
        else:
            if answers[i] == pattern2[k % len(pattern2) - 1]:
                score[1] += 1
            if answers[i] == pattern3[j % len(pattern3)]:
                score[2] += 1
            j += 1
    max_score = max(score)
    i = 0
    for s in score:
        if max_score == s:
            result.append(i + 1)
        i += 1
    return result


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(mok_exam([1, 2, 3, 4, 5]), [1])
        self.assertEqual(mok_exam([1, 3, 2, 4, 2]), [1, 2, 3])


if __name__ == "__main__":
    unittest.main()
