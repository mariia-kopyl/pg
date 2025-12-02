from abc import ABC, abstractmethod

class Piece(ABC):
    def __init__(self, color, position):
        """
        Inicializuje šachovou figurku.
        :param color: Barva figurky ('white' nebo 'black').
        :param position: Aktuální pozice na šachovnici jako tuple (row, col).
        """
        self.__color = color
        self.__position = position

    @abstractmethod
    def possible_moves(self):
        """
        Vrací všechny možné pohyby figurky.
        Musí být implementováno v podtřídách.
        :return: Seznam možných pozic [(row, col), ...].
        """
        pass

    @staticmethod
    def is_position_on_board(position):
        return 1 <= position[0] <= 8 and 1 <= position[1] <= 8

    @property
    def color(self):
        return self.__color

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, new_postion):
        self.__position = new_postion

    def __str__(self):
        return f'Piece({self.color}) at position {self.position}'


class Pawn(Piece):
    def possible_moves(self):
        """
        Vrací všechny možné tahy pěšáka.
        Bílý pěšák se pohybuje vpřed (řádek se zvyšuje).
        Černý pěšák se pohybuje vpřed (řádek se snižuje).
        :return: Seznam možných pozic [(row, col), ...].
        """
        row, col = self.position
        moves = []
        
        if self.color == 'white':
            # Bílý pěšák jde vpřed (zvyšuje se řádek)
            moves.append((row + 1, col))
            # Pokud je naStartovní pozici (řádek 2), může jít o 2 pole
            if row == 2:
                moves.append((row + 2, col))
        else:  # black
            # Černý pěšák jde vpřed (snižuje se řádek)
            moves.append((row - 1, col))
            # Pokud je na startovní pozici (řádek 7), může jít o 2 pole
            if row == 7:
                moves.append((row - 2, col))
        
        # Filtruje tahy, které jsou mimo šachovnici
        final_moves = []
        for move in moves:
            if self.is_position_on_board(move):
                final_moves.append(move)
        return final_moves

    def __str__(self):
        return f'Pawn({self.color}) at position {self.position}'


class Knight(Piece):
    def possible_moves(self):
        """
        Vrací všechny možné tahy jezdce.
        :return: Seznam možných pozic [(row, col), ...].
        """
        row, col = self.position
        moves = [
            (row + 2, col + 1), (row + 2, col - 1),
            (row - 2, col + 1), (row - 2, col - 1),
            (row + 1, col + 2), (row + 1, col - 2),
            (row - 1, col + 2), (row - 1, col - 2)
        ]
        
        # Filtruje tahy, které jsou mimo šachovnici
        final_moves = []
        for move in moves:
            if self.is_position_on_board(move):
                final_moves.append(move)
        return final_moves

    def __str__(self):
        return f'Knight({self.color}) at position {self.position}'


class Bishop(Piece):
    def possible_moves(self):
        """
        Vrací všechny možné tahy střelce.
        Střelec se pohybuje diagonálně.
        :return: Seznam možných pozic [(row, col), ...].
        """
        row, col = self.position
        moves = []
        
        # Čtyři diagonální směry
        directions = [
            (1, 1),   # doprava dolů
            (1, -1),  # doleva dolů
            (-1, 1),  # doprava nahoru
            (-1, -1)  # doleva nahoru
        ]
        
        for d_row, d_col in directions:
            for i in range(1, 8):
                new_row = row + i * d_row
                new_col = col + i * d_col
                new_pos = (new_row, new_col)
                
                if self.is_position_on_board(new_pos):
                    moves.append(new_pos)
                else:
                    break
        
        return moves

    def __str__(self):
        return f'Bishop({self.color}) at position {self.position}'


class Rook(Piece):
    def possible_moves(self):
        """
        Vrací všechny možné tahy věže.
        Věž se pohybuje horizontálně a vertikálně.
        :return: Seznam možných pozic [(row, col), ...].
        """
        row, col = self.position
        moves = []
        
        # Čtyři směry: nahoru, dolů, doleva, doprava
        directions = [
            (1, 0),   # dolů
            (-1, 0),  # nahoru
            (0, 1),   # doprava
            (0, -1)   # doleva
        ]
        
        for d_row, d_col in directions:
            for i in range(1, 8):
                new_row = row + i * d_row
                new_col = col + i * d_col
                new_pos = (new_row, new_col)
                
                if self.is_position_on_board(new_pos):
                    moves.append(new_pos)
                else:
                    break
        
        return moves

    def __str__(self):
        return f'Rook({self.color}) at position {self.position}'


class Queen(Piece):
    def possible_moves(self):
        """
        Vrací všechny možné tahy královny.
        Královna se pohybuje jako věž i jako střelec.
        :return: Seznam možných pozic [(row, col), ...].
        """
        row, col = self.position
        moves = []
        
        # Osm směrů: horizontálně, vertikálně a diagonálně
        directions = [
            (1, 0),   # dolů
            (-1, 0),  # nahoru
            (0, 1),   # doprava
            (0, -1),  # doleva
            (1, 1),   # doprava dolů
            (1, -1),  # doleva dolů
            (-1, 1),  # doprava nahoru
            (-1, -1)  # doleva nahoru
        ]
        
        for d_row, d_col in directions:
            for i in range(1, 8):
                new_row = row + i * d_row
                new_col = col + i * d_col
                new_pos = (new_row, new_col)
                
                if self.is_position_on_board(new_pos):
                    moves.append(new_pos)
                else:
                    break
        
        return moves

    def __str__(self):
        return f'Queen({self.color}) at position {self.position}'


class King(Piece):
    def possible_moves(self):
        """
        Vrací všechny možné tahy krále.
        Král se může pohybovat o jedno pole všemi směry.
        :return: Seznam možných pozic [(row, col), ...].
        """
        row, col = self.position
        moves = [
            (row + 1, col),     # dolů
            (row - 1, col),     # nahoru
            (row, col + 1),     # doprava
            (row, col - 1),     # doleva
            (row + 1, col + 1), # doprava dolů
            (row + 1, col - 1), # doleva dolů
            (row - 1, col + 1), # doprava nahoru
            (row - 1, col - 1)  # doleva nahoru
        ]
        
        # Filtruje tahy, které jsou mimo šachovnici
        final_moves = []
        for move in moves:
            if self.is_position_on_board(move):
                final_moves.append(move)
        return final_moves

    def __str__(self):
        return f'King({self.color}) at position {self.position}'


if __name__ == "__main__":
    # Testování
    print("Knight")
    piece = Knight("black", (1, 2))
    print(piece)
    print(piece.possible_moves())
    
    print("Pawn (white)")
    pawn_white = Pawn("white", (2, 4))
    print(pawn_white)
    print(pawn_white.possible_moves())
    
    print("Pawn (black)")
    pawn_black = Pawn("black", (7, 4))
    print(pawn_black)
    print(pawn_black.possible_moves())
    
    print("Bishop")
    bishop = Bishop("white", (4, 4))
    print(bishop)
    print(bishop.possible_moves())
    
    print("Rook")
    rook = Rook("white", (4, 4))
    print(rook)
    print(rook.possible_moves())

    
    print("King")
    king = King("white", (4, 4))
    print(king)
    print(king.possible_moves())