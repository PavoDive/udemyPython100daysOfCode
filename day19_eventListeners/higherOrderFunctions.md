Higher order functions are functions that have other functions as arguments:

```
def add(n1, n2):
    return n1 + n2

def multiply(n1, n2):
    return n1 * n2
	
def calculator(n1, n2, func):
    return func(n1, n2)
```

In this case, `calculator` is a higher order function.
