def primeNumbersList(x: int):
    primeNumbers = []
    for i in range(2, x):
        isPrime = True
        for j in primeNumbers:
            if i % j == 0:
                isPrime = False
                break
        if isPrime:
            primeNumbers.append(i)
    print(primeNumbers)

primeNumbersList(100)


