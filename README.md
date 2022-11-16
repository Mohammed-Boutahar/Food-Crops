# Python project

Membres du Groupe:

   - Boutahar Mohammed 
   - El Ajjouri Safaa
   - Sardi Ihssane


1- Environnement de développement :<br>
<p>Dans ce projet, nous avons travaillé avec le système d'exploitation Windows et une version Python de 3.8.8. Quant à l'environnement de développement, nous avons choisi d'utiliser PyCharm. </p>

2- Commande pour lancer le projet:<br>
<p>Il faut d'abord se placer dans le répertoire contenant l'ensemble du projet depuis un terminal puis exécuter la commande suivante :</p>
 >   "py main.py"<br>
Puisque la fonction main qui permet d'exécuter le programme se trouve dans le fichier foodCropsDataset.py<br>

<br>

<i>datasetTest = FoodCropsDataset()<br>

def main():<br>
>>>datasetTest.load("./csv/FeedGrains.csv")<br>

if name == 'main':<br>
>>> print(main())<br>
>>> a = int(input("entrez le groupe indicateur"))<br>
>>> b = str(input("entrez la localisation"))<br>
>>> c = int(input("entrez l'unité"))<br>
>>> d = int(input("entrez la commodité"))<br>
>>> FoodCropsDataset.findMeasurements(a, b, c, d)<br>
>>> main()<br></i>

<br>


3- Répartition des tâches : <br>
<p>L’objectif du projet est de réaliser les quatre opérations (O1, O2, O3, O4). Ainsi, la répartition qui nous a semblé judicieuse c'est de travailler chacun sur 1 opération de même complexité et d'effectuer des réunions à chaque reprise pour discuter l'avancement de chacun de nous par rapport au codage de son opération. Puis, nous nous sommes rassemblées  pour en discuter de l'opération O4 et la réaliser ensemble. A la fin, nous avons combiné les travaux pour enfin obtenir un code complet et persistant.</p>

Expliquons le travail réalisé au sein de chaque opération:<br>

O1 : Création de l'API Objet pour pouvoir manipuler le jeu de données.<br>

O2 : Chargement du jeu de données avec réutilisation des instances en utilisant la fonction suivante :<br>

 >>><i>def load(self, datasetPath: str)</i><br>

(qu'on peut trouver dans la classe FoodCropsDataset)<br>

O3 : Génération de la description d’une mesure en utilisant la fonction abstraite describe(self).<br>

O4 : Recherche de mesures selon quatre critères: le type de culture vivrière,
le type d’indicateur, la localisation g´eographique, l’unit´e de mesure.<br>

4- Problèmes rencontrés avec Solutions :  <br>
 - Utiliser les notions de la POO en python, en lisant les supports fournis par le professeur pour pouvoir l'exploiter dans le projet <br>
 - Comprendre le diagramme UML pour pouvoir traduire ce dernier en code correctement et demander à chaque fois l'aide du professeur pour avancer dans le projet <br>
 - Difficulté de répartir les taches équitablement. Et du coup la solution était de se réunir à plusieurs reprises pour voir l'avancement de chacun et de s'entraider<br>
 - Le problème principal était la fonction findMeasurement(...) qui nous a pris beaucoup de temps pour s'implémenter et qui peut ne pas fonctionner dans certains cas selon les paramètres données à la fonction.<br>

Conclusion : <br>

<p>Ce TP était une opportunité pour manipuler les données avec Python tout en exploitant les concepts de la programmation orientée objet, vu qu’il s’agit de notre première expérience avec un tel projet.</p>
