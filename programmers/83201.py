import collections
import unittest


def solution(scores):
    GRADE_TABLE = (
        ("A", 90),
        ("B", 80),
        ("C", 70),
        ("D", 50),
        ("F", 0),
    )

    result = ""

    for i in range(len(scores)):
        score = [scores[j][i] for j in range(len(scores))]
        score_counter = list(collections.Counter(sorted(score, reverse=True)).items())
        if score_counter[0][1] == 1 and score[i] == score_counter[0][0]:
            score.remove(score[i])
        else:
            if score_counter[-1][1] == 1 and score[i] == score_counter[-1][0]:
                score.remove(score[i])
        average = sum(score) / len(score)
        for grade in GRADE_TABLE:
            if grade[1] <= average:
                result += grade[0]
                break
    return result


class Test(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(solution(
            [[100, 90, 98, 88, 65], [50, 45, 99, 85, 77], [47, 88, 95, 80, 67], [61, 57, 100, 80, 65],
             [24, 90, 94, 75, 65]]), "FBABD")
        self.assertEqual(solution([[50, 90], [50, 87]]), "DA")
        self.assertEqual(solution([[70, 49, 90], [68, 50, 38], [73, 31, 100]]), "CFD")


if __name__ == "__main__":
    unittest.main()
