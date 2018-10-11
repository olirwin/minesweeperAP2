#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:mod:`minesweeper` module

:author: HERE YOUR NAME

:date:

This module provides functions and a class for minesweeper's game's management.

"""

import random
from enum import Enum
from cell import Cell


################################################
# Type declaration
################################################

class GameState(Enum):
    """
    A class to define an enumerated type with three values :

    * ``winning``
    * ``losing``
    * ``unfinished``

    for the three state of minesweeper game.
    """
    winning = 1
    losing = 2
    unfinished = 3


##############################################
# Function for game's setup and management
##############################################


def neighborhood(x, y, width, height):
    """
    :param x: x-coordinate of a cell
    :type x: int
    :param y: y-coordinate of a cell
    :type y: int
    :param height: height of the grid
    :type height: int
    :param width: widthof the grid
    :type width: int
    :return: the list of coordinates of the neighbors of position (x,y) in a
             grid of size width*height
    :rtype: list of tuple
    :UC: 0 <= x < width and 0 <= y < height
    :Examples:

    >>> neighborhood(3, 3, 10, 10)
    [(2, 2), (2, 3), (2, 4), (3, 2), (3, 4), (4, 2), (4, 3), (4, 4)]
    >>> neighborhood(0, 3, 10, 10)
    [(0, 2), (0, 4), (1, 2), (1, 3), (1, 4)]
    >>> neighborhood(0, 0, 10, 10)
    [(0, 1), (1, 0), (1, 1)]
    >>> neighborhood(9, 9, 10, 10)
    [(8, 8), (8, 9), (9, 8)]
    >>> neighborhood(3, 9, 10, 10)
    [(2, 8), (2, 9), (3, 8), (4, 8), (4, 9)]
    """

    neighbors = [(x-1, y-1), (x-1, y), (x-1, y+1), (x, y-1), (x, y+1), (x+1, y-1), (x+1, y), (x+1, y+1)]
    return [(u, v) for (u, v) in neighbors if (u in range(width) and v in range(height))]



class Minesweeper():
    """
    >>> game = Minesweeper(20, 10, 4)
    >>> game.get_width()
    20
    >>> game.get_height()
    10
    >>> game.get_nbombs()
    4
    >>> game.get_state() == GameState.unfinished
    True
    >>> cel = game.get_cell(1, 2)
    >>> cel.is_revealed()
    False
    """

    def __init__(self, width=30, height=20, nbombs=99):
        """
        build a minesweeper grid of size width*height cells
        with nbombs bombs randomly placed.

        :param width:[optional] horizontal size of game (default = 30)
        :type width: int
        :param height: [optional] vertical size of game (default = 20)
        :type height: int
        :param nbombs: [optional] number of bombs (default = 99)
        :type nbombs: int
        :return: a fresh grid of  width*height cells with nbombs bombs randomly placed.
        :rtype: Minesweeper
        :UC: width and height must be positive integers, and
             nbombs <= width * height
        :Example:

        >>> game = Minesweeper(20, 10, 4)
        >>> game.get_width()
        20
        >>> game.get_height()
        10
        >>> game.get_nbombs()
        4
        >>> game.get_state() == GameState.unfinished
        True
        >>> game.set_state(losing)
        >>> game.get_state() == GameState.unfinished
        False
        >>> game.get_state() == GameState.losing
        True
        >>> game.reveal_all_cells_from(4, 2)
        >>> game.get_cell(4, 2).is_revealed()
        True
        """

        assert nbombs <= (width * height), "You can't have more bombs than cells"

        self.__width = width
        self.__height = height
        self.__nbBombs = nbombs
        self.__nbCellsUnrevealed = height * width
        self.__gameState = GameState.unfinished
        self.__grid = []

        #On crée des cellules de classe cell, pour l'instant vides de tout contenu

        for i in range(self.__height) :
            line = []
            for j in range(self.__width) :
                line.append(Cell())
                line[j].set_coords(j, i)
            self.__grid.append(line)

        #On ajoute ensuite des bombes à des endroits aléatoires

        bombsPlaced = 0
        bombList = []
        while bombsPlaced < self.__nbBombs :
            x = random.randint(0, self.__width - 1)
            y = random.randint(0, self.__height - 1)
            randCoords = (x, y)
            if randCoords not in bombList :
                bombList += [randCoords]
                self.get_cell(x, y).set_bomb()
                bombsPlaced += 1

        # Il faut ensuite indiquer le nombre de bombes voisines a chaque cellule

        for i in range(self.__height) :
            for j in range(self.__width) :
                if (j, i) not in bombList :
                    for (u, v) in neighborhood(j, i, self.__width, self.__height) :
                        if self.get_cell(u, v).is_bomb() :
                            self.get_cell(j, i).incr_number_of_bombs_in_neighborhood()


    def get_height(self):
        """
        :return: height of the grid in self
        :rtype: int
        :UC: none
        """

        return self.__height

    def get_width(self):
        """
        :return: width of the grid in game
        :rtype: int
        :UC: none
        """

        return self.__width

    def get_nbombs(self):
        """
        :return: number of bombs in game
        :rtype: int
        :UC: none
        """

        return self.__nbBombs


    def get_cell(self, x, y):
        """
        :param x: x-coordinate of a cell
        :type x: int
        :param y: y-coordinate of a cell
        :type y: int
        :return: the cell of coordinates (x,y) in the game's grid
        :type: cell
        :UC: 0 <= x < width of game and 0 <= y < height of game
        """

        return self.__grid[y][x]

    def get_nbCellsUnrevealed(self) :
        """
        Returns the numberof unrevealed cells in the game

        :return: number of cells with cell.is_revealed() == False
        :rtype: int
        :UC: none
        """
        return self.__nbCellsUnrevealed

    def get_state(self):
        """
        :return: the state of the game (winning, losing or unfinished)
        :rtype: GameState
        :UC: none
        """

        return self.__gameState

    def set_state(self, gameState) :
        """
        Sets the game's GameState to gameState

        :param gameState: the state to set the game to
        :type gameState: GameState
        :return: None
        :side effect: changes the gameState
        """
        self.__gameState = gameState

    def reveal_all_cells_from(self, x, y):
        """
        :param x: x-coordinate
        :param y: y-coordinate
        :return: none
        :side effect: reveal all cells of game game from the initial cell (x,y).
        :UC: 0 <= x < width of game and 0 <= y < height of game
        """

        for i in range(y, self.__height) :
            for j in range (x, self.__width) :
                self.__grid[i][j].reveal()

    def reveal_all_clear_cells_from(self, x, y) :
        """
        Reveals all the clear cells from an initial (x, y) coordinate in all directions \
        until it encounters a cell with a non-zero number of bombs in it's neighborhood.

        :param x: x-coordinate
        :type x: int
        :param y: y-coordinate
        :type y: int
        :return: none
        :side effect: reveals all cells of the game around the (x, y) cell that are empty of bombs
        :UC: 0 <= x < width of game and 0 <= y < height of game
        """

        assert x in range(0, self.__width), "x must be between 0 and the game width"
        assert y in range(0, self.__height), "y must be between 0 and the game height"

#        if not self.get_cell(x, y).is_revealed():
#            lost = 0
#            self.get_cell(x, y).reveal()
#            self.__nbCellsUnrevealed -= 1
#            if self.get_cell(x, y).is_bomb() :
#                self.set_state(GameState.losing)
#                lost += 1
#            if self.get_cell(x, y).number_of_bombs_in_neighborhood() == 0 and lost == 0:
#                for (u, v) in neighborhood(x, y, self.__width, self.__height) :
#                    self.reveal_all_clear_cells_from(u, v)
#        if self.__nbCellsUnrevealed == self.__nbBombs :
#            self.set_state(GameState.winning)


        cell = self.get_cell(x, y)

        if cell.is_bomb() :
            cell.reveal()
            self.set_state(GameState.losing)
        else :
            if not cell.is_revealed() :
                cell.reveal()
                self.__nbCellsUnrevealed -= 1
                if cell.number_of_bombs_in_neighborhood() == 0:
                    for (u, v) in neighborhood(x, y, self.__width, self.__height) :
                        self.reveal_all_clear_cells_from(u, v)

        if self.__nbCellsUnrevealed == self.__nbBombs :
            self.set_state(GameState.winning)



    def reveal_clear_cells_if_not_hypothetic(self, x, y):
        if not self.get_cell(x, y).is_hypothetic():
            self.reveal_all_clear_cells_from(x, y)










if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=True)
