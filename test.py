
'''
Avec lambda function + comprehension list
'''

l_function_plus = [lambda x:x+i for i in range(10)]

assert l_function_plus[3](10)==13, "Arggggg!"

'''
Avec lambda fonction dans un for
'''
l_function_plus = []
for i in range(10):
  l_function_plus.append(lambda x:x+i)

assert l_function_plus[3](10)==13, "Arggggg!"

'''
Avec des functions nommées
'''
l_function_plus = []
for i in range(10):
  def function_plus(x):
    return x + i
  l_function_plus.append(function_plus)

assert l_function_plus[3](10)==13, "Arggggg!"


#Toutes ces functions renvoient x+9
