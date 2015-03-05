# PyPlan
Create planning according to doodle.

french:
Hey ! J'ai codé un programme pour organiser les plannings de permanences en fonction de ce que les gens ont mis sur le doodle :D
Alors, c'est très simple: on fait comme d'habitude, on met chacun nos disponibilités sur le Doodle (pour les permanences). Et là, il faudra sélectionner avec la souris presque toute la page doodle, et tout coller dans un fichier de mon programme qui s'appelle "input.txt". Ensuite, on lance le programme en double cliquant sur "pyPlan.exe", et il en ressort un autre fichier "OUTPUT.txt" avec tous les heures réparties équitablement. Il faudra ensuite le copier et le coller sur facebook et voili voilou 8-)

Quelques règles pour que ca fonctionne correctement:
- Sur le doodle, dans la case "nom" il faut mettre au max un nom composé de 2 parties. Pas plus ! Pas de parenthèse, ni tiret.
- Pour les horaires du doodle, utiliser seulement les nombres, ":", "-" et " ". Rien de plus.
Enfaite, ces règles peuvent être éviter en modifiant l'expression régulier qui est défini dans le programme. Ca se fait facilement, mais il faut la nouvelle expression. Donc si vous voulez, je peux m'occuper de faire les plannings. Mais si un jour j'ai plus envie, ben respectez ces règles x)

Inconvénients du programme par rapport à un humain:
- Il n'y a pas le facteur humain, c'est à dire que si deux personnes ne s'aiment pas, le programme ne le sait pas, et il peut quand même les mettre ensemble. Il faudra donc modifier dans le fichier final si besoin est. Vice versa, si deux personnes s'aiment, il ne le sait pas.
- Pas d’intelligence: le programme a été codé pour être équitable. Il n'a pas été optimisé pour "arranger" les plannings: c'est à dire que il peut très bien vous mettre par exemple pour l'ouverture et la fermeture en sautant le milieu. Il faudra modifier par la suite si vous voulez vous arranger entre vous.
- Utilisation de l'aléatoire: les plannings sont générés méthodiquement, mais il y a une part d'aléatoire dedans. Ainsi un même doodle peut générer deux plannings différents.

Améliorations possibles:
- Déjà, régler les Inconvénients.
- Ajouter une liste des "remplaçants" au cas où quelqu'un a un empêchement.
- Faire une interface graphique.
