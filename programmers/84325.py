import unittest


def solution(table, languages, preference):
    language_preference = []
    for lang, pref in zip(languages, preference):
        language_preference.append((lang, pref))

    points = {}
    for col in table:
        splitted_data = col.split()
        key = splitted_data.pop(0)
        langs = splitted_data[::-1]
        point = 0
        for pref in language_preference:
            try:
                point += (langs.index(pref[0]) + 1) * pref[1]
            except ValueError:
                continue
        points[key] = point

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
