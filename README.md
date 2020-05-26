# MyFaithIsMySword
This personal project is a work in progress of a multiplayer dice game. Currently, rules below are in French and will be translated in English at the end, all comments in the code are in English.

### How to start a game ?
Launch the game.py file.

# Règles
Les joueurs constituent un village dans un univers "heroic fantaisy".
Tout le monde commence en tant que villageois, saurez-vous vous élevez au rang de Dieu et en tirer avantage pour gagner ?
A moins que vous craignez d'être déchus en redevenant un membre du village et que vous vous chachez du courroux du nouveau Dieu ... 
Le but est de prendre le moins, ou bien de donner le plus ! \o/
Les festivités sont lancés par le joueur le plus motivé et son premier lancé de dés.


Matériel requis : 3D6 dont un clairement distinguable des autres (Spécial -> S) => [x][y][S] 
<!-- -->
Nombre de joueurs recommandés : 5 à 10 (moins, c'est chaud et plus c'est le bordel)


### REGLES GENERALES :
- Deux joueurs ne peuvent pas avoir le même rôle.

- Tous les rôles sont cumulables sauf pour les cas indiqués.

- [6][y][S] => Donne la valeur [x] (ex : [6][2][S] => Donne 2)

- [5][1][S] et [4][2][S] => Tout le monde prend la valeur de [S] (N'applique pas l'effet du Dragon, ni de la Princesse et de l'Ecuyer)

- Deux joueurs consécutifs font le même score => Duel : 
Les deux joueurs lancent chacun un dé : [J1] et [J2]
Le perdant prend le résultat de la différence de la valeur des dés lors du duel. En cas d'égalité, un second tour est nécessaire où le perdant aura le résultat *2)

- Un lancé de dé qui ne génère aucun éévénement fait prendre 1 au lanceur. i.e. Tu sers à rien = tu prends 1.


### ROLES :


#### --- DIEU ---
Rôle DOMINANT ! Lorsqu'on devient Dieu, on n'est plus ni Héro, ni Catin, ni Ecuyer.


Devient Dieu :
[4][4][S] ou [5][5][S] => Ces lancers de dés provoque une Bataille de Dieux entre l'ancien Dieu et le prétendant :
Un duel entre les deux se lance, mais le perdant prend *2 dès le premier tour tandis que le gagnant devient/reste le Dieu
[6][6][S] => Le lanceur devient Dieu et donne 6 (par tradition les 6 vont à l'ancien Dieu ...)

DIEU ATTAQUE LE VILLAGE :
Lorsque la somme des dés fait 7, [x][y][S] où [x] + [y] = 7 => Donne le plus grand des 2 dés (ex : [4][3][S] => Donne 4 aux habitants du village)


#### ---HEROS---
Le Héros a pour rôle de s'interposer lorsque Dieu abat son courroux sur le village en l'attaquant.
Celui-ci ne peut être déjà Dieu. Dans ce cas, Dieu, qui a fait un lancé pour devenir Héros, doit nommer le prochain Héros.

Devient Héros :
[1][1][S] ou [2][2][S] ou [3][3][S]

Quand Dieu attaque le village ([x] + [y] = 7), le Héros s'interpose en lançant 1 dé :
- [1] 		=> Le Héros est FOUDROYE : Prends 6 et perds son rôle de Héros.
- [2] ou [3] 	=> Tout le vilage subit le courroux de Dieu et prends la valeur en jeu.
- [4] ou [5]	=> Le Héros protège le village en étant le seul à prendre.
- [6] 		=> Dieu prend tout seul et ne distribue rien.


#### ---ORACLE---
L'Oracle tente de prédire le lancé du Héros avant qu'il ne s'interpose pour protéger le village.
Après le lancé du Héros, il peut changer le score du Héros en le décalant de 1 vers sa prédiction.
Si sa prédiction est/devient exacte, l'Oracle a le pouvoir de donner la valeur de sa prédiction à n'importe qui.

Devient Oracle :
[2][1][S]


#### ---Ecuyer---
L'Ecuyer assite toujours son Héros. Donc, quand ce dernier prend, l'Ecuyer prend avec lui la même valeur.
Pour devenir Ecuyer, il doit déjà y avoir un Héros dans le village.
On ne peut pas être Ecuyer si on est Dieu ou Héros.

Devient Ecuyer :
[3][1][S]

Si le Héros perds son rôle, on n'est plus Ecuyer non plus.
Un Ecuyer peut prendre la place du Héros précédent.


#### ---Prisonnier---
Le villageois entre en prison, si il n'y a pas déjà un prisonnier dedans, et prend la valeur du dé [S] pour célébrer son entrée.
Quand un 3 sort sur les dés [x][y], le prisonnier prend 1.
Pour sortir de sa prison, il doit réaliser un 3 sur une des faces des dés [x][y], puis prend la valeur du dé [S] pour célébrer sa sortie.
Cependant, si il fait [3][2][S] en tentant de sortir, le villageois a le plaisir de sortir et rerentrer dans la prison, du coup il prend 2* la valeur du dé [S] pour ce magnifique lancé.

Devient Prisonnier :
[3][2][S]


#### ---Catin---
Le villageois qui devient la Catin permet au village d'avoir une autre chance que le Héros de se protéger du courroux de Dieu.
Par conséquent, on ne peut pas devenir Catin si on est déjà Dieu.

Devient Catin :
[4][1][S]

La Catin s'interpose avant le Héros quand Dieu attaque le Village :
- [1] : Dieu prend la valeur de son attaque et ne donne rien
- [2], [3], [4], [5], [6]	: La catin boit son résultat en gorgées

L'Oracle n'intervient pas sur le lancer de la Catin.

#### ---Aubergiste---
L'Aubergiste a la possibilité à chaque fois que quelqu'un prend d'influencer le score soit en l'alégeant (- 1) soit en l'alourdissant (+ 1) et ce de manière individuelle.

Devient Aubergiste :
[5][3][S]


#### ---Princesse---
La Princesse a la possibilité de donner la moitié de ce qu'elle prend avec le Héro. (Le score est arrondis au plus bas : 5/2 = 2)
De ce fait, le joueur qui est déjà Héro ne peut pas devenir Princesse.

Devient Princesse :
[5][4][S]


#### ---DRAGON---
Quand il recoit des points, le Dragon peut souffler à sa droite ou à sa gauche.
Il donne le score divisé par 2 à chaque personne en chaine (on s'arrête à 1)

Devient Dragon et donne 5
[6][5][S]
