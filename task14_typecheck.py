def egcd(a: int, b: int) -> tuple:
    """
    Returns a tuple (d, x, y) where d is gcd(a, b), x and y are coefficients such that d = ax + by.
    This time it's typechecked!
    """
    if b == 0:
        return a, 1, 0
    else:
        d, x, y = egcd(b, a % b)
        return d, y, x - y * (a // b)

print(egcd(123.0, 18.0))
# Argument 1 to "egcd" has incompatible type "float"; expected "int"
# Argument 2 to "egcd" has incompatible type "float"; expected "int"

print(egcd(642, 248))