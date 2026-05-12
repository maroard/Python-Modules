# Fiche de revision - Module 10 FuncMage

Objectif general du projet : comprendre les bases de la programmation fonctionnelle en Python.
Les fonctions sont des objets comme les autres : on peut les passer en argument, les retourner,
les stocker dans des variables, les combiner et les decorer.

## Exercice 0 - Lambda Sanctum

Fichier : `ex0/lambda_spells.py`

Theme principal : expressions lambda, `map`, `filter`, `sorted`, `min`, `max`.

Une `lambda` est une fonction anonyme courte :

```python
lambda x: x * 2
```

Elle est utile quand l'operation est simple et utilisee une seule fois, par exemple comme cle de tri
ou comme transformation dans `map`.

Fonctions a connaitre :

- `artifact_sorter(artifacts)` trie une liste de dictionnaires par `power` decroissant.
- `power_filter(mages, min_power)` garde seulement les mages dont la puissance est suffisante.
- `spell_transformer(spells)` transforme chaque sort en ajoutant `* ` au debut et ` *` a la fin.
- `mage_stats(mages)` calcule la puissance max, min et moyenne.

Idees importantes :

- `sorted(iterable, key=..., reverse=True)` retourne une nouvelle liste triee.
- `filter(lambda x: condition, iterable)` garde les elements qui verifient la condition.
- `map(lambda x: transformation, iterable)` transforme tous les elements.
- `max(..., key=lambda ...)` et `min(..., key=lambda ...)` permettent de comparer par un champ precis.

Exemple mental :

```python
sorted(artifacts, key=lambda artifact: artifact["power"], reverse=True)
```

Ici, la lambda dit a Python : "pour trier, regarde la valeur de `power`".

Question typique : quand utiliser `lambda` plutot qu'une fonction `def` ?

Reponse : utilise `lambda` pour une operation courte, lisible et locale. Utilise `def` si la logique
est longue, reutilisee, ou si elle merite un nom clair.

Pieges possibles :

- Oublier de convertir `map` ou `filter` en `list`.
- Trier dans le mauvais sens.
- Faire une division par zero si la liste de mages est vide. Le sujet ne demande pas explicitement
  ce cas, mais en evaluation on peut te demander comment tu le gererais.

## Exercice 1 - Higher Realm

Fichier : `ex1/higher_magic.py`

Theme principal : fonctions d'ordre superieur.

Une fonction d'ordre superieur est une fonction qui recoit une autre fonction en parametre,
ou qui retourne une fonction.

Contrat des sorts :

```python
def spell(target: str, power: int) -> str:
    ...
```

Toutes les fonctions de cet exercice manipulent des sorts qui prennent `target` et `power`.

Fonctions a connaitre :

- `spell_combiner(spell1, spell2)` retourne une nouvelle fonction qui lance les deux sorts.
- `power_amplifier(base_spell, multiplier)` retourne une fonction qui multiplie la puissance avant de lancer le sort.
- `conditional_caster(condition, spell)` retourne une fonction qui lance le sort seulement si la condition est vraie.
- `spell_sequence(spells)` retourne une fonction qui lance tous les sorts d'une liste dans l'ordre.

Idees importantes :

- Une fonction peut etre stockee dans une variable :

```python
mega_fireball = power_amplifier(fireball, 3)
```

- Une fonction peut etre retournee par une autre fonction :

```python
def power_amplifier(base_spell, multiplier):
    def amplified_spell(target, power):
        return base_spell(target, power * multiplier)
    return amplified_spell
```

- La fonction interne garde acces a `base_spell` et `multiplier`.

Question typique : que veut dire "first-class citizen" ?

Reponse : en Python, une fonction est une valeur comme une autre. On peut la passer en argument,
la retourner, la mettre dans une liste ou un dictionnaire, et l'assigner a une variable.

Question typique : pourquoi utiliser `Callable` ?

Reponse : `Callable` sert a typer une variable ou un parametre qui doit etre une fonction.
Le sujet recommande de l'importer depuis `collections.abc`.

Question typique : a quoi sert `callable()` ?

Reponse : `callable(obj)` renvoie `True` si `obj` peut etre appele avec des parentheses.
Exemple : une fonction est callable, une chaine de caracteres ne l'est pas.

Pieges possibles :

- Appeler le sort trop tot au lieu de retourner une fonction.
- Perdre la signature attendue `(target: str, power: int)`.
- Pour `conditional_caster`, oublier que la condition recoit les memes arguments que le sort.

## Exercice 2 - Memory Depths

Fichier : `ex2/scope_mysteries.py`

Theme principal : portee lexicale, closures, `nonlocal`.

Une closure est une fonction qui se souvient des variables de son environnement de creation,
meme apres la fin de la fonction externe.

Fonctions a connaitre :

- `mage_counter()` cree un compteur prive qui augmente a chaque appel.
- `spell_accumulator(initial_power)` cree un accumulateur de puissance.
- `enchantment_factory(enchantment_type)` fabrique une fonction specialisee.
- `memory_vault()` retourne un dictionnaire avec deux fonctions, `store` et `recall`, qui partagent une memoire privee.

Exemple cle :

```python
def mage_counter():
    call_count = 0

    def counter():
        nonlocal call_count
        call_count += 1
        return call_count

    return counter
```

`counter` se souvient de `call_count`. Chaque appel modifie la meme variable capturee.

Question typique : pourquoi `nonlocal` ?

Reponse : `nonlocal` permet de modifier une variable definie dans la fonction englobante.
Sans `nonlocal`, Python considererait `call_count` comme une nouvelle variable locale dans
`counter`, ce qui provoquerait une erreur au moment de faire `call_count += 1`.

Question typique : pourquoi `global` est interdit mais `nonlocal` autorise ?

Reponse : `global` modifie un etat partage par tout le programme, ce qui rend le code moins
previsible et moins pur. `nonlocal` garde l'etat enferme dans une closure : l'etat existe, mais
il reste prive et controle.

Difference importante :

- `local` : variable de la fonction actuelle.
- `nonlocal` : variable de la fonction externe.
- `global` : variable au niveau du module.

Pieges possibles :

- Mettre le compteur en variable globale.
- Creer une seule memoire partagee entre tous les vaults par erreur.
- Oublier que deux compteurs crees par deux appels differents doivent etre independants.

## Exercice 3 - Ancient Library

Fichier : `ex3/functools_artifacts.py`

Theme principal : `functools`, `operator`, `reduce`, `partial`, `lru_cache`, `singledispatch`.

Fonctions a connaitre :

- `spell_reducer(spells, operation)` reduit une liste d'entiers avec une operation.
- `partial_enchanter(base_enchantment)` cree des fonctions specialisees avec `partial`.
- `memoized_fibonacci(n)` calcule Fibonacci avec cache.
- `spell_dispatcher()` cree une fonction qui change de comportement selon le type de l'argument.

`reduce` :

```python
reduce(add, [10, 20, 30])
```

Calcule progressivement :

```text
10 + 20 = 30
30 + 30 = 60
```

`operator` :

- `operator.add` fait une addition.
- `operator.mul` fait une multiplication.
- On peut aussi utiliser `max` et `min`.

`partial` :

```python
partial(base_enchantment, 50, "fire")
```

Cree une nouvelle fonction ou certains arguments sont deja fixes. Il ne reste plus qu'a fournir
le `target`.

`lru_cache` :

```python
@lru_cache(maxsize=None)
def memoized_fibonacci(n):
    ...
```

Le resultat d'un appel est garde en memoire. Si on redemande le meme `n`, Python reutilise le
resultat au lieu de refaire tous les calculs.

`singledispatch` :

Permet d'avoir une fonction principale, puis des versions specialisees selon le type :

- `int` : sort de degats.
- `str` : enchantement.
- `list` : multi-cast.
- autre type : comportement par defaut.

Question typique : pourquoi la memoization est efficace pour Fibonacci ?

Reponse : sans cache, Fibonacci recalcule enormement de sous-resultats identiques.
Avec `lru_cache`, chaque valeur de `fib(n)` est calculee une seule fois puis reutilisee.

Pieges possibles :

- Ne pas gerer la liste vide dans `spell_reducer`.
- Ne pas lever ou gerer l'erreur pour une operation inconnue.
- Oublier que `partial` retourne une fonction, pas une chaine.
- Confondre surcharge classique et `singledispatch` : ici le dispatch depend du type du premier argument.

## Exercice 4 - Master's Tower

Fichier : `ex4/decorator_mastery.py`

Theme principal : decorateurs, `functools.wraps`, decorateur parametre, retry, `staticmethod`.

Un decorateur est une fonction qui prend une fonction et retourne une nouvelle fonction.
Il sert a ajouter un comportement sans modifier directement la fonction originale.

Schema classique :

```python
def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # code avant
        result = func(*args, **kwargs)
        # code apres
        return result
    return wrapper
```

Fonctions a connaitre :

- `spell_timer(func)` affiche le nom de la fonction, mesure le temps, puis retourne le resultat original.
- `power_validator(min_power)` cree un decorateur qui verifie la puissance avant d'appeler la fonction.
- `retry_spell(max_attempts)` relance une fonction si elle leve une exception.
- `MageGuild.validate_mage_name(name)` valide un nom sans utiliser `self`.
- `MageGuild.cast_spell(self, spell_name, power)` utilise le decorateur de validation.

`functools.wraps` :

`wraps(func)` conserve les metadonnees de la fonction originale, comme son nom, sa docstring
et certaines infos utiles au debug.

Decorateur parametre :

```python
@power_validator(10)
def cast_spell(...):
    ...
```

Ici, `power_validator(10)` est appele d'abord. Il retourne ensuite le vrai decorateur.

Question typique : separation of concerns ?

Reponse : les decorateurs permettent de separer la logique principale et les comportements
transversaux. Par exemple, le sort fait son travail, tandis que le decorateur gere le timing,
la validation ou les retries.

Question typique : difference entre `@staticmethod` et methode d'instance ?

Reponse :

- Une methode d'instance recoit `self` et peut acceder a l'etat de l'objet.
- Une `staticmethod` ne recoit pas `self`. Elle est rangee dans la classe car elle est liee au concept
  de la classe, mais elle ne depend pas d'une instance.

Pieges possibles :

- Oublier `return result` dans un wrapper.
- Oublier `@wraps(func)`.
- Attraper une exception dans `retry_spell` mais ne pas retenter correctement.
- Dans un decorateur applique a une methode, oublier que le premier argument est `self`.
- Pour `cast_spell(self, spell_name, power)`, la puissance est donc souvent dans `args[2]`.

## Questions de peer-review a savoir expliquer

Pourquoi la programmation fonctionnelle aide ?

Elle favorise des fonctions petites, composables et reutilisables. On peut construire un comportement
complexe en combinant des fonctions simples.

Quelle difference entre transformation et effet de bord ?

Une transformation prend une entree et produit une sortie. Un effet de bord modifie quelque chose
ailleurs : affichage, fichier, variable globale, reseau, etc. Le projet encourage les transformations
claires et limitees.

Pourquoi eviter les variables globales ?

Elles rendent le programme plus difficile a comprendre, tester et debugguer, car n'importe quelle partie
du code peut modifier l'etat partage.

Comment reconnaitre une closure ?

Une fonction interne utilise une variable definie dans une fonction externe, puis cette fonction interne
est retournee ou utilisee apres la creation.

Comment reconnaitre une fonction d'ordre superieur ?

Elle prend une fonction en argument ou retourne une fonction.

Comment expliquer un decorateur simplement ?

Un decorateur enveloppe une fonction dans une autre fonction pour ajouter un comportement autour de
l'appel original.

## Mini check-list avant evaluation

- Tous les fichiers sont dans les bons dossiers : `ex0` a `ex4`.
- Les signatures demandees dans le PDF sont respectees.
- Les fonctions retournent les bons types.
- Les exemples dans les `main()` s'executent.
- Pas de bibliotheque externe.
- Pas de `eval()` ni `exec()`.
- Pas de variable globale pour garder l'etat.
- Savoir expliquer chaque `lambda`, chaque fonction retournee, chaque closure et chaque decorateur.
