import unittest
import sys

sys.path.append('C:/Users/wtind/projects/mental_maths_project/mentalmaths')

from main import ProblemGenerator

class TestProblemGenerator(unittest.TestCase):

    def test_answer_correct(self):

        data = ProblemGenerator.generate_with_level('hard')

        self.assertTrue(data['answer'] == data['num1'] * data['num2'])





        



if __name__ == '__main__':
    unittest.main()