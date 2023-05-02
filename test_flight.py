
from functools import lru_cache

#FIVE_NAMES = ['A', 'B', 'C', 'D', 'E']
SIX_NAMES = ['Alice', 'Bob', 'Carol', 'Dave', 'Eve', 'Frank']

AGES = [34, 25, 56, 18, 30, 42] 


MAP_NAME_TO_AGE = { name: age for name, age in zip(SIX_NAMES, AGES)}

def average_age():
    return sum(AGES) / len(AGES)    


# recursive function
# fibonacci definition: f(n) = f(n-1) + f(n-2)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)  

# runs much faster because of the caching component
@lru_cache(maxsize=None)
def fibonacci_cached(n):
    if n < 2:
        return n
    return fibonacci_cached(n-1) + fibonacci_cached(n-2)    


