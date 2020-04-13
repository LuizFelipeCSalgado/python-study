Two broad species of functions:

1. Scalar - apply to individual values and compute individual result
2. Collection - work with iterable collections
    2.1 Reduction - fold values to a resulting value
    2.2 Mapping - applies a function to all items of a collection - results a
                  collection with the same size
    2.3 Filter - applies a function to all items of a colection - results a
                 collection with a subset of the input

        reduction          mapping           filter
input   collection  collection               collection
output  value       collection (same size)   subset of input


One common application of for loop iterable processing is the
    unwrap(process(wrap(iterable)))
    wrap(wrap(wrap()))
design patterns
    wrap - transform each item of an iterable into a two tuples with a derived
           sort key or other value and then the imutable item => (key, item)
    unwrap - discard the value (key) used to wrap

It's important to note that a good functional design allow us to freely replace
any function with its equivalent, which makes refactoring quite simple. We've
tried to achieve this goal when we provide alternative implementations of the
various functions.
(pg 81)

The perely functional viewpoint is that ALL OF OUR ITERABLES CAN BE PROCESSED
WITH RECURSIVE FUNCTIONS, where the STATE IS MERELY THE RECURSIVE CALL STACK.

"Simplicity means we're somewhat less likely to confuse the precessing state"

---

not all(isprime(x) for x in someset) # AND reduction
any(not isprime(x) for x in someset) # OR  reduction


outliers - discrepante
broad - amplo, extenso, geral, principal, óbvio
stray - disperso
