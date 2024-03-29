import sys
import io
import unittest
from unittest.mock import patch
from faker import Faker
from tic_tac_toe import TicTac


class TestTicTac(unittest.TestCase):
    @patch('tic_tac_toe.TicTac.__init__', return_value=None)
    def setUp(self, __init__mock):
        self.game = TicTac()
        self.game.map = [' 'for i in range(9)]
        self.game.players = [[Faker(locale='Ru_ru').name, 'x'], [Faker(locale='Ru_ru').name, '0']]
        self.game.next_move_player = self.game.players[0]
        print("Set up")

    def tearDown(self):
        suppress_text = io.StringIO()
        sys.stdout = suppress_text
        self.game.map = [' 'for i in range(9)]
        print("Tear down")

    def test_push(self):
        suppress_text = io.StringIO()
        sys.stdout = suppress_text
        print('Start testing push method...')
        # Simple pushing 'x'
        self.game.push([3, 3])
        self.assertListEqual(self.game.map, [' ', ' ', ' ',
                                             ' ', ' ', ' ',
                                             ' ', ' ', 'x'])
        # Pushing '0' on 'x'
        print("Pushing '0' on 'x'")
        self.game.push([3, 3])
        self.assertListEqual(self.game.map, [' ', ' ', ' ',
                                             ' ', ' ', ' ',
                                             ' ', ' ', 'x'])
        # Simple pushing '0'
        self.game.push([2, 2])
        self.assertListEqual(self.game.map, [' ', ' ', ' ',
                                             ' ', '0', ' ',
                                             ' ', ' ', 'x'])
        # Pushing 'x' on 'x'
        print("Pushing 'x' on 'x'")
        self.game.push([3, 3])
        self.assertListEqual(self.game.map, [' ', ' ', ' ',
                                             ' ', '0', ' ',
                                             ' ', ' ', 'x'])
        # Pushing 'x' on '0'
        print("Pushing 'x' on '0'")
        self.game.push([2, 2])
        self.assertListEqual(self.game.map, [' ', ' ', ' ',
                                             ' ', '0', ' ',
                                             ' ', ' ', 'x'])
        # Simple pushing 'x'
        self.game.push([1, 2])
        self.assertListEqual(self.game.map, [' ', 'x', ' ',
                                             ' ', '0', ' ',
                                             ' ', ' ', 'x'])
        # Pushing '0' on '0'
        print("Pushing '0' on '0'")
        self.game.push([2, 2])
        self.assertListEqual(self.game.map, [' ', 'x', ' ',
                                             ' ', '0', ' ',
                                             ' ', ' ', 'x'])
        print('End testing push method')

    def test_is_tie(self):
        suppress_text = io.StringIO()
        sys.stdout = suppress_text
        print('Start testing is_tie method...')
        # Empty map
        self.game.map = [' ', ' ', ' ',
                         ' ', ' ', ' ',
                         ' ', ' ', ' ']
        self.assertFalse(self.game.is_tie())
        # Tie end of game
        self.game.map = ['x', '0', 'x',
                         'x', 'x', '0',
                         '0', 'x', '0']
        self.assertTrue(self.game.is_tie())
        self.game.map = ['x', '0', 'x',
                         '0', '0', 'x',
                         'x', 'x', '0']
        self.assertTrue(self.game.is_tie())
        # Game is not ended
        self.game.map = [' ', '0', 'x',
                         'x', 'x', '0',
                         '0', 'x', '0']
        self.assertFalse(self.game.is_tie())
        # '0' won
        self.game.map = ['x', 'x', '0',
                         'x', '0', '0',
                         '0', 'x', 'x']
        self.assertFalse(self.game.is_tie())
        # 'x' won
        self.game.map = ['x', '0', 'x',
                         '0', 'x', '0',
                         'x', '0', 'x']
        self.assertFalse(self.game.is_tie())
        print('End testing is_tie method')

    def test_winner(self):
        suppress_text = io.StringIO()
        sys.stdout = suppress_text
        print('Start testing winner method...')
        # Empty map
        self.game.map = [' ', ' ', ' ',
                         ' ', ' ', ' ',
                         ' ', ' ', ' ']
        self.assertIsNot(self.game.winner(), self.game.players[0][0])
        self.assertIsNot(self.game.winner(), self.game.players[1][0])
        # Nobody won
        self.game.map = ['x', '0', 'x',
                         'x', 'x', '0',
                         '0', 'x', '0']
        self.assertIsNot(self.game.winner(), self.game.players[0][0])
        self.assertIsNot(self.game.winner(), self.game.players[1][0])

        # 'x' won situations
        # main diag
        self.game.map = ['x', '0', 'x',
                         '0', 'x', '0',
                         '0', 'x', 'x']
        self.assertIs(self.game.winner(), self.game.players[0][0])
        self.assertIsNot(self.game.winner(), self.game.players[1][0])
        # side diag
        self.game.map = ['x', '0', ' ',
                         '0', 'x', ' ',
                         ' ', ' ', 'x']
        self.assertIs(self.game.winner(), self.game.players[0][0])
        self.assertIsNot(self.game.winner(), self.game.players[1][0])
        # 1 string
        self.game.map = ['x', 'x', 'x',
                         'x', '0', '0',
                         '0', 'x', '0']
        self.assertIs(self.game.winner(), self.game.players[0][0])
        self.assertIsNot(self.game.winner(), self.game.players[1][0])
        # 2 string
        self.game.map = ['x', '0', '0',
                         'x', 'x', 'x',
                         '0', '0', 'x']
        self.assertIs(self.game.winner(), self.game.players[0][0])
        self.assertIsNot(self.game.winner(), self.game.players[1][0])
        # 3 string
        self.game.map = ['0', '0', 'x',
                         'x', '0', '0',
                         'x', 'x', 'x']
        self.assertIs(self.game.winner(), self.game.players[0][0])
        self.assertIsNot(self.game.winner(), self.game.players[1][0])
        # 1 column
        self.game.map = ['x', 'x', '0',
                         'x', '0', 'x',
                         'x', '0', '0']
        self.assertIs(self.game.winner(), self.game.players[0][0])
        self.assertIsNot(self.game.winner(), self.game.players[1][0])
        # 2 column
        self.game.map = ['0', 'x', '0',
                         'x', 'x', '0',
                         '0', 'x', 'x']
        self.assertIs(self.game.winner(), self.game.players[0][0])
        self.assertIsNot(self.game.winner(), self.game.players[1][0])
        # 3 column
        self.game.map = ['0', 'x', 'x',
                         '0', '0', 'x',
                         'x', '0', 'x']
        self.assertIs(self.game.winner(), self.game.players[0][0])
        self.assertIsNot(self.game.winner(), self.game.players[1][0])
        self.game.map = ['0', '0', 'x',
                         ' ', 'x', 'x',
                         '0', ' ', 'x']
        self.assertIs(self.game.winner(), self.game.players[0][0])
        self.assertIsNot(self.game.winner(), self.game.players[1][0])
        self.game.map = ['x', '0', 'x',
                         '0', 'x', '0',
                         'x', '0', 'x']
        self.assertIs(self.game.winner(), self.game.players[0][0])
        self.assertIsNot(self.game.winner(), self.game.players[1][0])

        # '0' won situations
        # main diag
        self.game.map = ['0', 'x', '0',
                         'x', '0', 'x',
                         'x', '0', '0']
        self.assertIsNot(self.game.winner(), self.game.players[0][0])
        self.assertIs(self.game.winner(), self.game.players[1][0])
        # side diag
        self.game.map = ['0', 'x', ' ',
                         'x', '0', ' ',
                         ' ', ' ', '0']
        self.assertIsNot(self.game.winner(), self.game.players[0][0])
        self.assertIs(self.game.winner(), self.game.players[1][0])
        # 1 string
        self.game.map = ['0', '0', '0',
                         '0', 'x', 'x',
                         'x', '0', 'x']
        self.assertIsNot(self.game.winner(), self.game.players[0][0])
        self.assertIs(self.game.winner(), self.game.players[1][0])
        # 2 string
        self.game.map = ['0', 'x', 'x',
                         '0', '0', '0',
                         'x', 'x', '0']
        self.assertIsNot(self.game.winner(), self.game.players[0][0])
        self.assertIs(self.game.winner(), self.game.players[1][0])
        # 3 string
        self.game.map = ['x', 'x', '0',
                         '0', 'x', 'x',
                         '0', '0', '0']
        self.assertIsNot(self.game.winner(), self.game.players[0][0])
        self.assertIs(self.game.winner(), self.game.players[1][0])
        # 1 column
        self.game.map = ['0', '0', 'x',
                         '0', 'x', '0',
                         '0', 'x', 'x']
        self.assertIsNot(self.game.winner(), self.game.players[0][0])
        self.assertIs(self.game.winner(), self.game.players[1][0])
        # 2 column
        self.game.map = ['x', '0', 'x',
                         '0', '0', 'x',
                         'x', '0', '0']
        self.assertIsNot(self.game.winner(), self.game.players[0][0])
        self.assertIs(self.game.winner(), self.game.players[1][0])
        # 3 column
        self.game.map = ['x', '0', '0',
                         'x', 'x', '0',
                         '0', 'x', '0']
        self.assertIsNot(self.game.winner(), self.game.players[0][0])
        self.assertIs(self.game.winner(), self.game.players[1][0])
        self.game.map = ['0', 'x', '0',
                         'x', '0', 'x',
                         '0', 'x', 'x']
        self.assertIsNot(self.game.winner(), self.game.players[0][0])
        self.assertIs(self.game.winner(), self.game.players[1][0])
        self.game.map = ['0', '0', '0',
                         'x', 'x', ' ',
                         '0', 'x', 'x']
        self.assertIsNot(self.game.winner(), self.game.players[0][0])
        self.assertIs(self.game.winner(), self.game.players[1][0])
        # By game rules, it's impossible to be winner 'x' and '0' together
        print('End testing winner method')

    def test_validate_input(self):
        suppress_text = io.StringIO()
        sys.stdout = suppress_text
        print('Start validate_input method...')
        # Correct coordinates
        self.assertTrue(self.game.validate_input('1 1'))
        self.assertTrue(self.game.validate_input('1 2'))
        self.assertTrue(self.game.validate_input('1 3'))
        self.assertTrue(self.game.validate_input('2 1'))
        self.assertTrue(self.game.validate_input('2 2'))
        self.assertTrue(self.game.validate_input('2 3'))
        self.assertTrue(self.game.validate_input('3 1'))
        self.assertTrue(self.game.validate_input('3 2'))
        self.assertTrue(self.game.validate_input('3 3'))
        # Not empty coordinate
        self.game.map = ['x', 'x', '0',
                         'x', '0', '0',
                         '0', ' ', 'x']
        self.assertFalse(self.game.validate_input('1 1'))
        self.assertFalse(self.game.validate_input('1 2'))
        self.assertFalse(self.game.validate_input('1 3'))
        self.assertFalse(self.game.validate_input('2 1'))
        self.assertFalse(self.game.validate_input('2 2'))
        self.assertFalse(self.game.validate_input('2 3'))
        self.assertFalse(self.game.validate_input('3 1'))
        self.assertTrue(self.game.validate_input('3 2'))
        self.assertFalse(self.game.validate_input('3 3'))

        self.game.map = ['x', '0', 'x',
                         'x', 'x', '0',
                         '0', 'x', '0']
        self.assertFalse(self.game.validate_input('1 1'))
        self.assertFalse(self.game.validate_input('1 2'))
        self.assertFalse(self.game.validate_input('1 3'))
        self.assertFalse(self.game.validate_input('2 1'))
        self.assertFalse(self.game.validate_input('2 2'))
        self.assertFalse(self.game.validate_input('2 3'))
        self.assertFalse(self.game.validate_input('3 1'))
        self.assertFalse(self.game.validate_input('3 2'))
        self.assertFalse(self.game.validate_input('3 3'))

        self.game.map = ['x', '0', 'x',
                         ' ', ' ', ' ',
                         '0', 'x', '0']
        self.assertFalse(self.game.validate_input('1 1'))
        self.assertFalse(self.game.validate_input('1 2'))
        self.assertFalse(self.game.validate_input('1 3'))
        self.assertTrue(self.game.validate_input('2 1'))
        self.assertTrue(self.game.validate_input('2 2'))
        self.assertTrue(self.game.validate_input('2 3'))
        self.assertFalse(self.game.validate_input('3 1'))
        self.assertFalse(self.game.validate_input('3 2'))
        self.assertFalse(self.game.validate_input('3 3'))
        # Words (incorrect)
        print('Words instead of coordinates')
        self.assertFalse(self.game.validate_input('sldjwe'))
        self.assertFalse(self.game.validate_input('sdf dfw'))
        # Incorrect coordinates
        print('Incorrect coordinates')
        self.assertFalse(self.game.validate_input('0 0'))
        self.assertFalse(self.game.validate_input('4 4'))
        self.assertFalse(self.game.validate_input('4 1'))
        self.assertFalse(self.game.validate_input('4 2'))
        self.assertFalse(self.game.validate_input('4 3'))
        self.assertFalse(self.game.validate_input('1 4'))
        self.assertFalse(self.game.validate_input('2 4'))
        self.assertFalse(self.game.validate_input('3 4'))
        self.assertFalse(self.game.validate_input('0 1'))
        self.assertFalse(self.game.validate_input('0 2'))
        self.assertFalse(self.game.validate_input('0 3'))
        self.assertFalse(self.game.validate_input('1 0'))
        self.assertFalse(self.game.validate_input('2 0'))
        self.assertFalse(self.game.validate_input('3 0'))
        self.assertFalse(self.game.validate_input('120 0123'))
        # Not enough
        print('Not enough coordinates')
        self.assertFalse(self.game.validate_input('100'))
        self.assertFalse(self.game.validate_input('2'))
        self.assertFalse(self.game.validate_input('3'))
        # Redundant
        self.assertFalse(self.game.validate_input('0 0 0'))
        self.assertFalse(self.game.validate_input('0 0 1'))
        self.assertFalse(self.game.validate_input('0 0 2'))
        self.assertFalse(self.game.validate_input('0 0 4'))
        self.assertFalse(self.game.validate_input('1 1 1'))
        self.assertFalse(self.game.validate_input('1 2 3'))
        self.assertFalse(self.game.validate_input('1 2 4'))
        self.assertFalse(self.game.validate_input('4 2 1'))
        self.assertFalse(self.game.validate_input('3 0 3'))
        self.assertFalse(self.game.validate_input('2 2 2 2'))
        self.assertFalse(self.game.validate_input('1 1 1 1'))
        self.assertFalse(self.game.validate_input('1 2 3 1 2 3 2 3 2 1 2 3 2 3 2 1'))
        # Empty string
        self.assertFalse(self.game.validate_input(''))
        print('End validate_input method')


if __name__ == "__main__":
    unittest.main()
