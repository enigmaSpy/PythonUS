from random import randint

def averageRandom():
    x:int = 1_000_000
    total:int =0
    for _ in range(x):
        total+=randint(1,10)
    print(f"Średnia wartośc:{float(total/x)}")
averageRandom()