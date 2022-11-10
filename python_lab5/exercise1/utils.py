import math


def process_item(x: str) -> int:
    number = float(x)
    potential_prime = int(number) + 1
    if number < 2:
        return 2
    while 1:
        is_prime = True
        for i in range(2, int(math.sqrt(potential_prime)) + 1):
            if potential_prime % i == 0:
                is_prime = False
                break
        if is_prime:
            return potential_prime
        potential_prime += 1


def is_float(to_convert):
    try:
        float(to_convert)
        return True
    except ValueError:
        return False
