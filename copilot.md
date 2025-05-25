Copilot said: Dans ton code, le problème vient du
Dans ton code, le problème vient du fait que la variable i est "capturée" par les fonctions lambda et les fonctions nommées, mais elles ne "mémorisent" pas la valeur de i au moment de leur création. Elles utilisent la valeur finale de i lorsqu'elles sont appelées, donc toutes tes fonctions renvoient x+9.

Pour obtenir une liste de fonctions qui renvoient bien x+1, x+2, x+3, ..., il faut passer i en argument par défaut dans la lambda ou la fonction nommée. Par exemple :

Python
# Avec lambda et argument par défaut
l_function_plus = [lambda x, i=i: x + i for i in range(10)]

# Test : chaque fonction renvoie x + i
print([f(10) for f in l_function_plus])  # Affiche : [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
Explications :

En écrivant lambda x, i=i: x + i, tu captures la valeur courante de i dans la fonction au moment où elle est créée.
Cela marche aussi pour une fonction nommée :
Python
l_function_plus = []
for i in range(10):
    def function_plus(x, i=i):
        return x + i
    l_function_plus.append(function_plus)
Résumé :
Utilise i=i en argument par défaut pour capturer la valeur de i dans chaque fonction de la liste.

N’hésite pas si tu veux une explication plus détaillée !
