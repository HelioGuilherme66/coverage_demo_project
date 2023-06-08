import unittest


class TestAction(unittest.TestCase):

    def test_valid_data(self):
        from myapp import Action
        my_action = Action('1234')
        
        print(f"My action is: {my_action}")
