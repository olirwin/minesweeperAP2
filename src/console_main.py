"""
:mod:`main` module

:author: `FIL - IEEA - Univ. Lille1.fr <http://portail.fil.univ-lille1.fr>`_

:date:  201_, september. Last revision: 2018, september

Main module to play the minesweeper's game : console version


"""

import sys, os
from minesweeper import Minesweeper, GameState

def main() :
    """
    Main function to play a console version of the minesweeper game
    """

    #On dégage la console

    os.system("clear")

    #On prépare les variables

    if len(sys.argv) == 4:
        width = int(sys.argv[1])
        height = int(sys.argv[2])
        nbombs = int(sys.argv[3])
    else:
        width = 5
        height = 5
        nbombs = 5

    #On crée le jeu

    game = Minesweeper(width, height, nbombs)

    #Interface adorable de présentation

    game_manual()

    #Boucle principale du jeu

    while game.get_state() == GameState.unfinished:
        #On récupère le coup du joueur
        print_game(game)
        print("\n Your play x, y, C (C=(R)eveal,(S)et,(U)nset): ")
        x, y, action = input().split(', ')
        x = int(x)
        y = int(y)

        #On joue le coup
        apply_action(x, y, action, game)

    #Fin du jeu et vérification de l'état de la partie

    if game.get_state() == GameState.losing:
        apply_action(x, y, "E", game)
        print_game(game)
        print("\n YOU HAVE LOST THIS GAME... \n")
    else :
        print_game(game)
        print("\n WINNER ! \n")



def game_manual() :
    """
    The manual for the minesweeper game. Opens and reads into the console one or two files,\
    a welcome file (manual.txt) and if needed a help file (howtoplay.txt)

    :return: None
    :side effect: reads files
    :UC: none
    """
    manual = open("../manual.txt", "r")
    print(manual.read())
    manual.close()
    help = input()

    if help.upper()== "HELP" :
        os.system("clear")
        manual = open("../howtoplay.txt", "r")
        print(manual.read())
        input()

    os.system('clear')

def print_game(game) :
    """
    Prints the console output of the game

    :param game: the game to print
    :type height: Minesweeper
    :return: none
    :side effect: prints a grid in terminal
    :UC: none
    """
    #On designe la ligne horizontale
    ligne = "  "
    for i in range(game.get_width()):
        ligne += "+---"
    ligne += "+"

    #On imprime le jeu
    print("  " + "".join("{:4d}".format(i) for i in range(game.get_width())))
    for i in range(game.get_height()) :
        colonnes = "{:2d}".format(i)
        print(ligne)
        for j in range(game.get_width()) :
            colonnes += "| " + str(game.get_cell(j, i)) + " "
        colonnes += "|"
        print(colonnes)
    print(ligne)

def apply_action(x, y, action, game) :
    """
    Applies the parameter action to the game cell (x, y)

    :param x: x-coordinate of cell to play on
    :type x: int
    :param y: y-coordinate of cell to play on
    :type y: int
    :param action: action to apply ("R", "S" or "U")
    :type action: str
    :param game: the game we're playing
    :type game: Minesweeper
    :return: none
    :side effect: changes the state of the cell (x, y) with the action action
    :UC: none
    """
    cell = game.get_cell(x, y)
    if action == "R" :
        game.reveal_all_clear_cells_from(x, y)
    elif action == "S" :
        cell.set_hypothetic()
    elif action == "U" :
        cell.unset_hypothetic()
    elif action == "E" :
        game.reveal_all_cells_from(0, 0)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
