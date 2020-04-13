Patterns using higher-order function to **TRANSFORM THE STRUCTURE OF THE DATA**.

- **Wrap** objects to create more complex objects
- **Unwrap** complex objects into their components
- **Flatten** a structure
- **Structure** a flatten sequence

# Map and filter

f(x) - a function
C    - a collection
b    - a condition

## Map

- map function
```python
  map(f, C)
```

- generator expression
```python
  (f(x) for i in C)
```

- generator function
```python
  def mymap(f, C):
    for x in C:
      yield f(x)
```

## Filter

- filter function
```python
  filter(b, C)
```

- generator expression
```python
  (x for i in C if b(x))
```

- generator function
```python
  def myfilter(b, C):
    for x in C:
      if b(x)
        yield x
```

"Of course, we can combine mapping and filtering to create yet more complex
functions. It might seem like a good ideia to create more complex functions
to limit the amount of processing. This isn't always true; a complex function
might not beat the performance of a nested use of simple map() and filter()
functions. Generally, we only want to create a more complex function if it
encapsultates a concept and makes the software easier to understand."
