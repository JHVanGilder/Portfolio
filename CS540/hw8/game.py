import random
import copy


class TeekoPlayer:
    """ An object representation for an AI game player for the game Teeko.
    """
    board = [[' ' for j in range(5)] for i in range(5)]
    pieces = ['b', 'r']

    def __init__(self):
        """ Initializes a TeekoPlayer object by randomly selecting red or black as its
        piece color.
        """
        self.my_piece = random.choice(self.pieces)
        self.opp = self.pieces[0] if self.my_piece == self.pieces[1] else self.pieces[1]

    def make_move(self, state):
        """ Selects a (row, col) space for the next move. You may assume that whenever
        this function is called, it is this player's turn to move.

        Args:
            state (list of lists): should be the current state of the game as saved in
                this TeekoPlayer object. Note that this is NOT assumed to be a copy of
                the game state and should NOT be modified within this method (use
                place_piece() instead). Any modifications (e.g. to generate successors)
                should be done on a deep copy of the state.

                In the "drop phase", the state will contain less than 8 elements which
                are not ' ' (a single space character).

        Return:
            move (list): a list of move tuples such that its format is
                    [(row, col), (source_row, source_col)]
                where the (row, col) tuple is the location to place a piece and the
                optional (source_row, source_col) tuple contains the location of the
                piece the AI plans to relocate (for moves after the drop phase). In
                the drop phase, this list should contain ONLY THE FIRST tuple.

        Note that without drop phase behavior, the AI will just keep placing new markers
            and will eventually take over the board. This is not a valid strategy and
            will earn you no points.
        """
        free_spots = 0
        for row in state:
            free_spots = free_spots + row.count(' ')
        if free_spots > 17:
            drop_phase = True
        else:
            drop_phase = False

        move = []
        if not drop_phase:
            opt_val = float('-inf')
            opt_state = None
            for s in self.succ(state, False):
                if self.game_value(s) == -1 or self.game_value(s) == 1:
                    opt_state = s
                    break
                current_val = self.max_value(state, 0)
                if current_val > opt_val:
                    opt_val = current_val
                    opt_state = s
            for i in range(len(state)):
                for j in range(len(state[i])):
                    if state[i][j] != ' ' and opt_state[i][j] == ' ':
                        move.append((i, j))
                    if state[i][j] == ' ' and opt_state[i][j] != ' ':
                        move.insert(0, (i, j))

        # select an unoccupied space randomly
        # TODO: implement a minimax algorithm to play better
        else:
            opt_val = float('-inf')
            opt_state = None
            for s in self.succ(state, True):
                if self.game_value(s) == -1 or self.game_value(s) == 1:
                    opt_state = s
                    break
                current_val = self.max_value(state, 0)
                if current_val > opt_val:
                    opt_val = current_val
                    opt_state = s
            for i in range(len(state)):
                for j in range(len(state[i])):
                    if state[i][j] == ' ' and opt_state[i][j] != ' ':
                        move.insert(0, (i, j))

        print(move)
        return move

    def drop_status(self, state):
        free_spaces = 0
        for row in state:
            free_spaces += row.count(' ')
        if free_spaces > 17:
            drop_phase = True
        else:
            drop_phase = False
        return drop_phase

    def succ(self, state, drop):
        color = self.my_piece
        drop_phase = drop
        legal_moves = []
        if drop_phase == True:
            for i in range(len(state)):
                for j in range(len(state[i])):
                    if state[i][j] == ' ':
                        copy_state = copy.deepcopy(state)
                        copy_state[i][j] = color
                        legal_moves.append(copy_state)
            return legal_moves
        elif drop_phase == False:
            for i in range(len(state)):
                for j in range(len(state[i])):
                    if state[i][j] == color:
                        # check top middle
                        if (i - 1) >= 0 and state[i - 1][j] == ' ':
                            copy_state = copy.deepcopy(state)
                            copy_state[i - 1][j] = color
                            copy_state[i][j] = ' '
                            legal_moves.append(copy_state)
                        # check top left
                        if (i - 1) >= 0 and (j - 1) >= 0 and state[i - 1][j - 1] == ' ':
                            copy_state = copy.deepcopy(state)
                            copy_state[i - 1][j - 1] = color
                            copy_state[i][j] = ' '
                            legal_moves.append(copy_state)
                        # check top right
                        if (i - 1) >= 0 and (j + 1) <= 4 and state[i - 1][j + 1] == ' ':
                            copy_state = copy.deepcopy(state)
                            copy_state[i - 1][j + 1] = color
                            copy_state[i][j] = ' '
                            legal_moves.append(copy_state)
                        # check middle left
                        if (j - 1) >= 0 and state[i][j - 1] == ' ':
                            copy_state = copy.deepcopy(state)
                            copy_state[i][j - 1] = color
                            copy_state[i][j] = ' '
                            legal_moves.append(copy_state)
                        # check middle right
                        if (j + 1) <= 4 and state[i][j + 1] == ' ':
                            copy_state = copy.deepcopy(state)
                            copy_state[i][j + 1] = color
                            copy_state[i][j] = ' '
                            legal_moves.append(copy_state)
                        # check bottom middle
                        if (i + 1) <= 4 and state[i + 1][j] == ' ':
                            copy_state = copy.deepcopy(state)
                            copy_state[i + 1][j] = color
                            copy_state[i][j] = ' '
                            legal_moves.append(copy_state)
                        # check bottom left
                        if (i + 1) <= 4 and (j - 1) >= 0 and state[i + 1][j - 1] == ' ':
                            copy_state = copy.deepcopy(state)
                            copy_state[i + 1][j - 1] = color
                            copy_state[i][j] = ' '
                            legal_moves.append(copy_state)
                        # check bottom right
                        if (i + 1) <= 4 and (j + 1) <= 4 and state[i + 1][j + 1] == ' ':
                            copy_state = copy.deepcopy(state)
                            copy_state[i + 1][j + 1] = color
                            copy_state[i][j] = ' '
                            legal_moves.append(copy_state)
        return legal_moves

    def opponent_move(self, move):
        """ Validates the opponent's next move against the internal board representation.
        You don't need to touch this code.

        Args:
            move (list): a list of move tuples such that its format is
                    [(row, col), (source_row, source_col)]
                where the (row, col) tuple is the location to place a piece and the
                optional (source_row, source_col) tuple contains the location of the
                piece the AI plans to relocate (for moves after the drop phase). In
                the drop phase, this list should contain ONLY THE FIRST tuple.
        """
        # validate input
        if len(move) > 1:
            source_row = move[1][0]
            source_col = move[1][1]
            if source_row != None and self.board[source_row][source_col] != self.opp:
                self.print_board()
                print(move)
                raise Exception("You don't have a piece there!")
            if abs(source_row - move[0][0]) > 1 or abs(source_col - move[0][1]) > 1:
                self.print_board()
                print(move)
                raise Exception('Illegal move: Can only move to an adjacent space')
        if self.board[move[0][0]][move[0][1]] != ' ':
            raise Exception("Illegal move detected")
        # make move
        self.place_piece(move, self.opp)

    def place_piece(self, move, piece):
        """ Modifies the board representation using the specified move and piece

        Args:
            move (list): a list of move tuples such that its format is
                    [(row, col), (source_row, source_col)]
                where the (row, col) tuple is the location to place a piece and the
                optional (source_row, source_col) tuple contains the location of the
                piece the AI plans to relocate (for moves after the drop phase). In
                the drop phase, this list should contain ONLY THE FIRST tuple.

                This argument is assumed to have been validated before this method
                is called.
            piece (str): the piece ('b' or 'r') to place on the board
        """
        if len(move) > 1:
            self.board[move[1][0]][move[1][1]] = ' '
        self.board[move[0][0]][move[0][1]] = piece

    def print_board(self):
        """ Formatted printing for the board """
        for row in range(len(self.board)):
            line = str(row)+": "
            for cell in self.board[row]:
                line += cell + " "
            print(line)
        print("   A B C D E")

    def game_value(self, state):
        """ Checks the current board status for a win condition

        Args:
        state (list of lists): either the current state of the game as saved in
            this TeekoPlayer object, or a generated successor state.

        Returns:
            int: 1 if this TeekoPlayer wins, -1 if the opponent wins, 0 if no winner

        TODO: complete checks for diagonal and box wins DONE
        """
        # check horizontal wins
        for row in state:
            for i in range(2):
                if row[i] != ' ' and row[i] == row[i+1] == row[i+2] == row[i+3]:
                    return 1 if row[i]==self.my_piece else -1

        # check vertical wins
        for col in range(5):
            for i in range(2):
                if state[i][col] != ' ' \
                        and state[i][col] == state[i+1][col] == state[i+2][col] == state[i+3][col]:
                    return 1 if state[i][col]==self.my_piece else -1

        for row in range(2):
            for col in range(2):
                if state[row][col] != ' ' and (state[row][col] == state[row + 1][col + 1] ==
                    state[row + 2][col + 2] == state[row + 3][col + 3]):
                    return 1 if state[row][col]==self.my_piece else -1

        for row in range(3, 5):
            for col in range(2):
                if state[row][col] != ' ' and (state[row][col] == state[row - 1][col + 1] ==
                    state[row - 2][col + 2] == state[row - 3][col + 3]):
                    return 1 if state[row][col]==self.my_piece else -1

        for row in range(4):
            for col in range(4):
                if state[row][col] != ' ' and (state[row][col] == state[row][col + 1] ==
                    state[row + 1][col + 1] == state[row + 1][col]):
                    return 1 if state[row][col]==self.my_piece else -1

        # TODO: check \ diagonal wins DONE
        # TODO: check / diagonal wins DONE
        # TODO: check box wins DONE

        return 0 # no winner yet

    def heuristic_game_value(self, state, color):
        if abs(self.game_value(state)) == 1:
            return self.game_value(state)
        else:
            count_list = []
            num_horizontal = 0
            for row in state:
                if num_horizontal > row.count(color):
                    num_horizontal = row.count(color)
            count_list.append(num_horizontal)
            num_vertical = 0
            for row in zip(*state):
                if num_vertical > row.count(color):
                    num_vertical = row.count(color)
            count_list.append(num_vertical)
            corner_diag1 = 0
            for i in range(len(state)):
                if state[i][i] == color:
                    corner_diag1 += 1
            count_list.append(corner_diag1)
            corner_diag2 = 0
            for i in reversed(range(len(state))):
                if state[i][4-i] == color:
                    corner_diag2 += 1
            count_list.append(corner_diag2)
            diag3 = 0
            for i in range(1, 4):
                for j in range(3):
                    if state[i][j] == color:
                        diag3 += 1
            count_list.append(diag3)
            diag4 = 0
            for i in range(3):
                for j in range(1, 4):
                    if state[i][j] == color:
                        diag4 += 1
            count_list.append(diag4)
            diag5 = 0
            for i in reversed(range(1, 4)):
                for j in range(3):
                    if state[i][j] == color:
                        diag5 += 1
            count_list.append(diag5)
            diag6 = 0
            for i in reversed(range(3)):
                for j in range(1, 4):
                    if state[i][j] == color:
                        diag6 += 1
            count_list.append(diag6)
        h = float(max(count_list))/4.0
        return h

    def max_value(self, state, depth):
        if abs(self.heuristic_game_value(state, self.opp)) == 1:
            return self.heuristic_game_value(state, self.opp)
        elif depth == 2:
            return self.heuristic_game_value(state, self.opp)
        else:
            return max(self.heuristic_game_value(next, self.opp)
                       for next in self.succ(state, self.drop_status(state)))

############################################################################
#
# THE FOLLOWING CODE IS FOR SAMPLE GAMEPLAY ONLY
#
############################################################################
def main():
    print('Hello, this is Samaritan')
    ai = TeekoPlayer()
    piece_count = 0
    turn = 0

    # drop phase
    while piece_count < 8 and ai.game_value(ai.board) == 0:

        # get the player or AI's move
        if ai.my_piece == ai.pieces[turn]:
            ai.print_board()
            move = ai.make_move(ai.board)
            # print(move)
            ai.place_piece(move, ai.my_piece)
            print(ai.my_piece+" moved at "+chr(move[0][1]+ord("A"))+str(move[0][0]))
        else:
            move_made = False
            ai.print_board()
            print(ai.opp+"'s turn")
            while not move_made:
                player_move = input("Move (e.g. B3): ")
                while player_move[0] not in "ABCDE" or player_move[1] not in "01234":
                    player_move = input("Move (e.g. B3): ")
                try:
                    ai.opponent_move([(int(player_move[1]), ord(player_move[0])-ord("A"))])
                    move_made = True
                except Exception as e:
                    print(e)

        # update the game variables
        piece_count += 1
        turn += 1
        turn %= 2

    # move phase - can't have a winner until all 8 pieces are on the board
    while ai.game_value(ai.board) == 0:

        # get the player or AI's move
        if ai.my_piece == ai.pieces[turn]:
            ai.print_board()
            move = ai.make_move(ai.board)
            print(move)
            ai.place_piece(move, ai.my_piece)
            print(ai.my_piece+" moved from "+chr(move[1][1]+ord("A"))+str(move[1][0]))
            print("  to "+chr(move[0][1]+ord("A"))+str(move[0][0]))
        else:
            move_made = False
            ai.print_board()
            print(ai.opp+"'s turn")
            while not move_made:
                move_from = input("Move from (e.g. B3): ")
                while move_from[0] not in "ABCDE" or move_from[1] not in "01234":
                    move_from = input("Move from (e.g. B3): ")
                move_to = input("Move to (e.g. B3): ")
                while move_to[0] not in "ABCDE" or move_to[1] not in "01234":
                    move_to = input("Move to (e.g. B3): ")
                try:
                    ai.opponent_move([(int(move_to[1]), ord(move_to[0])-ord("A")),
                                    (int(move_from[1]), ord(move_from[0])-ord("A"))])
                    move_made = True
                except Exception as e:
                    print(e)

        # update the game variables
        turn += 1
        turn %= 2

    ai.print_board()
    if ai.game_value(ai.board) == 1:
        print("AI wins! Game over.")
    else:
        print("You win! Game over.")


if __name__ == "__main__":
    main()
    # for i in reversed(range(5)):
    #     print([i, 4-i])