import random
import os
os.system('cls' if os.name == 'nt' else 'clear')

d = random.randint(1,20)
if d == 20:
    print(f"{d}\tSucces Critique?!")
elif d == 1:
    print(f"{d}\tEchec Critique...")
else:
    print(d)
