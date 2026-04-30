# Day 59 - Function Caching in Python

from functools import lru_cache

# function without caching
def square(num):
    print(f"Calculating square of {num}")
    return num * num

print(square(4))
print(square(4))


print("\nUsing Function Caching:\n")

# function with caching
@lru_cache(maxsize=None)
def cube(num):
    print(f"Calculating cube of {num}")
    return num * num * num

print(cube(3))
print(cube(3))
print(cube(5))
print(cube(5))
