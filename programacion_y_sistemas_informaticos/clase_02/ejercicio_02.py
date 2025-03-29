def collatz(x):
    c = 0
    while x != 1:
        if x % 2 == 0:
            x = x / 2
        else:
            x = 3 * x + 1
        c += 1
    return print(f"La cantidad de pasos son {c}")

collatz(25)