#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:mod:`cell` module

:author: YOUR NAME HERE

:date:


"""

class Cell():

    def __init__(self):
        """
        :return: a new hidden cell of a minesweeper's grid.
                 existence of a bomb, number of bombs in neighborhood
                 have to be stated later.
        :rtype: Cell
        :UC: none
        :Examples:

        >>> cel = Cell()
        >>> cel.is_bomb()
        False
        >>> cel.is_hypothetic()
        False
        >>> cel.is_revealed()
        False
        >>> cel.number_of_bombs_in_neighborhood()
        0
        """

        self.__coords = (0, 0)
        self.__bomb = False
        self.__hypo = False
        self.__revealed = False
        self.__nbBombs = 0

    def set_coords(self, x, y) :
        """
        :param x: the abscissa of the Cell
        :type x: int
        :param y: the ordinate of the Cell
        :type y: int
        :return: None
        :side effect: Sets cell coordinates to (x, y)
        :UC: none
        :Example:

        >>> cell = Cell()
        >>> cell.get_coords()
        (0, 0)
        >>> cell.set_coords(4, 7)
        >>> cell.get_coords()
        (4, 7)
        >>> cell.set_coords(10, 3)
        >>> cell.get_coords()
        (10, 3)
        """

        self.__coords = (x, y)


    def get_coords(self) :
        """
        :return: the coordinates of the Cell
        :rtype: tuple
        :UC: none
        :Example:

        >>> cell = Cell()
        >>> cell.get_coords()
        (0, 0)
        >>> cell.set_coords(4, 7)
        >>> cell.get_coords()
        (4, 7)
        >>> cell.set_coords(10, 3)
        >>> cell.get_coords()
        (10, 3)
        """

        return self.__coords


    def is_revealed(self):
        """
        :return: True if self is revealed, False otherwise
        :rtype: bool
        :UC: none
        :Example:

        >>> cel = Cell()
        >>> cel.is_revealed()
        False
        >>> cel.reveal()
        >>> cel.is_revealed()
        True
        """

        return self.__revealed

    def reveal(self):
        """
        :return: None
        :side effect: modify reveal state of self
        :UC: none
        :Example:

        >>> cel = Cell()
        >>> cel.is_revealed()
        False
        >>> cel.reveal()
        >>> cel.is_revealed()
        True
        """

        self.__revealed = True

    def is_bomb(self):
        """
        :return: True if self contains a bomb, False otherwise
        :rtype: bool
        :UC: none
        :Example:

        >>> cel = Cell()
        >>> cel.is_bomb()
        False
        >>> cel.set_bomb()
        >>> cel.is_bomb()
        True
        """

        return self.__bomb


    def set_bomb(self):
        """
        :return: None
        :side effect: put a bomb in self
        :UC: none
        :Example:

        >>> cel = Cell()
        >>> cel.is_bomb()
        False
        >>> cel.set_bomb()
        >>> cel.is_bomb()
        True
        """

        self.__bomb = True

    def is_hypothetic(self):
        """
        :return: True if cel if hypothetically containing a bomb
                 False otherwise
        :rtype: bool
        :UC: none
        :Example:

        >>> cel = Cell()
        >>> cel.is_hypothetic()
        False
        >>> cel.set_hypothetic()
        >>> cel.is_hypothetic()
        True
        """

        return self.__hypo


    def set_hypothetic(self):
        """
        :return: None
        :side effect: modify hypothetic bomb state of self if self is not revealed
        :UC: none
        :Example:

        >>> cel = Cell()
        >>> cel.is_hypothetic()
        False
        >>> cel.set_hypothetic()
        >>> cel.is_hypothetic()
        True
        """

        self.__hypo = True

    def unset_hypothetic(self):
        """
        :return: None
        :side effect: modify hypothetic bomb state of self if self is not revealed
        :UC: none
        :Example:

        >>> cel = Cell()
        >>> cel.is_hypothetic()
        False
        >>> cel.set_hypothetic()
        >>> cel.is_hypothetic()
        True
        >>> cel.unset_hypothetic()
        >>> cel.is_hypothetic()
        False
        """

        self.__hypo = False


    def number_of_bombs_in_neighborhood(self):
        """
        :return: number of bombs in the neighborhood of self
        :rtype: int
        :UC: none
        :Example:

        >>> cel = Cell()
        >>> cel.number_of_bombs_in_neighborhood()
        0
        >>> cel.incr_number_of_bombs_in_neighborhood()
        >>> cel.number_of_bombs_in_neighborhood()
        1
        """

        return self.__nbBombs

    def incr_number_of_bombs_in_neighborhood(self):
        """
        :return: None
        :side effect: increment the number of bombs in neighborhood of self
        :UC: none
        :Example:

        >>> cel = Cell()
        >>> cel.number_of_bombs_in_neighborhood()
        0
        >>> cel.incr_number_of_bombs_in_neighborhood()
        >>> cel.number_of_bombs_in_neighborhood()
        1
        """

        self.__nbBombs += 1


    def __str__(self):
        """
        :return: a string representation of self state
        :rtype: str
        :UC: none
        :Example:

        >>> cel = Cell()
        >>> str(cel) == ' '
        True
        >>> cel.set_hypothetic()
        >>> str(cel) == '?'
        True
        >>> cel.unset_hypothetic()
        >>> cel.reveal()
        >>> str(cel) == '0'
        True
        >>> cel.incr_number_of_bombs_in_neighborhood()
        >>> str(cel) == '1'
        True
        >>> cel.set_bomb()
        >>> str(cel) == 'B'
        True
        """

        if self.__revealed :
            if self.__bomb :
                return 'B'
            else :
                return str(self.__nbBombs)
        elif self.__hypo :
            return '?'
        else :
            return ' '



if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=True)
