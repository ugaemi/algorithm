import unittest


def solution(table, languages, preference):
    points = {}
    for col in table:
        splitted_data = col.split()
        for lang, pref in zip(languages, preference):
            if lang in splitted_data:
                points[splitted_data[0]] = points.get(splitted_data[0], 0) + (6 - splitted_data.index(lang)) * pref
    return sorted(points, key=lambda k: (-points[k], k))[0]


class Test(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(solution(["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++",
                                   "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP",
                                   "GAME C++ C# JAVASCRIPT C JAVA"], ["PYTHON", "C++", "SQL"], [7, 5, 5]), "HARDWARE")
        self.assertEqual(solution(["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++",
                                   "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP",
                                   "GAME C++ C# JAVASCRIPT C JAVA"], ["JAVA", "JAVASCRIPT"], [7, 5]), "PORTAL")


if __name__ == "__main__":
    unittest.main()
