# Napisz program wyznaczający ciąg _Fibonacciego_ dla 93 elementu (lub 93 iteracji) 
# w najszybszym możliwym czasie.

def fibo(iteration: int) -> list[int]:
    if iteration <= 0: return []
    if iteration <= 1: return [0]
    fib=[0,1]
    for _ in range(2,iteration):
        fib.append(fib[-1]+fib[-2])
    return fib

print(fibo(100))
