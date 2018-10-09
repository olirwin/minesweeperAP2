============================
:mod:`graphicalboard` module
============================

Ce module fournit essentiellement une fonction de création d'une fenêtre graphique pour
jouer au démineur. Il nécessite les modules :mod:`cell` et :mod:`minesweeper`.

* Création d'une fenêtre de jeu :
  
  .. autofunction:: graphicalboard.create

* Gestion des évènements (clics) :

  .. autofunction:: graphicalboard.__changestate
  .. autofunction:: graphicalboard.__changeflag
  .. autofunction:: graphicalboard.__redraw

* Gestion de la partie (gagnant / perdant) :

  .. autofunction:: graphicalboard.__test_end
  .. autofunction:: graphicalboard.__block_game
  .. autofunction:: graphicalboard.__disable_game
