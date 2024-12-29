def cube (a):
    return a * a * a
def three (a):
    if a % 3 == 0:
        return cube(a)
    else:
        return False
a = int(input("Enter number: "))
print(three(a))


def square (a):
    return a * a 
def two (a):
    if a % 2 == 0:
        return square(a)
    else:
        return False
a = int(input("Enter number: "))
print(two(a))