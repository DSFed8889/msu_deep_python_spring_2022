class TicTac:
    """Tic Tac Toe"""
    def validate_input(self, input_str):
        """Validation of coordinates"""
        try:
            input_list = list(map(int, input_str.split()))
        except ValueError:
            print("Ошибка! Вводите цифры!")
            return False
        if len(input_list) != 2:
            print("Неверное количество координат!")
            return False
        if input_list[0] > 3 or input_list[0] < 1 or input_list[1] > 3 or input_list[1] < 1:
            print("Координаты должны быть от 1 до 3!")
            return False
        if self.map[(input_list[1] - 1) + (input_list[0] - 1) * 3] != ' ':
            print('Error! This field is already occupied!')
            return False
        return True

    def __init__(self):
        self.map = [' ' for i in range(9)]
        print("Map consist of 9 points: columns and rows from 1 to 3")
        self.players = [['', ''], ['', '']]
        while self.players[0][0] == self.players[1][0]:
            print("Please, enter first nickname (x):")
            self.players[0] = (input(), 'x')
            self.next_move_player = self.players[0]
            print("Please, enter second nickname (0):")
            self.players[1] = (input(), '0')
            if self.players[0][0] == self.players[1][0]:
                print("Your nicknames are same!")

    def show_map(self):
        """Showing a map"""
        print("Map condition now:")
        for i in range(0, 7, 3):
            print(f'| {self.map[i]} | { self.map[i + 1]} | { self.map[i + 2]} |')

    def winner(self):
        """Returns nickname of winner"""
        def get_name(sign):
            for j in range(2):
                if self.players[j][1] == sign:
                    return self.players[j][0]
            return None

        # Checking rows and columns
        for i in range(3):
            if self.map[i*3] != ' ':
                if self.map[i*3] == self.map[i*3 + 1]:
                    if self.map[i*3 + 1] == self.map[i*3 + 2]:
                        return get_name(self.map[i*3])
            if self.map[i] != ' ':
                if self.map[i] == self.map[i+3] and self.map[i+3] == self.map[i+6]:
                    return get_name(self.map[i])
        # Checking diagonals
        if self.map[4] == ' ':
            return ''
        if self.map[0] == self.map[4] and self.map[4] == self.map[8]:
            return get_name(self.map[4])
        if self.map[2] == self.map[4] and self.map[4] == self.map[6]:
            return get_name(self.map[4])
        return ''

    def is_tie(self):
        """Returns is map situation tie (Bool)"""
        if ' ' not in self.map and self.winner() == '':
            return True
        return False

    def push(self, coords):
        """Pushing next sign on coords place"""
        if self.map[(coords[1] - 1) + (coords[0] - 1) * 3] == ' ':
            self.map[(coords[1] - 1) + (coords[0] - 1) * 3] = self.next_move_player[1]
            if self.next_move_player is self.players[0]:
                self.next_move_player = self.players[1]
            else:
                self.next_move_player = self.players[0]
            return 0
        print('Error! This field is already occupied!')
        return 1

    def start_game(self):
        """Game manager"""
        while self.winner() == '' and not self.is_tie():
            player = self.next_move_player
            while self.next_move_player == player:
                print(f"{self.next_move_player[0]} players move:")
                input_str = input()
                while not self.validate_input(input_str):
                    input_str = input()
                self.push(list(map(int, input_str.split())))
            self.show_map()
        if self.is_tie():
            print("It's tie!")
        else:
            print(f"The winner is: {self.winner()}!")


if __name__ == '__main__':
    a = TicTac()
    a.start_game()
