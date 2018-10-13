# DÉMINEUR - Versions console et graphique


Le Démineur est un jeu emblématique de nombreux systèmes d'exploitation à travers les âges. Nous nous proposons ici d'en réaliser une implémentation rédigée en Python, sous deux formes :

-- Une version console, plus adaptée à un format de jeu plus réduit
-- Une version graphique, correspondant à l'image la plus répandue du Démineur

### Installation

Le Démineur ne requiert aucune installation, il suffit d'extraire les fichiers de l'archive. Toute la documentation relative au jeu est accessible à l'aide de la commande :
```sh
$ make doc
```

Qui placera par défaut dans le dossier ‘doc’ les pages de documentation du projet

### Lancement

Pour lancer et jouer au Démineur : 
(À partir du dossier racine du projet)

- Version Graphique :
    - Sans paramètres :
        ```sh
        $ python3 src/graphical_main.py
        ```
    
    - Avec paramètres :
        ```sh
        $ python3 src/graphical_main.py x y n
        ```
    
        Avec $$x$$ la largeur de la grille, $$y$$ la hauteur, et $$n$$ le nombres de bombes
    

- Version Console :

    - Sans paramètres
        ```sh
        $ python3 src/console_main.py
        ```
    
    - Avec paramètres :
        ```sh
        $ python3 src/console_main.py x y n
        ```
    
        Avec $$x$$ la largeur de la grille, $$y$$ la hauteur, et $$n$$ le nombres de bombes
        
### Ajouts

-- La version console possède désormais une vraie grille
-- Un texte de présentation apparaît lors du lancement de la version console, permettant également de lancer un tutoriel pour les coups à jouer
-- Le titre de la fenètre de terminal change de la même manière que celui de la version graphique pour avoir une idée du nombre de bombes dans la grille

### TO-DOs

-- Ne plus rendre l'apparition du texte de présentation systématique à l'aide d'une option en ligne de commande
-- Ajouter les couleurs au jeu en terminal pour plus de lisibilité


								     . . .
								      \|/
								    `--+--'
								      /|\
								     ' | '
								       |
								       |
								   ,--'#`--. 
								   |#######|
								_.-'#######`-._                    
							     ,-'###############`-.
							   ,'#####################`,
							  /#########################\
							 |###########################|
							|#############################|
							|#############################|
							|#############################|
							|#############################|
							 |###########################|
							  \#########################/
							   `.#####################,'
							     `._###############_,'
								`--..#####..--'



