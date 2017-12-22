from math import sqrt


#  Non-curried version of quadratic formula (abc-formule)
def quadratic_formula(a, b, c):
    d = b ** 2 - 4 * a * c
    if d < 0:
        return None
    elif d == 0:
        return (-1 * b) / (2 * a)
    else:
        return (-1 * b - sqrt(d)) / (2 * a), (-1 * b + sqrt(d)) / 2 * a


def curried_quadratic_formula(a):
    def function1(b):
        def function2(c):
            d = b ** 2 - 4 * a * c
            if d < 0:
                return None
            elif d == 0:
                return (-1 * b) / (2 * a)
            else:
                return (-1 * b - sqrt(d)) / (2 * a), (-1 * b + sqrt(d)) / 2 * a

        return function2

    return function1


print("normal results:")
print(quadratic_formula(1, 5, 6))
print(quadratic_formula(1, 0, 16))
print(quadratic_formula(1, 2, 1))

print("\nCurried results")
print(curried_quadratic_formula(1)(5)(6))
print(curried_quadratic_formula(1)(0)(16))
print(curried_quadratic_formula(1)(2)(1))
