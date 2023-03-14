import json
import random

class ProblemGenerator:

    @staticmethod
    def generate():
        
        result = {}

        num1 = random.randint(2,20)
        num2 = random.randint(2,20)
        
        result['num1'] = num1
        result['num2'] = num2
        result['operation'] = 'multiply'
        result['answer'] = num1 * num2

        return result
    
    @staticmethod
    def generate_with_level(difficulty):

        #define bounds for problem values of different difficulties
        level_map = {
            'easy': {
                'lower': 2,
                'upper': 12
            },
            'medium': {
                'lower': 2,
                'upper': 20
            },            
            'hard': {
                'lower': 2,
                'upper': 40
            }
        }

        result = {}
        num1 = random.randint(level_map[difficulty]['lower'], level_map[difficulty]['upper'] )
        num2 = random.randint(level_map[difficulty]['lower'], level_map[difficulty]['upper'] )

        result['num1'] = num1
        result['num2'] = num2
        result['operation'] = 'multiply'
        result['answer'] = num1 * num2

        return result







        




    
    

