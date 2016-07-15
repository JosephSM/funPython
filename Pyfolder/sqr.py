#stupid square
def square(n):
    if n == 1:
        return 1
    return square(n-1) + (2*(n-1) + 1)
print(square(100))
