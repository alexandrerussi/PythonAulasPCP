import math

num = int(input("Digite um num: "))
raiz = math.sqrt(num)
print(f"A raiz de {num} é {raiz:.2f}")

graus = 45
radiano = graus / 180 * math.pi
seno = math.sin(radiano)
print(seno)

import random

num_random = random.random()
print(num_random)

num_random_int = random.randint(1, 10)
print(num_random_int)