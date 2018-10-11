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

    #On change le titre du terminal pour garder un oeil sur le nombre de bombes

    if nbombs == 1 :
        title = "Minesweeper for dummies ({:d} bomb)".format(nbombs)
    else :
        title = "Minesweeper ({:2d} bombs)".format(nbombs)

    sys.stdout.write("\x1b]0;%s\x07" % title)

    #Boucle principale du jeu

    while game.get_state() == GameState.unfinished:

        #On imprime le jeu dans une fenêtre de terminal propre

        os.system("clear")
        print_game(game)

        #On récupère le coup du joueur

        x = -1
        y = -1
        action = "Invalid"
        while (x not in range(width) or y not in range(height) or action not in ["R", "S", "U"]):
            try :
                x, y, action = input("\n Your play x, y, C (C=(R)eveal,(S)et,(U)nset): ").split(',')
                x = int(x)
                y = int(y)
                action = action.strip()
            except KeyboardInterrupt:
                raise KeyboardInterrupt()
            except :
                print("Your play is ill formed")
                continue

        print()
        apply_action(x, y, action, game)



    #Fin du jeu et vérification de l'état de la partie

    if game.get_state() == GameState.losing:
        os.system("clear")
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
    path = os.path.abspath(os.path.dirname(__file__))
    manual = open(os.path.join(path, "../texts/manual.txt"), "r")
    print(manual.read())
    manual.close()
    help = input()

    if help.upper()== "HELP" :
        os.system("clear")
        manual = open(os.path.join(path, "../texts/howtoplay.txt"), "r")
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
    #On crée les lignes horizontales

    #Modèle de ligne intermédiaires

    ligne_inter = "   "
    ligne_inter += "├───"
    for i in range(game.get_width()-1):
        ligne_inter += "┼───"
    ligne_inter += "┤"

    #Ligne du haut

    ligne_haut = "   "
    ligne_haut += "┌───"
    for i in range(game.get_width()-1):
        ligne_haut += "┬───"
    ligne_haut += "┐"

    #Ligne du bas

    ligne_bas = "   "
    ligne_bas += "└───"
    for i in range(game.get_width()-1):
        ligne_bas += "┴───"
    ligne_bas += "┘"

    #On imprime le jeu

    print("   " + " ".join("{:3d}".format(i) for i in range(game.get_width())))
    print(ligne_haut)
    for i in range(game.get_height()-1) :
        colonnes = "{:2d} ".format(i)
        for j in range(game.get_width()) :
            colonnes += "│ " + str(game.get_cell(j, i)) + " "
        colonnes += "│"
        print(colonnes)
        print(ligne_inter)
    colonnes = "{:2d} ".format(game.get_height()-1)
    for j in range(game.get_width()) :
        colonnes += "│ " + str(game.get_cell(j, game.get_height()-1)) + " "
    colonnes += "│"
    print(colonnes)
    print(ligne_bas)

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
        game.reveal_clear_cells_if_not_hypothetic(x, y)
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
