"""
Exercices concernant la programmation POO
Par: Qian Qian
Groupe: 407
"""

from module.string_foo import StringFoo
from module.rectangle import Rectangle
from module.cercle import Cercle
from module.hero import Hero

# Test StringFoo
string_foo = StringFoo()
string_foo.set_string("Hello World!")
string_foo.print_string()

# Test Rectangle
rectangle = Rectangle(24, 32)
rectangle.calcul_aire()
rectangle.afficher_infos()

# Test Cercle
cercle = Cercle(5)
print(f"Aire de cercle: {cercle.calcul_aire()}")
print(f"Circonference de cercle: {cercle.calcul_circonference()}")

# Test Hero
hero_1 = Hero("Austin")
hero_2 = Hero("Michael")
hero_1.attaque(hero_2)
hero_1.attaque(hero_2)
